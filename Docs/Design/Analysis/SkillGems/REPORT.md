# Skill-gem numerical analysis

Proposed offline model; not production balance approval.

- Catalog SHA256: 155da6574c3a30ce86759fd500281a906afbfbd4681765f3390d712015754894
- Analyzer SHA256: a737cd052b341d7a77a8c2b888ab0aeaba2faaca7ed1aca417206033fd55bce9
- Seeds: 24; window: 60 seconds.
- Total simulations: 9048
- Unit tests: 56 passed; runtime Python 3.9.6.

## Structural combinations

| Weapon | Valid single groups | Ordered three-group layouts |
| --- | ---: | ---: |
| 한손검 | 624 | 128978568 |
| 활 | 844 | 323583888 |
| 마법봉 | 331 | 19061550 |
| 양손도끼 | 424 | 36067680 |
| 양손망치 | 424 | 36067680 |

Counts describe legal syntax, not viable play styles.

## Build benchmarks

| Build | Scenario | Mean DPS | Approx. 95% interval | Survival | DOT DPS | Triggers |
| --- | --- | ---: | --- | ---: | ---: | ---: |
| 비치명 회전 검투사 | 고정 단일 대상 | 1472.7 | 1472.7..1472.7 | 100% | 0.0 | 0.0 |
| 비치명 회전 검투사 | 밀집 다수 대상 | 5386.3 | 5365.3..5407.3 | 100% | 0.0 | 0.0 |
| 비치명 회전 검투사 | 흩어진 이동 대상 | 704.6 | 672.1..737.1 | 100% | 0.0 | 0.0 |
| 비치명 회전 검투사 | 근거리 생존 압박 | 667.3 | 651.1..683.6 | 0% | 0.0 | 0.0 |
| 치명 저격 사수 | 고정 단일 대상 | 2112.6 | 2005.9..2219.2 | 100% | 0.0 | 0.0 |
| 치명 저격 사수 | 밀집 다수 대상 | 3395.4 | 3216.7..3574.2 | 100% | 0.0 | 0.0 |
| 치명 저격 사수 | 흩어진 이동 대상 | 1799.5 | 1667.7..1931.3 | 100% | 0.0 | 0.0 |
| 치명 저격 사수 | 근거리 생존 압박 | 817.6 | 765.0..870.1 | 0% | 0.0 | 0.0 |
| 군집 연쇄 사수 | 고정 단일 대상 | 716.9 | 713.1..720.6 | 100% | 0.0 | 0.0 |
| 군집 연쇄 사수 | 밀집 다수 대상 | 5094.5 | 5063.6..5125.3 | 100% | 0.0 | 0.0 |
| 군집 연쇄 사수 | 흩어진 이동 대상 | 2207.0 | 2186.8..2227.2 | 100% | 0.0 | 0.0 |
| 군집 연쇄 사수 | 근거리 생존 압박 | 274.1 | 270.9..277.3 | 0% | 0.0 | 0.0 |
| 귀환 관통 사수 | 고정 단일 대상 | 1686.8 | 1673.6..1700.1 | 100% | 0.0 | 0.0 |
| 귀환 관통 사수 | 밀집 다수 대상 | 7039.6 | 6989.0..7090.2 | 100% | 0.0 | 0.0 |
| 귀환 관통 사수 | 흩어진 이동 대상 | 2373.7 | 2320.4..2426.9 | 100% | 0.0 | 0.0 |
| 귀환 관통 사수 | 근거리 생존 압박 | 573.5 | 557.2..589.8 | 0% | 0.0 | 0.0 |
| 냉기 전환 검투사 | 고정 단일 대상 | 1812.9 | 1798.7..1827.2 | 100% | 0.0 | 0.0 |
| 냉기 전환 검투사 | 밀집 다수 대상 | 4396.9 | 4333.8..4460.1 | 100% | 0.0 | 0.0 |
| 냉기 전환 검투사 | 흩어진 이동 대상 | 1064.6 | 1021.9..1107.2 | 100% | 0.0 | 0.0 |
| 냉기 전환 검투사 | 근거리 생존 압박 | 833.7 | 795.5..871.8 | 0% | 0.0 | 0.0 |
| 반복 시전 원소술사 | 고정 단일 대상 | 1381.7 | 1373.9..1389.5 | 100% | 0.0 | 0.0 |
| 반복 시전 원소술사 | 밀집 다수 대상 | 5668.6 | 5620.6..5716.7 | 100% | 0.0 | 0.0 |
| 반복 시전 원소술사 | 흩어진 이동 대상 | 1818.5 | 1778.8..1858.3 | 100% | 0.0 | 0.0 |
| 반복 시전 원소술사 | 근거리 생존 압박 | 1177.9 | 1151.4..1204.5 | 54% | 0.0 | 0.0 |
| 지대 유지 원소술사 | 고정 단일 대상 | 1742.8 | 1736.7..1748.8 | 100% | 0.0 | 0.0 |
| 지대 유지 원소술사 | 밀집 다수 대상 | 7826.2 | 7788.3..7864.0 | 100% | 0.0 | 0.0 |
| 지대 유지 원소술사 | 흩어진 이동 대상 | 916.8 | 896.8..936.7 | 100% | 0.0 | 0.0 |
| 지대 유지 원소술사 | 근거리 생존 압박 | 1258.1 | 1219.0..1297.1 | 50% | 0.0 | 0.0 |
| 중량 여진 파쇄자 | 고정 단일 대상 | 2215.7 | 2183.3..2248.1 | 100% | 0.0 | 0.0 |
| 중량 여진 파쇄자 | 밀집 다수 대상 | 7733.8 | 7588.0..7879.7 | 100% | 0.0 | 0.0 |
| 중량 여진 파쇄자 | 흩어진 이동 대상 | 845.1 | 790.0..900.1 | 100% | 0.0 | 0.0 |
| 중량 여진 파쇄자 | 근거리 생존 압박 | 928.7 | 899.5..957.9 | 0% | 0.0 | 0.0 |
| 출혈 파쇄자 | 고정 단일 대상 | 2391.9 | 2362.5..2421.3 | 100% | 650.8 | 0.0 |
| 출혈 파쇄자 | 밀집 다수 대상 | 12303.7 | 12164.4..12443.0 | 100% | 2810.0 | 0.0 |
| 출혈 파쇄자 | 흩어진 이동 대상 | 1356.1 | 1292.5..1419.7 | 100% | 404.4 | 0.0 |
| 출혈 파쇄자 | 근거리 생존 압박 | 855.3 | 832.5..878.1 | 0% | 279.4 | 0.0 |
| 점화 원소술사 | 고정 단일 대상 | 1446.1 | 1439.9..1452.3 | 100% | 349.8 | 0.0 |
| 점화 원소술사 | 밀집 다수 대상 | 6345.7 | 6310.1..6381.3 | 100% | 2607.8 | 0.0 |
| 점화 원소술사 | 흩어진 이동 대상 | 1487.7 | 1447.0..1528.5 | 100% | 541.1 | 0.0 |
| 점화 원소술사 | 근거리 생존 압박 | 1209.9 | 1188.9..1230.9 | 67% | 315.3 | 0.0 |
| 치명 연동 원소술사 | 고정 단일 대상 | 685.1 | 638.5..731.7 | 100% | 0.0 | 11.1 |
| 치명 연동 원소술사 | 밀집 다수 대상 | 2426.9 | 2256.1..2597.7 | 100% | 0.0 | 9.9 |
| 치명 연동 원소술사 | 흩어진 이동 대상 | 636.4 | 592.0..680.7 | 100% | 0.0 | 9.5 |
| 치명 연동 원소술사 | 근거리 생존 압박 | 321.9 | 285.2..358.7 | 0% | 0.0 | 5.6 |
| 방패 반격 검투사 | 고정 단일 대상 | 414.8 | 398.5..431.0 | 100% | 0.0 | 6.7 |
| 방패 반격 검투사 | 밀집 다수 대상 | 1421.6 | 1376.1..1467.1 | 100% | 0.0 | 11.7 |
| 방패 반격 검투사 | 흩어진 이동 대상 | 221.4 | 204.0..238.7 | 100% | 0.0 | 7.9 |
| 방패 반격 검투사 | 근거리 생존 압박 | 407.1 | 391.3..422.9 | 100% | 0.0 | 10.1 |
| 생명 소모·흡혈 검투사 | 고정 단일 대상 | 1575.2 | 1560.2..1590.1 | 100% | 0.0 | 0.0 |
| 생명 소모·흡혈 검투사 | 밀집 다수 대상 | 3867.2 | 3809.8..3924.6 | 100% | 0.0 | 0.0 |
| 생명 소모·흡혈 검투사 | 흩어진 이동 대상 | 691.9 | 652.3..731.6 | 100% | 0.0 | 0.0 |
| 생명 소모·흡혈 검투사 | 근거리 생존 압박 | 1087.2 | 1037.6..1136.8 | 4% | 0.0 | 0.0 |

## Scenario leaders

- 고정 단일 대상: 출혈 파쇄자; within 20%: 출혈 파쇄자, 중량 여진 파쇄자, 치명 저격 사수
- 밀집 다수 대상: 출혈 파쇄자; within 20%: 출혈 파쇄자
- 흩어진 이동 대상: 귀환 관통 사수; within 20%: 귀환 관통 사수, 군집 연쇄 사수
- 근거리 생존 압박: 지대 유지 원소술사; within 20%: 지대 유지 원소술사, 점화 원소술사, 반복 시전 원소술사, 생명 소모·흡혈 검투사

## Holdout benchmarks

Seeds 24 onward; separate enemy settings.

| Build | Scenario | Mean DPS | Survival |
| --- | --- | ---: | ---: |
| 비치명 회전 검투사 | holdout_armour | 571.3 | 100% |
| 비치명 회전 검투사 | holdout_resist | 1309.4 | 100% |
| 비치명 회전 검투사 | holdout_wide | 1127.9 | 100% |
| 비치명 회전 검투사 | holdout_short | 2231.7 | 100% |
| 치명 저격 사수 | holdout_armour | 1041.7 | 100% |
| 치명 저격 사수 | holdout_resist | 3129.7 | 100% |
| 치명 저격 사수 | holdout_wide | 1928.1 | 100% |
| 치명 저격 사수 | holdout_short | 1978.6 | 100% |
| 군집 연쇄 사수 | holdout_armour | 368.2 | 100% |
| 군집 연쇄 사수 | holdout_resist | 1070.5 | 100% |
| 군집 연쇄 사수 | holdout_wide | 3119.3 | 100% |
| 군집 연쇄 사수 | holdout_short | 1628.4 | 100% |
| 귀환 관통 사수 | holdout_armour | 862.7 | 100% |
| 귀환 관통 사수 | holdout_resist | 2512.8 | 100% |
| 귀환 관통 사수 | holdout_wide | 2514.3 | 100% |
| 귀환 관통 사수 | holdout_short | 2496.1 | 100% |
| 냉기 전환 검투사 | holdout_armour | 1753.3 | 100% |
| 냉기 전환 검투사 | holdout_resist | 642.2 | 100% |
| 냉기 전환 검투사 | holdout_wide | 1146.3 | 100% |
| 냉기 전환 검투사 | holdout_short | 2731.8 | 100% |
| 반복 시전 원소술사 | holdout_armour | 1640.2 | 100% |
| 반복 시전 원소술사 | holdout_resist | 649.3 | 100% |
| 반복 시전 원소술사 | holdout_wide | 2034.3 | 100% |
| 반복 시전 원소술사 | holdout_short | 2549.4 | 100% |
| 지대 유지 원소술사 | holdout_armour | 2077.4 | 100% |
| 지대 유지 원소술사 | holdout_resist | 830.3 | 100% |
| 지대 유지 원소술사 | holdout_wide | 1531.9 | 100% |
| 지대 유지 원소술사 | holdout_short | 2633.1 | 100% |
| 중량 여진 파쇄자 | holdout_armour | 987.6 | 100% |
| 중량 여진 파쇄자 | holdout_resist | 2679.0 | 100% |
| 중량 여진 파쇄자 | holdout_wide | 1513.0 | 100% |
| 중량 여진 파쇄자 | holdout_short | 2592.8 | 100% |
| 출혈 파쇄자 | holdout_armour | 1308.8 | 100% |
| 출혈 파쇄자 | holdout_resist | 2540.7 | 100% |
| 출혈 파쇄자 | holdout_wide | 2490.7 | 100% |
| 출혈 파쇄자 | holdout_short | 4496.6 | 100% |
| 점화 원소술사 | holdout_armour | 1724.1 | 100% |
| 점화 원소술사 | holdout_resist | 696.3 | 100% |
| 점화 원소술사 | holdout_wide | 1969.1 | 100% |
| 점화 원소술사 | holdout_short | 2572.2 | 100% |
| 치명 연동 원소술사 | holdout_armour | 730.8 | 100% |
| 치명 연동 원소술사 | holdout_resist | 414.1 | 100% |
| 치명 연동 원소술사 | holdout_wide | 825.9 | 100% |
| 치명 연동 원소술사 | holdout_short | 1135.1 | 100% |
| 방패 반격 검투사 | holdout_armour | 165.5 | 100% |
| 방패 반격 검투사 | holdout_resist | 382.3 | 100% |
| 방패 반격 검투사 | holdout_wide | 327.9 | 100% |
| 방패 반격 검투사 | holdout_short | 722.6 | 100% |
| 생명 소모·흡혈 검투사 | holdout_armour | 562.0 | 46% |
| 생명 소모·흡혈 검투사 | holdout_resist | 1410.7 | 100% |
| 생명 소모·흡혈 검투사 | holdout_wide | 960.6 | 100% |
| 생명 소모·흡혈 검투사 | holdout_short | 2066.5 | 100% |

## Limits

- Target coverage is expected geometry, not Unity movement/collision, finite enemy HP, or overkill.
- Enemy armour/resistance/damage/density are comparison fixtures, not approved content.
- Gear fixtures share slots/star/tier/roll budgets; affix selection differs. No global optimal build search.
- Single-group rankings omit resource affordability, trigger sources and three-group scheduling; benchmarks model these separately.
- Normal-approximation intervals and limited seeds are descriptive, not proof of balance or tail survival.
- Minions, poison, chaos, penetration, passive trees, mana, offline rewards and clear time are not modeled.
- Leech uses one-second buckets rather than rolling-window limits.
- Attribute affixes are only prioritized until the requirement is met; fixtures remain heuristic rather than globally optimal.
- Enemy attack-speed penalties preserve expected mixed attack/spell rates; exact incoming event spacing is approximated.
- Enemy HP +30% does not change infinite-target DPS; no clear-time result is inferred.
- High-output layouts and weak archetypes are findings, not passing balance gates.

Full unique-layout and growth sweeps: [results.json](results.json).
Reproduce: python3 Tools/analyze_skill_gems.py --write-report
