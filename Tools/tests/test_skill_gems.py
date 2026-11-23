"""Independent arithmetic and state-machine regressions for the proposed model."""
import copy, importlib.util, json, math, random, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location("skill_model",ROOT/"Tools/analyze_skill_gems.py")
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)

class SkillGemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=M.load_catalog()
        cls.skills=M.index(cls.data,"skills"); cls.supports=M.index(cls.data,"supports")
    def stat(self,weapon="sword",profile="physical",uniques=()):
        return M.make_stats(self.data,weapon,profile,uniques=uniques)[0]
    def group(self,sid="spin",pair=(),stats=None,level=1,support_level=1):
        return M.prepare(self.data,self.skills[sid],pair,stats or self.stat(),level,support_level)
    def scenario(self,which=0):
        s=copy.deepcopy(self.data["scenarios"][which]); s["enemy_damage"]=0
        return s
    def build(self,sid="spin",pair=(),weapon="sword"):
        return {"id":"test","weapon":weapon,"gear":"physical","uniques":[],"groups":[{"skill":sid,"supports":list(pair)}]}

    def test_catalog_valid(self):
        self.assertEqual(M.validate_catalog(self.data),[])
        self.assertEqual((len(self.skills),len(self.supports)),(24,24))
    def test_duplicate_id_rejected(self):
        d=copy.deepcopy(self.data); d["skills"].append(copy.deepcopy(d["skills"][0]))
        self.assertTrue(any("Duplicate" in x for x in M.validate_catalog(d)))
    def test_nonfinite_rejected(self):
        d=copy.deepcopy(self.data); d["skills"][0]["power"]=float("nan")
        self.assertTrue(any("Nonfinite" in x for x in M.validate_catalog(d)))
    def test_zero_cooldown_rejected(self):
        d=copy.deepcopy(self.data); d["skills"][0]["cooldown"]=0
        self.assertTrue(M.validate_catalog(d))
    def test_unknown_effect_rejected(self):
        d=copy.deepcopy(self.data); d["supports"][0]["effects"]["typo"]=1
        self.assertTrue(any("unknown effect" in x for x in M.validate_catalog(d)))
    def test_invalid_multiplier_rejected(self):
        d=copy.deepcopy(self.data); d["supports"][0]["effects"]["hit"]=-1
        self.assertTrue(any("invalid multiplier" in x for x in M.validate_catalog(d)))
    def test_unknown_tag_rejected(self):
        d=copy.deepcopy(self.data); d["skills"][0]["tags"].append("typo")
        self.assertTrue(any("unknown tag" in x for x in M.validate_catalog(d)))
    def test_wrong_weapon_rejected(self):
        d=copy.deepcopy(self.data); d["builds"][0]["weapon"]="wand"
        self.assertTrue(any("weapon" in x for x in M.validate_catalog(d)))
    def test_duplicate_active_rejected(self):
        d=copy.deepcopy(self.data); d["builds"][0]["groups"][1]=copy.deepcopy(d["builds"][0]["groups"][0])
        self.assertTrue(any("active slots" in x for x in M.validate_catalog(d)))
    def test_duplicate_support_rejected(self):
        self.assertFalse(M.compatible(self.skills["spin"],["area","area"],self.supports))
    def test_empty_support_valid(self):
        self.assertTrue(M.compatible(self.skills["spin"],[],self.supports))
    def test_multiple_conversion_rejected(self):
        self.assertFalse(M.compatible(self.skills["spin"],["to_cold","to_fire"],self.supports))
    def test_fire_conversion_enables_ignite(self):
        self.assertTrue(M.compatible(self.skills["spin"],["to_fire","ignite"],self.supports))
        self.assertFalse(M.compatible(self.skills["spin"],["ignite"],self.supports))
    def test_conversion_invalidates_bleed(self):
        self.assertFalse(M.compatible(self.skills["spin"],["to_fire","bleed"],self.supports))
    def test_pierce_chain_exclusion(self):
        self.assertFalse(M.compatible(self.skills["piercing_arrow"],["chain"],self.supports))
        self.assertTrue(M.compatible(self.skills["spread_arrow"],["chain"],self.supports))
    def test_aim_multi_exclusion(self):
        self.assertFalse(M.compatible(self.skills["snipe"],["aim","multi"],self.supports))
    def test_trigger_repeat_exclusion(self):
        self.assertFalse(M.compatible(self.skills["slam"],["repeat","on_crit"],self.supports))
        self.assertFalse(M.compatible(self.skills["flame_burst"],["echo","on_crit"],self.supports))
    def test_block_requires_shield(self):
        self.assertFalse(M.compatible(self.skills["crush"],["on_block"],self.supports,"hammer",self.data["weapons"]))
    def test_persistent_repeat_excluded(self):
        self.assertFalse(M.compatible(self.skills["blade_field"],["repeat"],self.supports))
    def test_attack_spell_echo_excluded(self):
        self.assertFalse(M.compatible(self.skills["spin"],["echo"],self.supports))
    def test_all_fixture_budgets_are_legal(self):
        for w in self.data["weapons"]:
            for star in range(1,6):
                for profile in ("physical","elemental","spell","critical","defense","sustain"):
                    items=M.make_items(self.data,w,profile,star)
                    self.assertEqual(M.validate_items(self.data,items),[])
                    self.assertTrue(all(len(x["affixes"])==6 for x in items))
    def test_affix_group_overflow_detected(self):
        items=M.make_items(self.data,"sword"); items[0]["affixes"]["attack_cold"]=19
        self.assertTrue(M.validate_items(self.data,items))
    def test_affix_illegal_value_detected(self):
        items=M.make_items(self.data,"sword"); items[0]["affixes"]["weapon_phys_flat"]=9999
        self.assertTrue(M.validate_items(self.data,items))
    def test_reference_damage_arithmetic(self):
        stats=self.stat()
        stats.update(weapon_damage=180,physical_inc=80)
        g=self.group("spin",(),stats)
        self.assertAlmostEqual(g["components"]["physical"],180*2.2*1.8)
    def test_conversion_increases_added_once(self):
        stats=self.stat(); stats.update(weapon_damage=100,physical_inc=20,elemental_inc=30)
        g=self.group("spin",["to_fire"],stats)
        self.assertEqual(g["components"].get("physical",0),0)
        self.assertAlmostEqual(g["components"]["fire"],100*2.2*1.5+stats.get("attack_fire",0)*2.2*1.3)
    def test_cooldown_increases_add(self):
        stats=self.stat(); stats["cooldown"]=40
        g=self.group("slam",["haste"],stats)
        self.assertAlmostEqual(g["cooldown"],4/1.7)
    def test_haste_does_not_change_action(self):
        self.assertAlmostEqual(self.group("slam",["haste"])["action"],self.group("slam")["action"])
    def test_heavy_does_not_change_cooldown(self):
        self.assertAlmostEqual(self.group("slam",["heavy"])["cooldown"],self.group("slam")["cooldown"])
        self.assertAlmostEqual(self.group("slam",["heavy"])["action"],1.5*self.group("slam")["action"])
    def test_no_crit_has_absolute_priority(self):
        stats=self.stat(uniques=["amulet"])
        self.assertEqual(self.group("spin",["critical"],stats)["crit"],0)
        self.assertEqual(stats["crit_chance"],0)
    def test_two_unique_rings_multiply_and_add(self):
        a=self.stat(); b=self.stat(uniques=["ring1","ring2"])
        self.assertAlmostEqual(b["hit_unique_multiplier"],0.64)
        self.assertAlmostEqual(b["cooldown"]-a.get("cooldown",0),110)
    def test_unique_belt_zeroes_es(self):
        stats=self.stat(uniques=["belt"])
        self.assertEqual(stats["es_max"],0)
        self.assertEqual(stats["hp_max"],math.floor((1000+stats["life"])*1.3))
    def test_level_growth_has_known_endpoints(self):
        a=self.group(); b=self.group(level=20)
        self.assertAlmostEqual(b["components"]["physical"]/a["components"]["physical"],1.38)
        a=self.group(pair=["area","haste"],support_level=1)
        b=self.group(pair=["area","haste"],support_level=20)
        inc=self.stat().get("physical_inc",0)/100
        self.assertAlmostEqual(b["components"]["physical"]/a["components"]["physical"],(1+inc+.38)/(1+inc))
    def test_xp_boundaries(self):
        g=self.data["growth"]
        for xp,level in [(0,1),(99,1),(100,2),(299,2),(300,3),(18999,19),(19000,20),(10**9,20)]:
            self.assertEqual(M.level_from_xp(xp,g),level)
        for xp in (-1,True,0.5):
            with self.assertRaises(ValueError): M.level_from_xp(xp,g)
    def test_xp_once_not_per_link(self):
        state={"xp":{},"settled":[]}
        out=M.settle_xp(state,"clear",5,["spin","area","area","area"],self.data)
        self.assertEqual(out["xp"]["area"],100)
        self.assertEqual(out["xp"]["spin"],100)
        self.assertEqual(out["xp"]["flame_burst"],25)
        self.assertEqual(state,{"xp":{},"settled":[]})
    def test_xp_failure_and_resume_idempotence(self):
        state={"xp":{},"settled":[]}
        self.assertEqual(M.settle_xp(state,"fail",5,["spin"],self.data,False),state)
        once=M.settle_xp(state,"ok",5,["spin"],self.data)
        restored=json.loads(json.dumps(once))
        self.assertEqual(M.settle_xp(restored,"ok",5,["spin"],self.data),once)
    def test_xp_cap_and_invalid_ids(self):
        state={"xp":{"spin":18990},"settled":[]}
        self.assertEqual(M.settle_xp(state,"ok",5,["spin"],self.data)["xp"]["spin"],19000)
        with self.assertRaises(ValueError): M.settle_xp(state,"ok",5,["missing"],self.data)
    def test_coverage_and_return_single_target_cap(self):
        stats=self.stat("bow")
        g=self.group("piercing_arrow",["multi","return"],stats)
        s=self.scenario()
        self.assertLessEqual(M.target_coverage(g,s),1)
        self.assertEqual(g["return_damage"],0.5)
    def test_seed_reproducibility(self):
        b=self.data["builds"][2]; s=self.data["scenarios"][1]
        self.assertEqual(M.simulate(self.data,b,s,17),M.simulate(self.data,b,s,17))
    def test_serial_actions_do_not_overlap(self):
        b=self.data["builds"][0]; s=self.scenario()
        stats=self.stat(uniques=b["uniques"])
        locks={g["skill"]:M.prepare(self.data,self.skills[g["skill"]],g["supports"],stats)["lock"] for g in b["groups"]}
        events=M.simulate(self.data,b,s,trace=True)["events"]
        casts=[e for e in events if e[1]=="cast"]
        for a,c in zip(casts,casts[1:]): self.assertGreaterEqual(c[0]-a[0]+1e-5,locks[a[2]])
    def test_trigger_cannot_recurse(self):
        b=self.build("slam",["on_crit"])
        out=M.simulate(self.data,b,self.scenario(),seconds=20,stats_override={"crit_inc":2000,"crit_base":1})
        self.assertGreater(out["triggered"],0)
        self.assertLessEqual(out["triggered"],41)
        self.assertLess(out["processed"],2000)
    def test_no_crit_suppresses_crit_trigger(self):
        b=self.build("slam",["on_crit"]); b["uniques"]=["amulet"]
        self.assertEqual(M.simulate(self.data,b,self.scenario())["triggered"],0)
    def test_block_trigger_needs_enemy_events(self):
        b=self.build("slam",["on_block"])
        self.assertEqual(M.simulate(self.data,b,self.scenario())["triggered"],0)
        s=copy.deepcopy(self.data["scenarios"][0])
        out=M.simulate(self.data,b,s,stats_override={"block_chance":1})
        self.assertGreater(out["triggered"],0)
    def test_life_cost_paid_once_per_activation_with_repeat(self):
        b=self.build("spin",["lifeburn","repeat"])
        out=M.simulate(self.data,b,self.scenario(),stats_override={"regen_per_second":0,"hp_max":1000})
        self.assertAlmostEqual(out["life_spent"],out["casts"].get("spin",0)*40)
        self.assertLess(out["life_spent"],1000)
        self.assertTrue(out["survived"])
    def test_fast_dot_refresh_preserves_tick(self):
        d=copy.deepcopy(self.data)
        flame=next(s for s in d["skills"] if s["id"]=="flame_burst")
        flame["cooldown"]=.05; flame["action"]=.05
        out=M.simulate(d,self.build("flame_burst",["ignite"],"wand"),self.scenario(),seconds=5)
        self.assertGreater(out["dot_dps"],0)
        stats=self.stat("wand")
        g=M.prepare(d,flame,["ignite"],stats)
        upper=g["components"]["fire"]*.6*.75
        self.assertLessEqual(out["dot_dps"],upper+1e-6)
    def test_persistent_replacement_cancels_old_pulses(self):
        d=copy.deepcopy(self.data)
        skill=next(s for s in d["skills"] if s["id"]=="blade_field")
        skill["cooldown"]=.1; skill["action"]=.2
        b=self.build("blade_field")
        out=M.simulate(d,b,self.scenario(),seconds=5,stats_override={"crit_chance":0,"crit_base":0,"aps":1})
        g=M.prepare(d,skill,[],dict(self.stat(),crit_chance=0,crit_base=0,aps=1))
        self.assertLess(out["hit_dps"],M.expected_hit(g,self.scenario())*6)
    def test_enemy_hp_mod_does_not_change_dummy_dps(self):
        b=self.data["builds"][0]; s=self.scenario()
        mod=dict(s,penalty="hp")
        self.assertEqual(M.simulate(self.data,b,s),M.simulate(self.data,b,mod))
    def test_dot_penalty_is_separate_from_hits(self):
        b=self.build("flame_burst",["ignite"],"wand"); s=self.scenario()
        a=M.simulate(self.data,b,s); c=M.simulate(self.data,b,dict(s,penalty="dot"))
        self.assertAlmostEqual(c["hit_dps"],a["hit_dps"])
        self.assertAlmostEqual(c["dot_dps"],a["dot_dps"]*.7)
    def test_all_example_outputs_finite(self):
        for b in self.data["builds"]:
            out=M.simulate(self.data,b,self.scenario(),seconds=10)
            self.assertTrue(math.isfinite(out["dps"]))
            self.assertGreaterEqual(out["dps"],0)
            self.assertLessEqual(out["hp_end_fraction"],1)

    def test_attribute_requirement_boundaries(self):
        for value,enabled in ((19,False),(20,True),(21,True)):
            stats=self.stat()
            stats["attributes"]["strength"]=value
            self.assertEqual(self.group(stats=stats)["enabled"],enabled)
    def test_trigger_does_not_bypass_heavy_action_cost(self):
        self.assertFalse(M.compatible(self.skills["slam"],["on_crit","heavy"],self.supports))
    def test_spell_growth_endpoint(self):
        stats=self.stat("wand")
        a=self.group("flame_burst",stats=stats,level=1)
        b=self.group("flame_burst",stats=stats,level=20)
        self.assertAlmostEqual(b["components"]["fire"]/a["components"]["fire"],3.28)
    def test_unique_hit_multiplier_does_not_multiply_dot_base(self):
        a=self.stat("wand")
        b=copy.deepcopy(a); b["hit_unique_multiplier"]=1.25
        ga=self.group("flame_burst",["ignite"],a)
        gb=self.group("flame_burst",["ignite"],b)
        self.assertEqual(ga["components"],gb["components"])
        self.assertAlmostEqual(gb["hit_multiplier"]/ga["hit_multiplier"],1.25)
    def test_armor_and_resistance_reference_caps(self):
        stats=self.stat()
        stats.update(armour_total=1e9,evasion_total=0,block_chance=0)
        s=self.scenario(); s["enemy_damage"]=100
        self.assertAlmostEqual(M.damage_taken(stats,s,random.Random(0),True,"physical")[0],25)
        self.assertAlmostEqual(M.mitigation("fire",dict(s,resistance=.95)),.25)
    def test_attribute_is_not_forced_on_every_endgame_item(self):
        items=M.make_items(self.data,"bow","critical")
        self.assertEqual(sum("dexterity" in x["affixes"] for x in items),1)
    def test_exact_one_second_attack_matches_hand_calculation(self):
        d=copy.deepcopy(self.data)
        skill=next(s for s in d["skills"] if s["id"]=="spin")
        skill.update(cooldown=.1,action=1)
        overrides={"weapon_damage":100,"aps":1,"crit_base":0,"crit_chance":0,"physical_inc":0,
          "attack_fire":0,"attack_cold":0,"attack_lightning":0,"hit_unique_multiplier":1}
        s=self.scenario(); s.update(armour=0,distance=1,moving_accuracy=1)
        result=M.simulate(d,self.build(),s,seconds=10,level=1,support_level=1,stats_override=overrides)
        self.assertEqual(result["casts"]["spin"],10)
        self.assertAlmostEqual(result["dps"],220)
    def test_healing_penalty_reduces_available_life(self):
        b=self.data["builds"][-1]
        s=self.scenario(2)
        a=M.simulate(self.data,b,s)
        c=M.simulate(self.data,b,dict(s,penalty="healing"))
        self.assertLessEqual(c["hp_end_fraction"],a["hp_end_fraction"]+1e-6)

if __name__=="__main__": unittest.main()
