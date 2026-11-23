# 방치형 액션 RPG의 초기 방향

**라이트한 PoE**를 지향하는 모바일 방치형 RPG다. 전투를 완전 자동으로 진행하고, 아이템 제작과 장비 득템의 재미에 무게를 둔다. 핵심은 종결 장비 제작이며, 종결 장비를 통해 경쟁하는 형태로 기획한다.

종결 장비는 빌드별로 좋은 옵션 조합을 찾고, 그 조합의 옵션 등급과 수치까지 완성하는 혼합형을 기준으로 한다.

종결 장비 경쟁은 같은 도전에서 제작한 장비·스킬 조합이 낸 자동 전투 성과를 중심으로 평가하며, 주 지표는 최고 도달 단계다. 점점 강해지는 도전을 어디까지 돌파했는지 비교한다. 각 단계에 별도의 제한 시간을 적용해 주어진 시간 안에 돌파해야 한다. 실패 후 재도전은 실패한 단계부터 시작하며, 재도전 입장 자체에는 별도 재료·재화를 소모하지 않는다. 구체적인 시간 수치와 단계 구성·기록 인정 조건·그 밖의 실패 처리·재도전 횟수·초기화·동률 처리 및 보상은 별도로 확인한다.

파밍 던전은 장비 제작 재료로 패널티를 부여하고 추가 드롭 기회를 높이는 구조다. 최초 부여·한 줄 교체·고정 강도 패널티 6종과 보상 계산을 확인했다. 해금된 파밍 대상은 무료로 횟수·대기 시간 제한 없이 도전하며, 성공 기본 보상은 희귀 장비 1회·제작재료 2회 추첨이다. 실패·직접 포기에는 해당 도전 보상을 지급하지 않고 사용한 재료는 환급하지 않는다. 접속 중단은 상태를 보관해 같은 파밍 도전을 이어한다. 현재 규칙과 승인 근거는 [파밍 던전 변화 기획서](Systems/Farming-Dungeon-Modification.md)에 모았다. 최고 도달 단계 경쟁은 모딩을 적용하지 않는 공통 도전 조건을 유지한다.

파밍은 1~5성 구간으로 나누고 해당 구간 첫 완주로 다음 구간을 해금한다. 구간과 같은 성급·선택한 부위의 장비를 얻으며, 기반과 옵션은 유효 후보에서 균등하게 추첨한다. 희귀 드롭의 옵션 개수는 4개 60%·5개 30%·6개 10%다. 현재 규칙과 정보 공개 범위는 [장비 득템·파밍 대상 기획서](Systems/Equipment-Drops-and-Farming-Targets.md)에 모았다.

주력 제작 경로는 전투에서 얻은 장비의 기반과 기존 옵션을 보고 제작할 대상을 선별해 다듬는 방식이다.

제작 잠재력은 진행 구간에 따른 5단계의 장비 등급으로 구분하고, 성급 같은 직관적인 구분을 장비에 직접 표시한다. 표시되는 등급과 실제 제작 가능 범위의 구간을 일치시켜 게임 안에서 제작 투자 대상을 파악할 수 있게 한다. 역할은 1성 성장 초반, 2성 성장 중반, 3성 성장 후반, 4성 엔드게임 진입, 5성 종결 제작으로 배분한다.

개별 추가 옵션은 낮은 1단계부터 높은 7단계로 표시한다. 성급별 허용 범위는 1성 1~3·2성 2~4·3성 3~5·4성 4~6·5성 5~7이다. 첫 희귀 옵션은 접두 19종·접미 15종, 총 34종이며 단계별 정수 1단위 범위를 제공한다. 기반 기본 성능·고정 특성 수치·계열별 후보와 피해/방어 계산은 [옵션·전투 기능 기획서](Systems/Equipment-Affixes-and-Combat-Numbers.md)에 모았다. 제작 작업별 추첨과 비용·실행/종료 처리는 [기본 제작 기획서](Systems/Equipment-Crafting.md)를 따른다.

같은 옵션의 인접 등급은 수치 범위가 일부 겹치도록 설계한다. 하위 등급의 좋은 결과가 상위 등급의 낮은 결과보다 좋은 수치를 제공할 수 있으며, 첫 34종의 겹침 범위는 옵션·전투 기능 기획서의 수치표를 따른다. 5성 희귀 장비는 드롭과 제작 모두 최상위 등급의 추가 옵션을 허용하며, 파밍 희귀 드롭의 분포는 기능 기획서를 따르며 제작과 다른 획득 경로의 분포는 별도로 정한다.

획득한 희귀 장비의 성급은 고정하며, 다음 성급의 장비를 새로 얻어 제작 대상을 교체한다. 희귀 장비의 추가 옵션은 다른 장비로 이전하지 않으며, 새 장비에 붙은 옵션부터 다듬는다. 미장착 장비는 무료 500칸에 보관하고 전투 밖에서 비교·교체·제작·분해한다. 희귀 분해와 고유 단건 분해마다 기존 5종 제작재료 중 1개를 추첨하며 과거 제작 재료를 추가 환급하지 않는다. 보호·교체·보상과 파밍 공간은 [장비 관리 기획서](Systems/Equipment-Inventory-Comparison-and-Salvage.md)를 따른다.

기본 제작 장비의 추가 옵션은 접두 최대 3개와 접미 최대 3개, 합계 최대 6개를 기준으로 한다. 희귀 장비의 전투 드롭에는 추가 옵션이 일부만 붙은 장비와 6개가 모두 찬 장비를 함께 제공한다.

장비는 주무기·보조 장비·방어구·장신구를 합해 10칸으로 구성하고 첫 무기는 한손검·양손도끼·마법봉이다. 기반마다 고정 특성 1개를 추가 옵션 6칸과 별도로 제공한다. 같은 기반·성급에서 특성 수치는 고정이며 기본 제작으로 바꾸지 않는다. 모든 기반 역할을 1~5성에 제공하고 같은 계열끼리 추가 옵션 후보를 공유한다. 실제 장착 관계와 기반 역할은 [장비 편성·기반 구조 기획서](Systems/Equipment-Catalog-and-Base-Structure.md)에 모았다.

추가 옵션 제작은 희귀 장비를 중심으로 한다. 기본 제작 작업은 옵션 한 개씩 추가·제거·교체하는 세 종류를 각각 제공한다. 기본 세 작업에는 별도의 성공·실패 판정을 두지 않는다. 고유 장비는 정해진 특수 효과를 제공하며 추가 옵션 제작에서는 제외한다. 고유는 부위 관계가 맞으면 여러 개를 함께 착용하고 총수 1개 제한을 두지 않는다. 첫 목록은 목걸이·반지·허리띠 각 1종을 4/5성으로 제공하며 같은 고유·성급의 성능은 고정이다. 해당 4/5성 목표 부위의 장비 추첨마다 희귀 97%·고유 3%를 적용하고 기존 보상 최대량은 유지한다. 고유는 단건 분해만 허용한다. 공통 규칙은 [고유 장비 기획서](Systems/Unique-Equipment-Role-Acquisition-and-Handling.md)를 따르며 첫 고유 3종의 효과·고정 수치와 동일 고유 복수 착용·중첩을 확인했다. 속행의 반지 두 개를 함께 쓸 수 있고 일반 수치/재사용 회복 증가는 합산하며 개별 감폭은 곱한다. 치명타·보호막 무효와 장착 변경의 무회복은 고유 기획서를 따른다.

조율석 1개로 현재 붙어 있는 모든 추가 옵션의 종류·단계를 유지하고 각 정수값을 독립 균등 재추첨한다. 새 값은 같거나 나빠져도 바로 적용하며 기존 값으로 되돌리거나 환급하지 않는다.

추가·제거·교체·수치 재추첨은 각각 부여석·제거석·교체석·조율석을 1개 소모한다. 추가·제거·교체에서 범위를 좁히는 접두/접미 지정에는 집중석 1개를 추가 사용하며, 유효 그룹이 하나뿐이면 집중석을 소모하지 않는다. 전투 밖에서 장착 중 장비도 제작하고 무효 동작은 차감하지 않는다. 같은 결과·나빠진 결과도 확정 적용하며 취소/중단과 복원은 [기본 제작 기획서](Systems/Equipment-Crafting.md)를 따른다.

제작 결과는 기본적으로 무작위이며, 재료나 작업으로 추첨 범위를 제한적으로 좁히는 통제 수단을 제공한다. 통제는 접두·접미 중 대상 그룹을 고르는 방식이며, 선택한 그룹 안의 개별 결과는 무작위다. 그룹 지정에는 기본 제작 비용 외에 추가 재료를 사용하고, 추가 통제 재료 없이 진행하는 제작도 제공한다. 추가·제거·교체 모두 이 통제를 허용하며, 통제한 교체의 제거와 추가는 같은 그룹 안에서 진행한다.

통제 재료 없이 교체할 때도 제거한 옵션의 그룹을 유지한다. 접두를 제거하면 새 접두, 접미를 제거하면 새 접미를 추첨해 교체 전후의 그룹별 옵션 개수는 유지한다. 제거할 기존 옵션과 새로 붙을 개별 옵션은 무작위다.

같은 종류의 추가 옵션은 한 희귀 장비에 1개만 허용한다. 등급·수치가 달라도 동일 종류로 보며, 드롭과 제작에 공통으로 적용한다. 접두 최대 3개·접미 최대 3개의 상한은 유지한다.

교체에서 방금 제거한 옵션 종류도 새 추첨 후보에 포함한다. 통제 여부에 관계없이 재등장을 허용하며, 같은 접두·접미 그룹과 동일 종류의 동시 중복 제한을 따른다. 옵션 종류가 그대로일 수 있다. 교체할 새 옵션의 성능 등급은 장비 성급의 허용 범위에서 다시 추첨하며, 기존보다 높거나 낮아질 수 있다. 통제 여부와 같은 종류의 재등장 여부에 관계없이 적용한다. 새 옵션의 성급별 허용 3단계는 각각 1/3, 단계 내 정수값은 균등 추첨한다.

희귀 장비의 추가·제거·교체·수치 재추첨에는 장비당 제작 횟수 제한을 두지 않는다. 각 작업의 실행 조건을 만족하고 필요한 비용을 지불하면 같은 장비를 계속 다듬을 수 있다. 기본 비용은 성급·반복 횟수에 관계없이 같으며 별도 골드·대기 시간·할증을 두지 않는다. 작업별 실행 조건과 기존 파밍 공급은 확정 기능 기획서를 따른다.

첫 제작 검증은 기본 4종과 집중석까지로 구성한다. 개별 옵션 잠금·영구 고정·확정 부여·추가 위험 강화와 별도 완성 비용/보너스는 도입하지 않으며, 분해 보호는 제작으로 옵션이 바뀌는 것을 막지 않는다. 기존 수치·자리 상한과 반복 제작 가능 상태를 유지하고 후속 특수 제작의 필요성은 목표 빌드와 파밍 시간을 정한 뒤 다시 검토한다. 승인 범위는 [DEC-0102](Decisions/DEC-0102-initial-crafting-scope-without-extra-special-crafting.md)와 [기본 제작 기획서](Systems/Equipment-Crafting.md)를 따른다.

제작에서 가능한 옵션 후보·허용 옵션 등급·수치 범위와 옵션 종류별·등급별 추첨 확률을 게임 안에서 공개한다. 현재 장비와 선택한 작업·통제 조건에 적용되는 정보를 기준으로 하며, 확률은 기본 제작 기획서의 작업별 조건을 따르며 실제 화면 구성은 후속 확인한다.

장비·스킬의 작동 구조는 PoE 1, 아이템 제작은 PoE 2를 기준으로 삼는다. PoEDB 계열 데이터와 제작자·커뮤니티 기록을 조사하고 세부 사양은 사용자 확인 뒤 정한다.

정식 젬은 [목록 제공·개별 경험치 성장 2안](Systems/Skill-Gem-Links-Growth-and-Acquisition.md)으로 방향을 확인했다. 사용자 요청으로 [스킬·젬 전체 초안](Proposals/Skill-Gems-and-Build-Diversity.md)과 [정적·수치 검증](Analysis/SkillGems/SUMMARY.md)을 작성했으며, 24/24종·성장량·새 발동/피해 규칙은 검토용이다. 이 요청을 새 수치나 Unity 구현의 승인으로 확대하지 않는다.

## 사용자 확인을 마친 사항

| 항목 | 확인된 내용 | 근거 |
| --- | --- | --- |
| 장르와 중심 요소 | 장비·스킬 조합이 핵심인 방치형 액션 RPG | [DEC-0001](Decisions/DEC-0001-genre.md) |
| 목표 방향성 | 라이트한 PoE | [DEC-0006](Decisions/DEC-0006-light-poe-vision.md) |
| 핵심 재미 | 제작과 득템 중심이며 종결 장비 제작이 핵심 | [DEC-0007](Decisions/DEC-0007-endgame-crafting.md) |
| 종결 장비의 기준 | 빌드별 좋은 옵션 조합과 그 조합의 등급·수치 완성을 함께 추구 | [DEC-0010](Decisions/DEC-0010-endgame-definition.md) |
| 주력 제작 경로 | 전투 드롭 장비의 기반과 기존 옵션을 보고 제작 대상을 선별해 다듬음 | [DEC-0020](Decisions/DEC-0020-drop-equipment-crafting-start.md) |
| 제작 잠재력의 구분 | 진행 구간별 소수의 장비 등급을 장비에 직접 표시하며 실제 제작 구간과 일치 | [DEC-0024](Decisions/DEC-0024-visible-progression-equipment-grades.md) |
| 장비 등급의 단계 수 | 5단계로 구성 | [DEC-0025](Decisions/DEC-0025-five-equipment-grades.md) |
| 장비 등급의 역할 | 1~3성 성장 초반·중반·후반, 4성 엔드게임 진입, 5성 종결 제작 | [DEC-0026](Decisions/DEC-0026-growth-focused-equipment-grade-roles.md) |
| 성급별 허용 옵션 등급 | 성급이 높아질수록 하한과 상한을 함께 높이고 낮은 등급 일부를 제외 | [DEC-0027](Decisions/DEC-0027-rising-affix-tier-floor-and-ceiling.md) |
| 희귀 장비의 성급 변경 | 획득 시 성급 고정, 다음 성급의 장비를 새로 얻어 교체 | [DEC-0028](Decisions/DEC-0028-fixed-rare-equipment-star-grade.md) |
| 희귀 장비의 추가 옵션 이전 | 장비 간 이전 없음, 새 장비에 붙은 옵션부터 다듬음 | [DEC-0029](Decisions/DEC-0029-no-affix-transfer-between-rare-equipment.md) |
| 5성 최상위 추가 옵션의 획득 경로 | 드롭과 제작 모두 허용 | [DEC-0030](Decisions/DEC-0030-top-tier-affixes-from-drops-and-crafting.md) |
| 개별 옵션의 성능 등급 | 장비 성급과 별개로 7단계 구성 | [DEC-0031](Decisions/DEC-0031-seven-affix-performance-tiers.md) |
| 성급별 허용 범위 | 비교용 순서로 1성 1~3, 2성 2~4, 3성 3~5, 4성 4~6, 5성 5~7 | [DEC-0032](Decisions/DEC-0032-three-affix-tiers-per-equipment-grade.md) |
| 같은 옵션 등급 안의 수치 | 최솟값~최댓값 범위의 여러 수치에서 추첨 | [DEC-0033](Decisions/DEC-0033-random-values-within-affix-tier-ranges.md) |
| 같은 옵션의 인접 등급 간 수치 | 범위를 일부 겹치게 설계, 하위 등급의 좋은 결과를 활용할 여지 제공 | [DEC-0034](Decisions/DEC-0034-overlapping-value-ranges-between-adjacent-affix-tiers.md) |
| 희귀 장비의 전투 드롭 | 추가 옵션이 일부만 붙은 장비와 6개가 모두 찬 장비를 함께 제공 | [DEC-0021](Decisions/DEC-0021-partial-and-full-affix-drops.md) |
| 추가 옵션 칸 | 접두 최대 3개와 접미 최대 3개 | [DEC-0011](Decisions/DEC-0011-affix-slots.md) |
| 기반 고정 특성 | 기반 종류마다 정해진 특성을 추가 옵션 6칸과 별도로 제공 | [DEC-0022](Decisions/DEC-0022-base-fixed-traits.md) |
| 추가 옵션 후보의 공유 | 같은 장비 계열의 기반들은 추가 옵션 종류의 후보를 공유 | [DEC-0023](Decisions/DEC-0023-shared-affix-pool-by-equipment-family.md) |
| 제작 대상과 고유 장비 | 희귀 장비의 추가 옵션 제작 중심, 고유 장비는 특수 효과 역할이며 추가 옵션 제작에서 제외 | [DEC-0012](Decisions/DEC-0012-crafting-equipment-scope.md) |
| 제작의 무작위 통제 | 기본은 무작위이며 재료나 작업으로 추첨 범위를 제한적으로 좁힘 | [DEC-0013](Decisions/DEC-0013-crafting-randomness-control.md) |
| 통제의 기본 단위 | 접두·접미 중 대상 그룹을 선택하며 그룹 안의 개별 결과는 무작위 | [DEC-0014](Decisions/DEC-0014-prefix-suffix-control.md) |
| 기본 제작 작업 | 옵션 한 개씩 추가·제거·교체하는 세 작업을 각각 제공 | [DEC-0015](Decisions/DEC-0015-basic-crafting-operations.md) |
| 별도 수치 재추첨 작업 | 추가 옵션 종류·등급을 유지하고 해당 등급 범위에서 수치 재추첨, 수치가 나빠질 수도 있음 | [DEC-0035](Decisions/DEC-0035-reroll-affix-values-keeping-types-and-tiers.md) |
| 수치 재추첨의 대상 범위 | 현재 붙어 있는 모든 추가 옵션의 수치를 함께 재추첨 | [DEC-0036](Decisions/DEC-0036-reroll-values-of-all-existing-affixes.md) |
| 수치 재추첨 결과 적용 | 새 결과를 바로 적용하며 나빠진 수치도 기존 값을 대체 | [DEC-0037](Decisions/DEC-0037-apply-new-rerolled-values-directly.md) |
| 기본 제작 재료의 구분 | 추가·제거·교체·수치 재추첨에 각각 전용 기본 재료를 배정해 4종으로 구성 | [DEC-0038](Decisions/DEC-0038-dedicated-basic-materials-for-each-crafting-operation.md) |
| 통제를 적용할 작업 | 세 작업 모두 허용하며 통제한 교체는 제거·추가 모두 같은 그룹 안에서 진행 | [DEC-0016](Decisions/DEC-0016-control-all-basic-operations.md) |
| 기본 작업의 실행 | 실행 조건을 만족하면 작업을 실행하며 별도의 성공·실패 판정 없음 | [DEC-0018](Decisions/DEC-0018-basic-crafting-no-failure-roll.md) |
| 그룹 지정의 비용 구조 | 기본 비용 외에 추가 통제 재료를 사용하며, 추가 통제 재료 없이 진행하는 제작도 제공 | [DEC-0019](Decisions/DEC-0019-extra-material-for-affix-control.md) |
| 통제 재료의 공유 범위 | 공통 통제 재료 1종을 추가·제거·교체가 공유하며 접두 또는 접미를 선택 | [DEC-0039](Decisions/DEC-0039-shared-material-for-prefix-suffix-control.md) |
| 통제 없는 교체의 그룹 관계 | 제거한 옵션과 같은 그룹에서 새 옵션을 추첨해 접두·접미 개수 유지 | [DEC-0040](Decisions/DEC-0040-keep-affix-group-in-uncontrolled-replacement.md) |
| 동일 추가 옵션 종류의 중복 | 드롭·제작 공통으로 희귀 장비당 같은 종류는 1개, 등급·수치 차이로 중복 허용하지 않음 | [DEC-0041](Decisions/DEC-0041-one-affix-of-each-kind-per-rare-equipment.md) |
| 교체에서 제거한 종류의 재등장 | 통제 여부에 관계없이 방금 제거한 종류도 새 추첨 후보에 포함 | [DEC-0046](Decisions/DEC-0046-allow-removed-affix-kind-to-reappear-in-replacement.md) |
| 교체할 새 옵션의 성능 등급 | 장비 성급의 허용 범위에서 다시 추첨하며 기존보다 높거나 낮아질 수 있음 | [DEC-0047](Decisions/DEC-0047-reroll-replacement-affix-tier-within-equipment-grade.md) |
| 장비당 제작 횟수 | 희귀 장비의 추가·제거·교체·수치 재추첨에 횟수 제한 없음, 실행 조건과 비용은 유지 | [DEC-0048](Decisions/DEC-0048-no-per-equipment-crafting-attempt-limit.md) |
| 제작 정보 공개 | 게임 안에서 옵션 후보·등급·수치 범위와 옵션 종류별·등급별 확률 공개 | [DEC-0051](Decisions/DEC-0051-disclose-crafting-candidates-ranges-and-probabilities.md) |
| 전투 조작 | 완전 자동 전투이며 전투 사이에 장비·스킬·도전 대상을 선택 | [DEC-0002](Decisions/DEC-0002-combat-control.md) |
| 주력 플랫폼 | 모바일 우선 | [DEC-0003](Decisions/DEC-0003-platform.md) |
| 장비와 스킬의 기준 | PoE 1의 방식 | [DEC-0005](Decisions/DEC-0005-poe1-reference.md) |
| 정식 젬 성장 방향 | 목록 제공·캐릭터 3×2·액티브별 경험치, 젬/빌드 다양성 확대. 전체 초안과 정적·수치 검증 작성 | [DEC-0106](Decisions/DEC-0106-individual-gem-growth-and-full-design-validation.md) |
| 아이템 제작의 기준 | PoE 2 | [DEC-0009](Decisions/DEC-0009-poe2-crafting-reference.md) |
| 경쟁 방향 | 종결 장비를 통해 경쟁 | [DEC-0008](Decisions/DEC-0008-endgame-gear-competition.md) |
| 경쟁의 중심 평가 기준 | 같은 도전에서 제작한 장비·스킬 조합이 낸 자동 전투 성과 | [DEC-0053](Decisions/DEC-0053-endgame-competition-centered-on-auto-combat-results.md) |
| 경쟁의 주 평가 지표 | 점점 강해지는 도전을 어디까지 돌파했는지 나타내는 최고 도달 단계 | [DEC-0054](Decisions/DEC-0054-highest-stage-as-primary-competition-metric.md) |
| 단계 도전의 시간 제한 | 각 단계에 별도의 제한 시간 적용, 구체적인 시간 수치는 미정 | [DEC-0057](Decisions/DEC-0057-separate-time-limit-for-each-competition-stage.md) |
| 실패 후 재도전의 시작 지점 | 실패한 단계부터 재도전, 횟수·초기화·보상은 별도 확인 | [DEC-0058](Decisions/DEC-0058-retry-competition-from-the-failed-stage.md) |
| 재도전 입장 비용 | 재도전 입장 자체에는 별도 재료·재화 소모 없음 | [DEC-0059](Decisions/DEC-0059-no-separate-entry-cost-for-competition-retries.md) |
| 던전 변화의 도입 방향 | 재화를 소모해 던전에 패널티를 추가하고 보상을 높임, 세부 규칙은 별도 확인 | [DEC-0060](Decisions/DEC-0060-currency-funded-dungeon-penalties-and-better-rewards.md) |
| 던전 변화의 적용 범위 | 파밍에만 적용하고 최고 도달 단계 경쟁은 공통 도전 조건 유지 | [DEC-0061](Decisions/DEC-0061-dungeon-modification-for-farming-only.md) |
| 파밍 던전의 패널티 부여 방식 | 플레이어가 고르지 않고 무작위로 부여, 초기 6종과 개수별 확률은 후속 결정에서 확인 | [DEC-0062](Decisions/DEC-0062-randomly-assign-farming-dungeon-penalties.md) |
| 패널티 재추첨의 범위 | 바꿀 패널티 하나를 지정해 무작위 교체하고 나머지 보존 | [DEC-0064](Decisions/DEC-0064-reroll-one-selected-dungeon-penalty.md) |
| 패널티 잠금 조작 | 각 줄 우측에 잠금 체크박스 토글 배치, 체크한 줄 보존 | [DEC-0065](Decisions/DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md) |
| 잠금 해제와 교체 대상의 연동 | 최대 한 줄만 잠금 해제, 다른 줄을 해제하면 기존 줄 자동 잠금 | [DEC-0066](Decisions/DEC-0066-allow-only-one-unlocked-dungeon-penalty-row.md) |
| 패널티 교체 결과의 적용 | 새 결과가 빌드에 더 불리해져도 기존 결과를 대체해 즉시 적용 | [DEC-0067](Decisions/DEC-0067-apply-new-dungeon-penalty-result-directly.md) |
| 패널티 교체의 재화 소모 | 교체 실행마다 재화를 소모, 실제 소모량은 별도 확인 | [DEC-0068](Decisions/DEC-0068-consume-currency-for-each-dungeon-penalty-replacement.md) |
| 패널티 교체의 재료 | 장비 옵션 교체의 기본 재료와 공유, 두 작업의 소모량·실행 규칙은 별도 확인 | [DEC-0070](Decisions/DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md) |
| 패널티 반복 교체의 비용 | 같은 조건에서는 반복 횟수가 늘어도 한 번의 소모량 유지, 실제 소모량은 별도 확인 | [DEC-0071](Decisions/DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md) |
| 패널티 교체 횟수 | 별도 횟수 제한 없음, 매번 필요한 재료와 실행 조건 충족 | [DEC-0073](Decisions/DEC-0073-no-attempt-limit-for-dungeon-penalty-replacement.md) |
| 파밍 성공 후 설정 | 성공적으로 클리어하면 패널티와 연결된 보상 강화 설정 초기화 | [DEC-0074](Decisions/DEC-0074-reset-farming-dungeon-modifiers-after-successful-clear.md) |
| 파밍 실패 후 설정 | 실패해도 패널티와 연결된 보상 강화 설정 초기화 | [DEC-0075](Decisions/DEC-0075-reset-farming-dungeon-modifiers-after-failure.md) |
| 파밍 실패 시 교체 재료 | 해당 실패 도전의 패널티 교체에 이미 쓴 재료는 환급하지 않음 | [DEC-0076](Decisions/DEC-0076-no-refund-of-dungeon-penalty-replacement-materials-after-failure.md) |
| 파밍 실패 후 재도전 | 같은 대상에 새 도전 허용, 재도전 입장 자체는 무료, 재설정 비용·횟수·조건은 별도 확인 | [DEC-0077](Decisions/DEC-0077-allow-farming-retries-without-separate-entry-cost.md) |
| 최초 패널티 부여 단위 | 기본 패널티들을 한 번의 작업으로 무작위 부여, 같은 준비에서는 최초 부여 1회와 이후 한 줄 교체만 제공 | [DEC-0078](Decisions/DEC-0078-initial-farming-dungeon-penalties-generated-as-one-random-batch.md) |
| 최초 패널티 개수 | 효과 부여에 사용하는 재화에 따라 무작위 결정, 개수별 확률은 후속 DEC-0089에서 확인 | [DEC-0082](Decisions/DEC-0082-currency-dependent-random-count-for-initial-dungeon-penalties.md) |
| 최초 부여 재화 종류 수 | 2종으로 시작, 재료 이름은 별도 확인 | [DEC-0083](Decisions/DEC-0083-two-currency-types-for-initial-dungeon-penalty-generation.md) |
| 최초 부여 재료의 공유 | 장비 제작 기본 재료 4종 중 2종을 골라 공유 | [DEC-0085](Decisions/DEC-0085-share-two-equipment-crafting-materials-with-initial-dungeon-penalty-generation.md) |
| 최초 부여에 공유할 재료 | 옵션 추가·교체의 기본 재료 2종을 최초 부여에 공유 | [DEC-0086](Decisions/DEC-0086-use-affix-addition-and-replacement-materials-for-initial-dungeon-penalties.md) |
| 최초 부여의 재료별 개수 범위 | 옵션 추가 재료는 1~2개, 옵션 교체 재료는 3~4개 무작위 부여 | [DEC-0088](Decisions/DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md) |
| 최초 부여 개수별 확률 | 추가 재료의 1개·2개는 각각 50%, 교체 재료의 3개·4개도 각각 50% | [DEC-0089](Decisions/DEC-0089-initial-dungeon-penalty-generation-rules.md) |
| 던전 준비·변경 기본 동작 | 무패널티 입장 허용, 최초 부여·교체 재료 각 1개, 최초 부여 뒤 한 줄 교체만 제공, 기본 전부 잠금·교체 뒤 해제 유지·실행 불가 시 차감 없음, 전투 전 준비 중에만 변경 | [DEC-0090](Decisions/DEC-0090-farming-dungeon-preparation-and-modification-rules.md) |
| 패널티·보상 콘텐츠 | 고정 강도 6종·균등 추첨·동일 종류 중복 없음·교체 때 재등장 허용, 줄당 추가 드롭 확률 20%p와 성공 정산, 효과·보상 확률 표시 | [DEC-0092](Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md) |
| 파밍 수급·정산 | 해금 대상 무료·무제한 입장, 성공 기본 희귀 1회·재료 2회 추첨, 공급 비율 30·15·35·15·5%, 사용 재료 환급 없음, 실패·포기 보상 없음, 접속 중단 보관·복귀와 1회 정산 | [DEC-0094](Decisions/DEC-0094-farming-dungeon-supply-settlement-and-resume.md) |
| 장비 득템·파밍 대상 | 1~5성 첫 완주 해금·같은 성급과 선택 부위 드롭, 기반 균등·옵션 4/5/6개 60/30/10%와 유효 후보 균등 추첨·게임 내 정보 공개 | [DEC-0095](Decisions/DEC-0095-equipment-drops-and-farming-targets.md) |
| 장비 편성·기반 구조 | 10칸·한손검/양손도끼/마법봉과 방패 장착 관계, 기반별 역할·특성 1개와 수치 고정/기본 제작 변경 불가, 성급별 기반 유지·같은 계열 후보 공유 | [DEC-0096](Decisions/DEC-0096-equipment-catalog-and-base-structure.md) |
| 옵션·전투 계산과 초기 수치표 | 기반 성능·특성 수치·희귀 옵션 34종과 계열별 후보·7단계 정수 범위, 공격/주문·합산/곱셈·치명타·속도·능력치·방어·회복 | [DEC-0097](Decisions/DEC-0097-equipment-affixes-base-stats-and-combat-numbers.md) |
| 기본 제작 실행·비용·확률·종료 | 4종 작업 기본석 1개·그룹 지정 집중석 1개, 작업별 균등 추첨·조율 독립성·유효/무효·취소/중단·장착 중 제작과 젬 조건 | [DEC-0098](Decisions/DEC-0098-crafting-execution-costs-odds-and-recovery.md) |
| 장비 보관·비교·교체·분해 | 무료 500칸·가상 교체 비교·전투 밖 무료 장착·반지/양손 처리·분해 보호·재료 1회 추첨과 환급 없음·파밍 공간·취소/복원 | [DEC-0100](Decisions/DEC-0100-equipment-inventory-comparison-and-salvage.md) |
| 첫 제작 검증 범위 | 기본 4종+집중석·추가 보호/위험 제작 후속 검토·상한/반복 제작 유지·완성 비용/보너스 없음·분해 보호 경계 | [DEC-0102](Decisions/DEC-0102-initial-crafting-scope-without-extra-special-crafting.md) |
| 고유 공통 규칙·복수 착용 | 첫 3종·4/5성·고정 일반 2+특수 1·부위별 복수 착용·장비당 97/3%·단건 분해와 보상 보존 | [DEC-0104](Decisions/DEC-0104-unique-equipment-with-multiple-equipped-items.md) |
| 첫 고유 효과·중복·빌드 검증 목표 | 안정의 목걸이·속행의 반지·불굴의 허리띠 4/5성 고정값·반지 두 개/혼합·증가 합산/감폭 곱셈·치명타/보호막 무효·장착 무회복 | [DEC-0105](Decisions/DEC-0105-first-unique-effects-stacking-and-build-goals.md) |

## 사용자 확인이 필요한 범위

후속 제작 모델에서의 특성 변경 수단, 추가 장비 계열·기반의 도입 여부, 5단계 장비 등급의 최종 명칭·구간별 실제 전투 구성과 개별 옵션의 등급 적용 범위·예외, 파밍 희귀 드롭 이외 경로의 분포·제한, 제작재료 교환과 파밍·분해 이외 공급, 공개 정보의 실제 화면 표현과 후속 적용 범위, 첫 검증 범위 이후 추가 통제·보호·특수 제작과 다른 재료를 도입할지, 완제품 드롭과 제작의 관계, 경쟁의 단계 구성·기록 인정 조건·제한 시간 수치·시간 초과와 그 밖의 실패 처리·재도전 횟수·초기화·동률 처리·공식·보상과 시즌 규칙은 미정이다. 추가 장비·옵션 데이터의 도입과 구간별 전투 구성, 다른 보상 경로, 자동 반복 입장과 계정의 오프라인 보상은 미정이다. 장비 제작의 환급·종료·재접속은 기본 제작 기획서를 따르며 장비 보관·비교·교체·분해와 투자 회수는 장비 관리 기획서를 따른다. 자동 분해·프리셋·고유 일괄 분해의 추가 여부·젬 보관·보관 확장은 후속 확인 사항이다. 첫 고유 3종의 개별 효과·고정 수치와 동일 고유 복수 착용·중첩/충돌은 고유 기획서를 따르며 추가 고유·후속 효과는 별도로 확인한다. 현재 고유는 기본 4종 제작·집중석·성급 승급·옵션 이전을 제공하지 않고 후속 강화 확장은 다시 확인한다. 라이트함을 어느 지점에서 만들지는 [제작 중심 적용 제안](Proposals/Crafting-Endgame.md)에서 논의한다.

캐릭터 구성, 스킬과 보조의 연결, 화면 방향과 시점, 세계관과 아트, 오프라인 보상, 과금, 첫 프로토타입의 범위 역시 확인이 필요하다. 자세한 순서는 [기획 순서](01-Decision-Queue.md)에 둔다.

원본 게임의 특정 패치 전체나 수치를 일괄 채택하지 않는다. 종결 장비 경쟁이라는 방향만으로 직접 PvP, 거래소와 장비 점수를 확정하지 않는다.
