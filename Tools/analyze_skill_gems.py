#!/usr/bin/env python3
"""Offline proposed skill-gem model; no Unity or third-party dependencies."""
from __future__ import annotations
import argparse, ast, collections, copy, hashlib, heapq, itertools, json, math, platform, random, re, statistics, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"Docs/Design/Models/SkillGems/catalog.json"
EPS=1e-8

def load_catalog(path=CATALOG):
    def unique(pairs):
        out={}
        for key,value in pairs:
            if key in out: raise ValueError("Duplicate JSON key: "+key)
            out[key]=value
        return out
    return json.loads(Path(path).read_text(encoding="utf-8"),object_pairs_hook=unique)

def index(data,key):
    return {x["id"]:x for x in data[key]}

def level_from_xp(xp,growth):
    if type(xp) is not int or xp<0: raise ValueError("XP must be a nonnegative integer")
    level=1
    while level<growth["max_level"]:
        cost=growth["xp_per_next_level_factor"]*level
        if xp<cost: break
        xp-=cost
        level+=1
    return level

def settle_xp(state,clear_id,star,equipped,data,success=True):
    if not isinstance(clear_id,str) or not clear_id: raise ValueError("Clear ID required")
    if type(star) is not int or not 1<=star<=5: raise ValueError("Invalid star")
    known=set(index(data,"skills"))|set(index(data,"supports"))
    if set(equipped)-known: raise ValueError("Unknown gem")
    out=copy.deepcopy(state)
    if not success or clear_id in out["settled"]: return out
    g=data["growth"]
    base=g["equipped_xp_per_star"]*star
    cap=g["xp_per_next_level_factor"]*sum(range(1,g["max_level"]))
    for gem in known:
        amount=base if gem in set(equipped) else int(base*g["unequipped_fraction"])
        out["xp"][gem]=min(cap,out["xp"].get(gem,0)+amount)
    out["settled"].append(clear_id)
    return out

def compatible(skill,pair,supports,weapon=None,weapons=None):
    if len(pair)>2 or len(set(pair))!=len(pair) or set(pair)-set(supports): return False
    tags=set(skill["tags"])
    effects=[supports[x]["effects"] for x in pair]
    conv=[e["convert"] for e in effects if "convert" in e]
    triggers=[e for e in effects if "trigger" in e]
    if len(conv)>1 or len(triggers)>1: return False
    if "multi" in pair and "aim" in pair: return False
    if triggers and ("repeat" in pair or "echo" in pair or "heavy" in pair): return False
    if "bleed" in pair and conv: return False
    for sid in pair:
        ok={
            "all":True,"area":"area" in tags,"attack":skill["kind"]=="attack",
            "direct_attack":skill["kind"]=="attack" and "direct" in tags,
            "direct_spell":skill["kind"]=="spell" and "direct" in tags,
            "projectile":"projectile" in tags,
            "chainable":"chain" in tags or ("projectile" in tags and "pierce" not in tags),
            "pierce":"projectile" in tags and "pierce" in tags,
            "physical":skill["element"]=="physical",
            "physical_attack":skill["element"]=="physical" and skill["kind"]=="attack",
            "direct_physical_attack":skill["element"]=="physical" and skill["kind"]=="attack" and "direct" in tags,
            "fire":skill["element"]=="fire" or conv==["fire"],
            "persistent":"persistent" in tags,"direct":"direct" in tags
        }.get(supports[sid]["requires"],False)
        if not ok: return False
    if "on_block" in pair and weapon is not None and not weapons[weapon]["shield"]: return False
    return True

def validate_catalog(data):
    errors=[]
    for cat in ("skills","supports","builds","scenarios"):
        ids=[x["id"] for x in data[cat]]
        if len(set(ids))!=len(ids): errors.append("Duplicate IDs: "+cat)
    def finite(v,path=""):
        if type(v) in (int,float) and not math.isfinite(v): errors.append("Nonfinite: "+path)
        elif isinstance(v,dict):
            for k,x in v.items(): finite(x,path+"."+k)
        elif isinstance(v,list):
            for i,x in enumerate(v): finite(x,path+"."+str(i))
    finite(data)
    skills,supports=index(data,"skills"),index(data,"supports")
    allowed_tags={"area","direct","persistent","projectile","pierce","chain","homing","combo"}
    allowed_effects={"radius","hit","repeat","repeat_damage","cdr","projectiles","chains","return_damage","force_projectiles","range","action","crit_multi","crit_inc","noncrit","cooldown","convert","pulses","ailment","ailment_rate","trigger","life_cost","leech","moving_accuracy","near","far"}
    for support in supports.values():
        if set(support["effects"])-allowed_effects: errors.append(support["id"]+": unknown effect")
        for key in ("hit","radius","range","action","cooldown","noncrit","near","far"):
            if key in support["effects"] and support["effects"][key]<=0: errors.append(support["id"]+": invalid multiplier")
    for s in skills.values():
        if set(s["tags"])-allowed_tags: errors.append(s["id"]+": unknown tag")
        for f in ("power","cooldown","action","range"):
            if s[f]<=0: errors.append(s["id"]+": nonpositive "+f)
        if not s["weapons"] or set(s["weapons"])-set(data["weapons"]): errors.append(s["id"]+": weapons")
        if s["pulses"]<1 or s["projectiles"]<1: errors.append(s["id"]+": counts")
        if s["pulses"]>1 and s["interval"]<=0: errors.append(s["id"]+": pulse interval")
        if "direct" in s["tags"] and "persistent" in s["tags"]: errors.append(s["id"]+": delivery tags")
    for b in data["builds"]:
        if b["weapon"] not in data["weapons"]:
            errors.append(b["id"]+": weapon")
            continue
        gs=b["groups"]
        if not 1<=len(gs)<=3 or len(set(g["skill"] for g in gs))!=len(gs): errors.append(b["id"]+": active slots")
        for g in gs:
            s=skills.get(g["skill"])
            if s is None or b["weapon"] not in s["weapons"]: errors.append(b["id"]+": skill/weapon")
            elif not compatible(s,g["supports"],supports,b["weapon"],data["weapons"]): errors.append(b["id"]+": incompatible "+g["skill"])
    for sid in supports:
        if not any(compatible(s,[sid],supports) or any(compatible(s,[sid,x],supports) for x in supports if x!=sid) for s in skills.values()):
            errors.append(sid+": unreachable")
    e=data["equipment"]
    for family,pool in e["pools"].items():
        if len(set(pool))!=len(pool) or set(pool)-set(e["affixes"]): errors.append(family+": invalid pool")
    if not 0<=data["growth"]["unequipped_fraction"]<=1: errors.append("XP fraction")
    return errors

def affix_value(data,aid,tier):
    lo,hi=data["equipment"]["ranges"][data["equipment"]["affixes"][aid]["range"]][tier-1]
    return (lo+hi)//2

def make_items(data,weapon,profile="physical",star=5):
    if type(star) is not int or not 1<=star<=5: raise ValueError("Invalid star")
    attribute=data["weapons"][weapon]["attribute"]
    priorities={
      "physical":["weapon_phys_flat","weapon_phys_inc","physical_inc","life","armour","regen","attack_fire"],
      "elemental":["weapon_phys_flat","weapon_phys_inc","elemental_inc","attack_cold","life","armour"],
      "spell":["spell_inc","spell_cold","spell_fire","spell_lightning","life","armour","regen"],
      "critical":["weapon_phys_flat","weapon_phys_inc","spell_inc","physical_inc","spell_cold","life","armour"],
      "defense":["life","armour","armour_inc","regen","weapon_phys_flat","weapon_phys_inc","physical_inc"],
      "sustain":["regen","life","weapon_phys_flat","weapon_phys_inc","physical_inc","armour"]}
    suffix=[attribute,"cooldown","fire_res","cold_res","lightning_res","block","attack_speed","cast_speed","local_attack_speed","healing","crit_inc","crit_multi"]
    if profile=="critical": suffix=[attribute,"crit_inc","crit_multi","local_attack_speed","cast_speed","cooldown","fire_res","cold_res","lightning_res","block","healing"]
    if profile=="sustain": suffix=[attribute,"healing","cooldown","fire_res","block","attack_speed","local_attack_speed","cold_res","lightning_res"]
    if profile=="spell": suffix=[attribute,"cast_speed","cooldown","fire_res","cold_res","lightning_res","crit_inc","crit_multi","block"]
    order=priorities[profile]+suffix
    slots=[(weapon,"weapon"),("head","head"),("chest","chest"),("gloves","gloves"),("boots","boots"),("amulet","amulet"),("ring","ring1"),("ring","ring2"),("belt","belt")]
    if data["weapons"][weapon]["shield"]: slots.append(("offhand","offhand"))
    result=[]
    attribute_total=10+(5*star if attribute=="strength" else 0)
    for family,slot in slots:
        chosen=[]
        for group in ("prefix","suffix"):
            eligible=[a for a in data["equipment"]["pools"][family] if data["equipment"]["affixes"][a]["group"]==group]
            local_order=order
            if group=="suffix" and attribute_total>=data["simulation"]["attribute_requirement"]:
                local_order=[a for a in order if a!=attribute]
            picked=sorted(eligible,key=lambda a:(local_order.index(a) if a in local_order else 999,a))[:3]
            chosen+=picked
            if attribute in picked: attribute_total+=affix_value(data,attribute,star+1)
        tier=star+1
        result.append({"family":family,"slot":slot,"star":star,"tier":tier,"affixes":{a:affix_value(data,a,tier) for a in chosen}})
    return result

def validate_items(data,items):
    errors=[]
    for item in items:
        pool=data["equipment"]["pools"][item["family"]]
        for group in ("prefix","suffix"):
            if sum(data["equipment"]["affixes"].get(a,{}).get("group")==group for a in item["affixes"])>3: errors.append("Too many "+group)
        if len(item["affixes"])>6: errors.append("Too many affixes")
        if not 1<=item["star"]<=5 or not 1<=item["tier"]<=7 or not item["star"]<=item["tier"]<=item["star"]+2: errors.append("Illegal tier")
        for aid,value in item["affixes"].items():
            if aid not in pool: errors.append("Ineligible affix "+aid)
            else:
                lo,hi=data["equipment"]["ranges"][data["equipment"]["affixes"][aid]["range"]][item["tier"]-1]
                if type(value) is not int or not lo<=value<=hi: errors.append("Invalid value "+aid)
    return errors

def make_stats(data,weapon,profile="physical",star=5,uniques=()):
    items=make_items(data,weapon,profile,star)
    v=collections.defaultdict(float)
    active=list(uniques) if star>=4 else []
    for item in items:
        if item["slot"] not in active:
            for aid,value in item["affixes"].items(): v[aid]+=value
    crit_base=0.05+(0.03 if profile=="critical" else 0)
    if profile!="critical": v["spell_inc" if weapon=="wand" else "weapon_phys_inc"]+=15
    v["life"]+=20*star
    v["strength"]+=5*star
    v["fire_res"]+=(4+2*star)*2
    if "amulet" in active:
        v["strength"]-=5*star
        v["strength"]+=36 if star==4 else 45
        v["life"]+=60 if star==4 else 75
    rings=sum(slot in active for slot in ("ring1","ring2"))
    for _ in range(rings):
        v["life"]+=48 if star==4 else 60
        v["cooldown"]+=(12 if star==4 else 15)+40
    if "belt" in active:
        v["life"]-=20*star
        v["life"]+=140 if star==4 else 175
        v["fire_res"]+=12 if star==4 else 15
    shield=data["weapons"][weapon]["shield"]
    stats=dict(v)
    stats.update({
      "weapon":weapon,"shield_enabled":shield,
      "weapon_damage":(data["weapons"][weapon]["damage"]*star+v["weapon_phys_flat"])*(1+v["weapon_phys_inc"]/100),
      "aps":data["weapons"][weapon]["aps"]*(1+v["local_attack_speed"]/100)*(1+v["attack_speed"]/100),
      "crit_base":crit_base,"crit_chance":min(1,crit_base*(1+v["crit_inc"]/100)),
      "crit_multiplier":1.5+v["crit_multi"]/100,
      "hp_max":math.floor((1000+v["life"])*(1.3 if "belt" in active else 1)),
      "es_max":0 if "belt" in active else v["shield"]*(1+v["shield_inc"]/100),
      "armour_total":((50+100+40+40+(70 if shield else 0))*star+v["armour"])*(1+(v["armour_inc"]+(50 if shield else 40))/100),
      "evasion_total":v["evasion"]*(1+v["evasion_inc"]/100),
      "block_chance":min(0.5,0.15+v["block"]/100) if shield else 0,
      "regen_per_second":v["regen"]*(1+v["healing"]/100),
      "hit_unique_multiplier":(1.25 if "amulet" in active else 1)*0.8**rings,
      "no_crit":"amulet" in active,
      "attributes":{a:10+v[a] for a in ("strength","dexterity","intelligence")},
      "resists":{e:min(0.75,max(0,v[e+"_res"]/100)) for e in ("fire","cold","lightning")}})
    if stats["no_crit"]: stats["crit_chance"]=0
    return stats,items

def prepare(data,skill,pair,stats,level=20,support_level=20):
    supports=index(data,"supports")
    if not compatible(skill,pair,supports,stats["weapon"],data["weapons"]): raise ValueError("Incompatible group")
    if not 1<=level<=data["growth"]["max_level"] or not 1<=support_level<=data["growth"]["max_level"]: raise ValueError("Invalid level")
    s=collections.defaultdict(float,stats)
    effects=[supports[x]["effects"] for x in pair]
    if skill["kind"]=="attack":
        parts=[("physical","physical",s["weapon_damage"]*skill["power"])]+[(e,e,s["attack_"+e]*skill["power"]) for e in ("fire","cold","lightning")]
    else:
        parts=[(skill["element"],skill["element"],skill["power"])]+[(e,e,s["spell_"+e]) for e in ("fire","cold","lightning")]
    conv=next((e["convert"] for e in effects if "convert" in e),None)
    rate=data["growth"]["spell_damage_per_level"] if skill["kind"]=="spell" else data["growth"]["active_damage_per_level"]
    growth=1+rate*(level-1)
    components=collections.defaultdict(float)
    for dest,origin,base in parts:
        if conv and dest=="physical": dest=conv
        inc=len(pair)*(support_level-1)*data["growth"]["support_increase_per_level"]
        if origin=="physical" or dest=="physical": inc+=s["physical_inc"]/100
        if dest!="physical": inc+=s["elemental_inc"]/100
        if skill["kind"]=="spell": inc+=s["spell_inc"]/100
        components[dest]+=base*growth*(1+inc)
    action=skill["action"]/(s["aps"] if skill["kind"]=="attack" else 1+s["cast_speed"]/100)
    action*=math.prod(e.get("action",1) for e in effects)
    repeat=any(e.get("repeat") for e in effects)
    cdr=s["cooldown"]+sum(e.get("cdr",0) for e in effects)
    crit_inc=s["crit_inc"]+sum(e.get("crit_inc",0) for e in effects)
    return {
      "skill":skill,"pair":list(pair),"components":dict(components),
      "hit_multiplier":math.prod(e.get("hit",1) for e in effects)*s["hit_unique_multiplier"],
      "radius":skill["radius"]*math.prod(e.get("radius",1) for e in effects),
      "range":skill["range"]*math.prod(e.get("range",1) for e in effects),
      "action":action,"lock":action*(2 if repeat else 1),
      "cooldown":skill["cooldown"]*math.prod(e.get("cooldown",1) for e in effects)/(1+cdr/100),
      "projectiles":1 if any("force_projectiles" in e for e in effects) else skill["projectiles"]+sum(e.get("projectiles",0) for e in effects),
      "pulses":skill["pulses"]+sum(e.get("pulses",0) for e in effects),
      "repeat":repeat,"repeat_damage":next((e["repeat_damage"] for e in effects if "repeat_damage" in e),1),
      "return_damage":next((e["return_damage"] for e in effects if "return_damage" in e),0),
      "chains":(2 if "chain" in skill["tags"] else 0)+sum(e.get("chains",0) for e in effects),
      "crit":0 if s["no_crit"] else min(1,s["crit_base"]*(1+crit_inc/100))*s.get("crit_penalty",1),
      "crit_multiplier":s["crit_multiplier"]+sum(e.get("crit_multi",0) for e in effects),
      "noncrit":math.prod(e.get("noncrit",1) for e in effects),
      "trigger":next((e["trigger"] for e in effects if "trigger" in e),None),
      "life_cost":sum(e.get("life_cost",0) for e in effects),
      "leech":sum(e.get("leech",0) for e in effects),
      "ailment":next((e["ailment"] for e in effects if "ailment" in e),None),
      "ailment_rate":next((e["ailment_rate"] for e in effects if "ailment_rate" in e),0),
      "moving_bonus":sum(e.get("moving_accuracy",0) for e in effects),
      "near":math.prod(e.get("near",1) for e in effects),"far":math.prod(e.get("far",1) for e in effects),
      "enabled":s["attributes"][data["weapons"][s["weapon"]]["attribute"]]>=data["simulation"]["attribute_requirement"]}

def mitigation(element,scenario,dot=False):
    if element=="physical": return 1 if dot else 1-min(0.75,scenario["armour"]/(scenario["armour"]+1000))
    return 1-min(0.75,max(0,scenario["resistance"]))

def target_coverage(g,scenario):
    """Expected covered targets. Proxy geometry, not physical collision."""
    skill=g["skill"]; n=scenario["targets"]; tags=skill["tags"]
    count=1.0
    if "area" in tags: count+=(n-1)*min(1,(g["radius"]/max(1,scenario["spread"]))**2)
    if "projectile" in tags: count=max(count,g["projectiles"]*((1.7 if "pierce" in tags else 1)+g["chains"]))
    elif "chain" in tags: count=1+g["chains"]
    accuracy=min(1,scenario["moving_accuracy"]+g["moving_bonus"]+(0.2 if "homing" in tags else 0))
    if "persistent" in tags: accuracy*=scenario["field_uptime"]
    reach=min(1,g["range"]/max(0.1,scenario["distance"]))
    return max(0,min(n,min(n,count)*accuracy*reach))

def expected_hit(g,scenario):
    raw=sum(v*mitigation(e,scenario) for e,v in g["components"].items())
    crit=g["crit"]*g["crit_multiplier"]+(1-g["crit"])*g["noncrit"]
    return raw*g["hit_multiplier"]*crit*(g["near"] if scenario["distance"]<=3 else g["far"])

def analytical_score(g,scenario):
    if g["trigger"]: return None
    count=target_coverage(g,scenario); period=max(g["cooldown"],g["lock"])
    mult=g["pulses"]*(1+(g["repeat_damage"] if g["repeat"] else 0))*(1+g["return_damage"])
    score=expected_hit(g,scenario)*count*mult/period
    if g["ailment"]:
        e="physical" if g["ailment"]=="bleed" else "fire"
        score+=g["components"].get(e,0)*g["ailment_rate"]*mitigation(e,scenario,True)*scenario.get("dot_multiplier",1)*count*min(1,3/period)
    return score

def damage_taken(stats,scenario,rng,attack,element):
    if attack and rng.random()<min(0.6,stats["evasion_total"]/(stats["evasion_total"]+1000)): return 0,False
    if rng.random()<stats["block_chance"]: return 0,True
    red=min(0.75,stats["armour_total"]/(stats["armour_total"]+1000)) if element=="physical" else stats["resists"][element]
    return scenario["enemy_damage"]*(1-red),False

def simulate(data,build,scenario,seed=0,star=5,level=20,support_level=20,uniques=None,seconds=None,trace=False,stats_override=None):
    skills=index(data,"skills")
    stats,_=make_stats(data,build["weapon"],build["gear"],star,build["uniques"] if uniques is None else uniques)
    scenario=copy.deepcopy(scenario)
    penalty=scenario.get("penalty")
    if penalty=="damage": scenario["enemy_damage"]*=1.2
    if penalty=="attack_speed":
        a=scenario["enemy_attack_fraction"]
        factor=1+0.15*a
        scenario["enemy_interval"]/=factor
        scenario["enemy_attack_fraction"]=a*1.15/factor
    if penalty=="healing": stats["regen_per_second"]*=0.7
    if penalty=="dot": scenario["dot_multiplier"]=0.7
    stats["crit_penalty"]=0.7 if penalty=="crit" else 1
    stats["crit_chance"]*=stats["crit_penalty"]
    if stats_override: stats.update(copy.deepcopy(stats_override))
    groups=[prepare(data,skills[g["skill"]],g["supports"],stats,level,support_level) for g in build["groups"]]
    horizon=scenario.get("seconds",data["simulation"]["seconds"]) if seconds is None else seconds
    rng=random.Random(seed); q=[]; serial=itertools.count()
    def push(t,kind,payload=None):
        if t<horizon-EPS: heapq.heappush(q,(round(t,9),next(serial),kind,payload))
    ready=[0.0]*len(groups); generations=[0]*len(groups)
    hp=float(stats["hp_max"]); es=float(stats["es_max"])
    previous=0.0; last_damage=-1e9
    dealt=hit_damage=dot_damage=life_spent=0.0
    cursor=trigger_cursor=0; next_trigger=0.0
    casts=collections.Counter(); dots={}; events=[]; versions=itertools.count()
    leech_bins=collections.defaultdict(float)
    blocks=triggered=processed=0; death=horizon
    push(0,"action")
    if scenario["enemy_damage"]>0: push(scenario["enemy_interval"],"incoming",0)
    def start(i,t,is_trigger=False):
        nonlocal hp,life_spent
        g=groups[i]; cost=stats["hp_max"]*g["life_cost"]
        if not g["enabled"] or hp<=cost or ready[i]>t+EPS: return False
        hp-=cost; life_spent+=cost; ready[i]=t+g["cooldown"]
        casts[g["skill"]["id"]]+=1; generations[i]+=1; gen=generations[i]
        reps=[(0,1.0)]+([(g["action"],g["repeat_damage"])] if g["repeat"] else [])
        for offset,scale in reps:
            for pulse in range(g["pulses"]):
                root=not is_trigger and offset==0 and pulse==0 and "direct" in g["skill"]["tags"]
                th=t+(0.02 if is_trigger else g["action"]*0.5)+offset+pulse*g["skill"]["interval"]
                push(th,"hit",(i,scale,gen,root))
                if g["return_damage"]: push(th+0.35,"hit",(i,scale*g["return_damage"],gen,False))
        if trace: events.append([round(t,6),"trigger" if is_trigger else "cast",g["skill"]["id"]])
        return True
    def trigger(kind,t,origin=None):
        nonlocal trigger_cursor,next_trigger,triggered
        if t+EPS<next_trigger: return
        for delta in range(len(groups)):
            i=(trigger_cursor+delta)%len(groups)
            if i!=origin and groups[i]["trigger"]==kind and start(i,t,True):
                next_trigger=t+data["simulation"]["trigger_global_cooldown"]
                trigger_cursor=(i+1)%len(groups); triggered+=1
                return
    while q:
        t,_,kind,payload=heapq.heappop(q); processed+=1
        if processed>100000: raise RuntimeError("Event budget exceeded")
        dt=t-previous
        if dt<-EPS: raise AssertionError("Time reversed")
        hp=min(stats["hp_max"],hp+stats["regen_per_second"]*dt)
        es=min(stats["es_max"],es+stats["es_max"]*0.2*max(0,t-max(previous,last_damage+3)))
        previous=t
        if kind=="action":
            chosen=None
            for delta in range(len(groups)):
                i=(cursor+delta)%len(groups)
                if groups[i]["trigger"] is None and start(i,t):
                    chosen=i; break
            if chosen is not None:
                cursor=(chosen+1)%len(groups)
                push(t+max(0.02,groups[chosen]["lock"]),"action")
            else:
                basic_base=0.05+(0.03 if build["gear"]=="critical" and stats["weapon"]!="wand" else 0)
                basic_chance=0 if stats["no_crit"] else min(1,basic_base*(1+stats.get("crit_inc",0)/100))*stats.get("crit_penalty",1)
                crit=rng.random()<basic_chance
                amount=stats["weapon_damage"]*(1+stats.get("physical_inc",0)/100)*stats["hit_unique_multiplier"]
                amount*=mitigation("physical",scenario)*(stats["crit_multiplier"] if crit else 1)
                amount*=min(1,(9 if stats["weapon"] in ("bow","wand") else 3)/max(0.1,scenario["distance"]))
                dealt+=amount; hit_damage+=amount; casts["basic"]+=1
                if crit: trigger("crit",t)
                push(t+1/max(0.01,stats["aps"]),"action")
        elif kind=="hit":
            i,scale,gen,root=payload; g=groups[i]
            if "persistent" in g["skill"]["tags"] and gen!=generations[i]: continue
            coverage=target_coverage(g,scenario)
            count=int(coverage)+int(rng.random()<coverage-int(coverage))
            targets=rng.sample(range(scenario["targets"]),min(scenario["targets"],count))
            if not targets: continue
            crit=rng.random()<g["crit"]
            amount=sum(v*mitigation(e,scenario) for e,v in g["components"].items())
            amount*=g["hit_multiplier"]*(g["crit_multiplier"] if crit else g["noncrit"])*scale
            amount*=g["near"] if scenario["distance"]<=3 else g["far"]
            total=amount*len(targets); dealt+=total; hit_damage+=total
            if g["leech"]:
                second=int(t); cap=stats["hp_max"]*data["simulation"]["leech_max_life_per_second"]
                heal=min(total*g["leech"]*(1+stats.get("healing",0)/100)*(0.7 if penalty=="healing" else 1),max(0,cap-leech_bins[second]))
                hp=min(stats["hp_max"],hp+heal); leech_bins[second]+=heal
            if g["ailment"]:
                e="physical" if g["ailment"]=="bleed" else "fire"
                dps=g["components"].get(e,0)*g["ailment_rate"]*mitigation(e,scenario,True)*scenario.get("dot_multiplier",1)
                for target in targets:
                    key=(g["ailment"],target); old=dots.get(key)
                    if old and old[1]>t+EPS and old[0]>dps+EPS: continue
                    version=next(versions)
                    next_tick=old[3] if old and old[1]>t+EPS else t+data["simulation"]["dot_tick"]
                    dots[key]=(dps,t+data["simulation"]["dot_seconds"],version,next_tick)
                    push(next_tick,"dot",(key,version))
            if root and crit: trigger("crit",t,i)
        elif kind=="dot":
            key,version=payload; current=dots.get(key)
            if current and current[2]==version and t<=current[1]+EPS:
                amount=current[0]*data["simulation"]["dot_tick"]
                dealt+=amount; dot_damage+=amount
                nxt=t+data["simulation"]["dot_tick"]
                dots[key]=(current[0],current[1],current[2],nxt)
                push(nxt,"dot",(key,version))
        elif kind=="incoming":
            attack=rng.random()<scenario["enemy_attack_fraction"]
            damage,blocked=damage_taken(stats,scenario,rng,attack,"physical" if payload%2==0 else "fire")
            blocks+=int(blocked)
            if blocked: trigger("block",t)
            if damage>0:
                last_damage=t; absorbed=min(es,damage); es-=absorbed; hp-=damage-absorbed
            if hp<=0:
                death=t; hp=0; break
            push(t+scenario["enemy_interval"],"incoming",payload+1)
    if previous<horizon and hp>0: hp=min(stats["hp_max"],hp+stats["regen_per_second"]*(horizon-previous))
    return {"dps":dealt/horizon,"hit_dps":hit_damage/horizon,"dot_dps":dot_damage/horizon,"survived":hp>0,"lifetime":death,
            "hp_end_fraction":hp/stats["hp_max"],"life_spent":life_spent,"casts":dict(casts),"blocks":blocks,"triggered":triggered,"events":events,"processed":processed}

def candidate_groups(data,weapon):
    supports=index(data,"supports"); ids=list(supports)
    pairs=[()]+[(x,) for x in ids]+list(itertools.combinations(ids,2))
    for skill in data["skills"]:
        if weapon in skill["weapons"]:
            for pair in pairs:
                if compatible(skill,pair,supports,weapon,data["weapons"]): yield skill,pair

def summarize_runs(runs):
    values=[r["dps"] for r in runs]; mean=statistics.mean(values)
    se=statistics.stdev(values)/math.sqrt(len(values)) if len(values)>1 else 0
    return {"mean_dps":round(mean,4),"ci95_normal":[round(mean-1.96*se,4),round(mean+1.96*se,4)],
            "min_dps":round(min(values),4),"max_dps":round(max(values),4),"survival_rate":sum(r["survived"] for r in runs)/len(runs),
            "mean_dot_dps":round(statistics.mean(r["dot_dps"] for r in runs),4),"mean_triggers":round(statistics.mean(r["triggered"] for r in runs),4),
            "mean_life_spent":round(statistics.mean(r["life_spent"] for r in runs),4),
            "mean_hp_end":round(statistics.mean(r["hp_end_fraction"] for r in runs),4)}

def analyze(data,seeds=24):
    errors=validate_catalog(data)
    if errors: raise ValueError("; ".join(errors))
    report={"schema_version":1,"python_runtime":platform.python_version(),"status":"proposed model; not balance approval",
            "catalog_sha256":hashlib.sha256(CATALOG.read_bytes()).hexdigest(),
            "analyzer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"seeds":list(range(seeds)),
            "seconds":data["simulation"]["seconds"]}
    static={"actives":len(data["skills"]),"supports":len(data["supports"]),"example_builds":len(data["builds"]),
            "scenarios":len(data["scenarios"]),"legal_item_checks":0,"weapon_configurations":{},"three_group_layouts":{}}
    reach=set(); rankings=[]
    for weapon in data["weapons"]:
        choices=list(candidate_groups(data,weapon)); counts=collections.Counter(s["id"] for s,p in choices)
        static["weapon_configurations"][weapon]=len(choices)
        static["three_group_layouts"][weapon]=sum(math.prod(counts[s] for s in combo)*6 for combo in itertools.combinations(counts,3))
        for s,pair in choices: reach.update(pair)
        stats,items=make_stats(data,weapon)
        if validate_items(data,items): raise ValueError("Invalid fixture")
        static["legal_item_checks"]+=len(items)
        for scenario in data["scenarios"]:
            scored=[]
            for s,pair in choices:
                score=analytical_score(prepare(data,s,pair,stats),scenario)
                if score is not None: scored.append({"skill":s["id"],"supports":list(pair),"score":round(score,4)})
            scored.sort(key=lambda r:(-r["score"],r["skill"],r["supports"]))
            rankings.append({"weapon":weapon,"scenario":scenario["id"],"evaluated":len(scored),"top10":scored[:10]})
    static["reachable_supports"]=sorted(reach)
    report["static"]=static; report["single_group_rankings"]=rankings
    print("Static enumeration complete; simulating benchmarks.",flush=True)
    report["benchmarks"]=[]
    for build in data["builds"]:
        _,items=make_stats(data,build["weapon"],build["gear"])
        if validate_items(data,items): raise ValueError("Illegal comparison equipment")
        for scenario in data["scenarios"]:
            runs=[simulate(data,build,scenario,seed) for seed in range(seeds)]
            report["benchmarks"].append({"build":build["id"],"scenario":scenario["id"],**summarize_runs(runs)})
    print("Benchmarks complete; sweeping unique layouts and growth.",flush=True)
    report["unique_sweep"]=[]
    for build in data["builds"]:
        for neck,rings,belt in itertools.product((0,1),range(3),(0,1)):
            uniques=(["amulet"] if neck else [])+["ring"+str(i+1) for i in range(rings)]+(["belt"] if belt else [])
            for scenario in data["scenarios"]:
                runs=[simulate(data,build,scenario,seed,uniques=uniques) for seed in range(min(8,seeds))]
                report["unique_sweep"].append({"build":build["id"],"scenario":scenario["id"],"uniques":uniques,**summarize_runs(runs)})
    report["growth_sensitivity"]=[]
    for build in data["builds"]:
        for star,level in itertools.product((1,3,5),(1,10,20)):
            runs=[simulate(data,build,data["scenarios"][0],seed,star=star,level=level,support_level=level) for seed in range(min(8,seeds))]
            report["growth_sensitivity"].append({"build":build["id"],"star":star,"gem_level":level,**summarize_runs(runs)})
    report["penalty_sensitivity"]=[]
    for build in data["builds"]:
        for penalty in ("hp","damage","attack_speed","healing","crit","dot"):
            scenario=copy.deepcopy(data["scenarios"][3])
            scenario["penalty"]=penalty
            runs=[simulate(data,build,scenario,seed) for seed in range(min(8,seeds))]
            report["penalty_sensitivity"].append({"build":build["id"],"penalty":penalty,**summarize_runs(runs)})
    report["holdout_benchmarks"]=[]
    for build in data["builds"]:
        for scenario in data.get("holdout_scenarios",[]):
            runs=[simulate(data,build,scenario,seed+24) for seed in range(seeds)]
            report["holdout_benchmarks"].append({"build":build["id"],"scenario":scenario["id"],"seconds":scenario.get("seconds",60),**summarize_runs(runs)})
    report["growth_economy"]={"xp_to_max":data["growth"]["xp_per_next_level_factor"]*sum(range(1,data["growth"]["max_level"])),
       "equipped_five_star_clears_to_max":math.ceil(data["growth"]["xp_per_next_level_factor"]*sum(range(1,data["growth"]["max_level"]))/(5*data["growth"]["equipped_xp_per_star"])),
      "unequipped_five_star_clears_to_max":math.ceil(data["growth"]["xp_per_next_level_factor"]*sum(range(1,data["growth"]["max_level"]))/(5*data["growth"]["equipped_xp_per_star"]*data["growth"]["unequipped_fraction"])),
      "note":"Clear counts from fixed XP; elapsed hours and offline progress are not assumed."}
    report["leaders"]=[]
    for scenario in data["scenarios"]:
        ordered=sorted([r for r in report["benchmarks"] if r["scenario"]==scenario["id"]],key=lambda r:-r["mean_dps"])
        report["leaders"].append({"scenario":scenario["id"],"best":ordered[0]["build"],"best_dps":ordered[0]["mean_dps"],
          "within_20_percent":[r["build"] for r in ordered if r["mean_dps"]>=0.8*ordered[0]["mean_dps"]]})
    report["warnings"]=[
      "Target coverage is expected geometry, not Unity movement/collision, finite enemy HP, or overkill.",
      "Enemy armour/resistance/damage/density are comparison fixtures, not approved content.",
      "Gear fixtures share slots/star/tier/roll budgets; affix selection differs. No global optimal build search.",
      "Single-group rankings omit resource affordability, trigger sources and three-group scheduling; benchmarks model these separately.",
      "Normal-approximation intervals and limited seeds are descriptive, not proof of balance or tail survival.",
      "Minions, poison, chaos, penetration, passive trees, mana, offline rewards and clear time are not modeled.",
      "Leech uses one-second buckets rather than rolling-window limits.",
      "Attribute affixes are only prioritized until the requirement is met; fixtures remain heuristic rather than globally optimal.",
      "Enemy attack-speed penalties preserve expected mixed attack/spell rates; exact incoming event spacing is approximated.",
      "Enemy HP +30% does not change infinite-target DPS; no clear-time result is inferred.",
      "High-output layouts and weak archetypes are findings, not passing balance gates."]
    report["simulation_runs"]=len(report["benchmarks"])*seeds+len(report["holdout_benchmarks"])*seeds+(len(report["unique_sweep"])+len(report["growth_sensitivity"])+len(report["penalty_sensitivity"]))*min(8,seeds)
    report["holdout_seeds"]=list(range(24,24+seeds))
    return report

def write_report(data,report,outdir):
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/"results.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    names={x["id"]:x["name"] for x in data["builds"]}; scenarios={x["id"]:x["name"] for x in data["scenarios"]}
    lines=["# Skill-gem numerical analysis","","Proposed offline model; not production balance approval.","",
      "- Catalog SHA256: "+report["catalog_sha256"],"- Analyzer SHA256: "+report["analyzer_sha256"],
       "- Seeds: "+str(len(report["seeds"]))+"; window: "+str(report["seconds"])+" seconds.",
      "- Total simulations: "+str(report["simulation_runs"]),
      "- Unit tests: "+str(report["tests"]["count"])+" passed; runtime Python "+report["python_runtime"]+".","",
      "## Structural combinations","","| Weapon | Valid single groups | Ordered three-group layouts |","| --- | ---: | ---: |"]
    for w,n in report["static"]["weapon_configurations"].items():
        lines.append("| "+data["weapons"][w]["name"]+" | "+str(n)+" | "+str(report["static"]["three_group_layouts"][w])+" |")
    lines+=["","Counts describe legal syntax, not viable play styles.","","## Build benchmarks","",
      "| Build | Scenario | Mean DPS | Approx. 95% interval | Survival | DOT DPS | Triggers |",
      "| --- | --- | ---: | --- | ---: | ---: | ---: |"]
    for r in report["benchmarks"]:
        lo,hi=r["ci95_normal"]
        lines.append(f'| {names[r["build"]]} | {scenarios[r["scenario"]]} | {r["mean_dps"]:.1f} | {lo:.1f}..{hi:.1f} | {r["survival_rate"]:.0%} | {r["mean_dot_dps"]:.1f} | {r["mean_triggers"]:.1f} |')
    lines+=["","## Scenario leaders",""]
    for r in report["leaders"]: lines.append("- "+scenarios[r["scenario"]]+": "+names[r["best"]]+"; within 20%: "+", ".join(names[x] for x in r["within_20_percent"]))
    lines+=["","## Holdout benchmarks","","Seeds 24 onward; separate enemy settings.","",
      "| Build | Scenario | Mean DPS | Survival |","| --- | --- | ---: | ---: |"]
    for r in report["holdout_benchmarks"]:
        lines.append(f'| {names[r["build"]]} | {r["scenario"]} | {r["mean_dps"]:.1f} | {r["survival_rate"]:.0%} |')
    lines+=["","## Limits",""]+["- "+w for w in report["warnings"]]
    lines+=["","Full unique-layout and growth sweeps: [results.json](results.json).",
      "Reproduce: python3 Tools/analyze_skill_gems.py --write-report",""]
    (outdir/"REPORT.md").write_text("\n".join(lines),encoding="utf-8")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--static",action="store_true"); p.add_argument("--write-report",action="store_true")
    p.add_argument("--seeds",type=int,default=24); args=p.parse_args()
    if args.seeds<1: p.error("--seeds must be positive")
    data=load_catalog(); errors=validate_catalog(data)
    if errors: raise SystemExit("\n".join(errors))
    if args.static:
        print("PASS: IDs, numbers, example compatibility and support reachability."); return
    sources=[Path(__file__),ROOT/"Tools/tests/test_skill_gems.py"]
    for source in sources: ast.parse(source.read_text(encoding="utf-8"),filename=str(source))
    suite=subprocess.run([sys.executable,"-m","unittest","discover","-s",str(ROOT/"Tools/tests"),"-p","test_skill_gems.py"],capture_output=True,text=True)
    if suite.returncode:
        raise SystemExit(suite.stdout+suite.stderr)
    match=re.search(r"Ran (\d+) tests",suite.stderr)
    if match is None: raise SystemExit("Missing unittest result")
    report=analyze(data,args.seeds)
    report["tests"]={"count":int(match.group(1)),"status":"passed","source_sha256":hashlib.sha256(sources[1].read_bytes()).hexdigest(),"ast_parse":"passed"}
    if args.write_report: write_report(data,report,ROOT/"Docs/Design/Analysis/SkillGems")
    print(json.dumps({"static":report["static"],"leaders":report["leaders"]},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
