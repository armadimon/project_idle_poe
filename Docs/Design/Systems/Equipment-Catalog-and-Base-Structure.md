# 장비 편성·기반 구조 기획

상태: [DEC-0096](../Decisions/DEC-0096-equipment-catalog-and-base-structure.md)에서 확인받은 첫 장비 구성. 장비 성급·파밍과 옵션 생성은 [장비 득템·파밍 대상](Equipment-Drops-and-Farming-Targets.md)을 함께 따른다.

## 장비 칸과 장착 관계

| 장비 칸 | 칸 수 | 첫 목록·관계 |
| --- | --- | --- |
| 주무기 | 1 | 한손검·양손도끼·마법봉 |
| 보조 장비 | 1 | 방패. 한손검·마법봉과 함께 장착 가능, 양손도끼와 동시 장착 불가 |
| 머리·갑옷·장갑·장화 | 각 1 | 부위마다 방어도형·회피형·보호막형 |
| 허리띠 | 1 | 생명력형·방어도형·보호막형 |
| 목걸이 | 1 | 힘형·민첩형·지능형 |
| 반지 | 2 | 화염 저항형·냉기 저항형·번개 저항형, 두 칸이 같은 종류 후보 사용 |
| 합계 | 10 | 양손도끼는 양손을 사용해 보조 장비와 함께 장착하지 않음 |

기본 성능과 특성의 실제 효과·수치는 후속 [DEC-0097](../Decisions/DEC-0097-equipment-affixes-base-stats-and-combat-numbers.md)의 [옵션·전투 기획서](Equipment-Affixes-and-Combat-Numbers.md)에서 확인했다. 첫 희귀 장비는 부위·양손 관계를 확인하고 별도 성급·레벨·능력치 착용 조건을 두지 않는다. 무료 장착·반지 칸 선택·양손 교체의 가방 공간과 젬 조건 재평가는 후속 [DEC-0100](../Decisions/DEC-0100-equipment-inventory-comparison-and-salvage.md)의 [장비 관리 기획서](Equipment-Inventory-Comparison-and-Salvage.md)를 따른다. 직업·무기별 스킬 호환성과 정식 젬 조건은 별도 확인한다. 기존 프로토타입의 무기·근력 조건·젬 연결 승인은 해당 구현 범위로 구분한다.

## 고유 장비와 장착

후속 [DEC-0104](../Decisions/DEC-0104-unique-equipment-with-multiple-equipped-items.md)의 [고유 기획서](Unique-Equipment-Role-Acquisition-and-Handling.md)는 목걸이·반지·허리띠 각 1종을 4/5성으로 제공한다. 부위가 맞는 여러 고유를 함께 착용하고 전체 1개 제한을 두지 않는다. 동일 고유 복수 착용·효과 중첩과 개별 성능/특수 효과는 다음 묶음에서 확인한다. 고유의 정해진 기반·일반 옵션 2개·특수 효과 1개는 아래 희귀 기반 후보와 무작위 옵션 추첨을 변경하지 않는다.

## 기반 역할·고정 특성

| 계열·부위 | 기반 3종의 역할 |
| --- | --- |
| 한손검·양손도끼 | 피해형·속도형·치명형 |
| 마법봉 | 주문 피해형·시전 속도형·치명형 |
| 머리·갑옷·장갑·장화·방패 | 방어도형·회피형·보호막형 |
| 목걸이 | 힘형·민첩형·지능형 |
| 반지 | 화염 저항형·냉기 저항형·번개 저항형 |
| 허리띠 | 생명력형·방어도형·보호막형 |

각 기반에 역할을 드러내는 고정 특성 1개를 제공한다. 같은 기반·성급에서는 해당 특성 수치가 고정되며 기본 추가·제거·교체·수치 재추첨의 4종 제작 작업으로 변경하지 않는다. 고정 특성은 추가 옵션 6칸과 별도다.

모든 기반 역할을 1~5성에 제공한다. 성급은 제작 잠재력, 기반은 빌드에서의 역할을 구분하는 기준이다. 기반 역할 이름은 기획용 분류이며 최종 아이템 이름·외형은 후속 기획에서 확인하며 실제 성능·특성 수치는 [옵션·전투 기획서](Equipment-Affixes-and-Combat-Numbers.md)를 따른다.

## 계열과 추가 옵션 후보 공유

| 후보를 공유하는 계열 | 공유 범위 |
| --- | --- |
| 무기 | 같은 무기 계열의 기반 3종끼리. 한손검·양손도끼·마법봉을 각각 구분 |
| 방어구 | 같은 부위의 기반 3종끼리. 방패도 하나의 부위로 구분 |
| 장신구 | 목걸이·반지·허리띠를 각각 구분. 반지 두 칸은 같은 후보 목록 사용 |

따라서 같은 부위의 방어도형·회피형·보호막형은 추가 옵션 종류 후보를 공유한다. 기반 역할을 다르게 골라도 같은 계열의 후보 종류가 달라지지 않는다. 첫 34종 옵션·접두/접미 분류·7단계 수치는 [공통 데이터](Equipment-Affixes-and-Combat-Numbers.md)를 따르며 제작 확률은 [기본 제작 기획서](Equipment-Crafting.md)를 따른다.

## 파밍 선택과 기반 확률

[승인된 부위 선택 파밍](Equipment-Drops-and-Farming-Targets.md)에 이 목록을 연결한다. 선택할 파밍 부위는 주무기·보조 장비·머리·갑옷·장갑·장화·허리띠·목걸이·반지다.

주무기 선택 시 해당 성급의 무기 3계열 × 기반 3종, 총 9종을 각각 1/9 확률로 추첨한다. 다른 파밍 부위는 각 3종을 각각 1/3 확률로 추첨한다. 반지 2칸은 파밍 부위 한 종류를 공유한다. 기본·모딩 추가 장비 보상에 같은 후보와 확률을 적용한다. 무기 계열·기반을 별도로 지정하는 추가 통제는 이번 승인 범위에 없다.

첫 목록의 기반은 성급당 33종이다. 무기 9종·방어구/방패 15종·장신구 9종을 합한 값이며, 성급 5단계를 합하면 165개 기반·성급 조합이다. 이 수는 슬롯 10칸이나 추가 옵션 종류 수와 구분한다.

## 후속 확인 묶음

기반 성능·고정 특성 수치, 접두/접미 후보와 적용 대상·7단계 범위·단위·계산은 [DEC-0097](../Decisions/DEC-0097-equipment-affixes-base-stats-and-combat-numbers.md)에서 확인했고 [옵션·전투 기획서](Equipment-Affixes-and-Combat-Numbers.md)에 모았다. 제작 실행·비용·확률은 [DEC-0098](../Decisions/DEC-0098-crafting-execution-costs-odds-and-recovery.md)에서 확인했고 [기본 제작 기획서](Equipment-Crafting.md)에 통합했다. 장비 보관·비교·교체·분해는 [DEC-0100](../Decisions/DEC-0100-equipment-inventory-comparison-and-salvage.md)에서 확인했고 [장비 관리 기획서](Equipment-Inventory-Comparison-and-Salvage.md)에 통합했다. [DEC-0102](../Decisions/DEC-0102-initial-crafting-scope-without-extra-special-crafting.md)에서 첫 제작은 기본 4종과 집중석부터 검증하는 A안으로 확인했다. 고유 공통 규칙은 [DEC-0104](../Decisions/DEC-0104-unique-equipment-with-multiple-equipped-items.md)에서 복수 착용으로 확인했다. 다음 미승인 묶음은 [첫 고유 3종의 효과·수치·중복과 빌드 검증](../Proposals/Unique-Equipment-Effects-and-Build-Cases.md)이다.

무기별 스킬 호환성·젬 요구 능력치·정식 젬 슬롯과 성장, 추가 무기 계열·보조 장비 종류·다른 특수 제작은 별도로 확인한다. 이번 목록을 향후 모든 무기·장비의 영구 목록으로 확정한 것은 아니다.

## 승인·조사·검증 상태

승인 이력은 [DEC-0096](../Decisions/DEC-0096-equipment-catalog-and-base-structure.md)이며, 선행 [기반 고정 특성](../Decisions/DEC-0022-base-fixed-traits.md)·[계열별 후보 공유](../Decisions/DEC-0023-shared-affix-pool-by-equipment-family.md)·[장비 득템과 파밍 대상](../Decisions/DEC-0095-equipment-drops-and-farming-targets.md)을 구체화했다.

[장비 분류 조사](../../Research/2026-11-18-equipment-catalog-and-affix-data.md)에 출처·버전·라이선스·호환성과 재사용 한계를 기록했다. 외부 코드·아이템 데이터·리소스를 반입하지 않았다.

현재 변경은 문서 반영이다. 정식 장비 목록을 Unity에 구현하거나 실제 전투·드롭·경제를 검증하지 않았다. 구현 전에 관련 기술 조사와 적용·검증 계획을 제안한다. 장착 관계·반지 후보 공유·성급별 기반 후보·기본/추가 드롭 일치와 균등 확률을 검토하고, 확정된 옵션·전투 수치표로 각 기반의 선택 이유와 한손/양손의 피해·생존 차이, 제작 출발점 획득 속도를 실제로 비교한다.
