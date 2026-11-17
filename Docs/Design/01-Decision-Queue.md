# 사용자와 확인할 기획 순서

확인된 방향은 [라이트한 PoE와 종결 장비 제작 중심](00-Concept.md)이다. 장비·스킬은 PoE 1, 제작은 PoE 2를 참조한다. 아래는 그 방향을 구체화하기 위해 남은 질문이며 답은 미정이다. 사용자가 다른 주제를 먼저 다루길 원하면 순서를 바꾼다.

종결 장비는 [빌드별 조합과 등급·수치 완성의 혼합형](Decisions/DEC-0010-endgame-definition.md), 추가 옵션은 [접두 최대 3개·접미 최대 3개](Decisions/DEC-0011-affix-slots.md)로 확인했다. [희귀 장비가 추가 옵션 제작의 중심이며 고유 장비는 특수 효과 역할](Decisions/DEC-0012-crafting-equipment-scope.md)을 맡는다. 제작은 [무작위 결과에 제한적인 통제 수단을 제공](Decisions/DEC-0013-crafting-randomness-control.md)하며, [접두·접미 중 대상 그룹을 선택](Decisions/DEC-0014-prefix-suffix-control.md)하는 방식이다.

기본 제작은 [옵션 한 개씩 추가·제거·교체하는 세 작업](Decisions/DEC-0015-basic-crafting-operations.md)으로 확인했다. [세 작업 모두 접두·접미 통제를 허용](Decisions/DEC-0016-control-all-basic-operations.md)하며 통제한 교체는 제거와 추가 모두 같은 그룹 안에서 진행한다. 기본 세 작업에는 [별도의 성공·실패 판정을 두지 않는다](Decisions/DEC-0018-basic-crafting-no-failure-roll.md). [그룹 지정에는 기본 비용 외에 추가 통제 재료를 사용](Decisions/DEC-0019-extra-material-for-affix-control.md)한다. [공통 통제 재료 1종을 세 작업이 공유](Decisions/DEC-0039-shared-material-for-prefix-suffix-control.md)하며, 같은 재료로 접두 또는 접미를 선택한다.

주력 제작은 [좋은 드롭 장비를 골라 다듬는 경로](Decisions/DEC-0020-drop-equipment-crafting-start.md)다. 희귀 장비는 [일부 옵션과 6개 옵션 구성을 함께 드롭](Decisions/DEC-0021-partial-and-full-affix-drops.md)한다. [기반 고정 특성은 추가 옵션 6칸과 별도로 제공](Decisions/DEC-0022-base-fixed-traits.md)한다. [같은 장비 계열의 기반들은 추가 옵션 후보를 공유](Decisions/DEC-0023-shared-affix-pool-by-equipment-family.md)한다.

제작 잠재력은 [진행 구간별 소수의 장비 등급을 직접 표시](Decisions/DEC-0024-visible-progression-equipment-grades.md)하는 방식으로 구분한다. 단계 수는 [5단계](Decisions/DEC-0025-five-equipment-grades.md)이며, [1~3성은 성장 초반·중반·후반, 4성은 엔드게임 진입, 5성은 종결 제작](Decisions/DEC-0026-growth-focused-equipment-grade-roles.md)으로 역할을 배분했다. [성급이 높아질수록 허용 옵션 등급의 하한과 상한을 함께 높이는 원칙](Decisions/DEC-0027-rising-affix-tier-floor-and-ceiling.md)을 확인했다. [획득한 희귀 장비의 성급은 고정](Decisions/DEC-0028-fixed-rare-equipment-star-grade.md)한다. [희귀 장비의 추가 옵션은 다른 장비로 이전하지 않는다](Decisions/DEC-0029-no-affix-transfer-between-rare-equipment.md). [5성 희귀 장비는 드롭과 제작 모두 최상위 등급 추가 옵션을 허용](Decisions/DEC-0030-top-tier-affixes-from-drops-and-crafting.md)한다. [개별 옵션의 성능 등급은 7단계](Decisions/DEC-0031-seven-affix-performance-tiers.md)로 구성한다. [성급별 허용 범위는 낮은 쪽부터 1성 1~3, 2성 2~4, 3성 3~5, 4성 4~6, 5성 5~7](Decisions/DEC-0032-three-affix-tiers-per-equipment-grade.md)로 확인했다. [같은 옵션 등급 안에서도 최솟값~최댓값 범위의 여러 수치를 추첨](Decisions/DEC-0033-random-values-within-affix-tier-ranges.md)한다. [같은 옵션의 인접 등급 간 수치 범위는 일부 겹치도록 설계](Decisions/DEC-0034-overlapping-value-ranges-between-adjacent-affix-tiers.md)한다. [옵션 종류·등급을 유지하는 별도 수치 재추첨 작업](Decisions/DEC-0035-reroll-affix-values-keeping-types-and-tiers.md)을 제공한다. [수치 재추첨은 현재 붙어 있는 모든 추가 옵션을 대상](Decisions/DEC-0036-reroll-values-of-all-existing-affixes.md)으로 한다. [재추첨한 새 결과를 바로 적용](Decisions/DEC-0037-apply-new-rerolled-values-directly.md)한다. [추가·제거·교체·수치 재추첨에 각각 전용 기본 재료를 배정해 4종으로 구성](Decisions/DEC-0038-dedicated-basic-materials-for-each-crafting-operation.md)한다. [통제 없는 교체도 제거한 옵션의 그룹을 유지](Decisions/DEC-0040-keep-affix-group-in-uncontrolled-replacement.md)한다. [동일 종류의 추가 옵션은 드롭·제작 공통으로 희귀 장비당 1개](Decisions/DEC-0041-one-affix-of-each-kind-per-rare-equipment.md)로 제한한다. [교체에서 제거한 옵션 종류의 재등장을 허용](Decisions/DEC-0046-allow-removed-affix-kind-to-reappear-in-replacement.md)한다. [교체할 새 옵션의 등급은 장비 성급의 허용 범위에서 다시 추첨](Decisions/DEC-0047-reroll-replacement-affix-tier-within-equipment-grade.md)한다. [희귀 장비의 네 제작 작업에 장비당 횟수 제한을 두지 않는다](Decisions/DEC-0048-no-per-equipment-crafting-attempt-limit.md). [제작 후보·등급·수치 범위와 옵션 종류별·등급별 확률을 게임 안에서 공개](Decisions/DEC-0051-disclose-crafting-candidates-ranges-and-probabilities.md)한다. [종결 장비 경쟁은 자동 전투 성과를 중심으로 평가](Decisions/DEC-0053-endgame-competition-centered-on-auto-combat-results.md)한다. [주 평가 지표는 최고 도달 단계](Decisions/DEC-0054-highest-stage-as-primary-competition-metric.md)다. 다음은 [단계 도전의 시간 제한 방식](Proposals/Endgame-Competition.md)을 확인하는 순서를 제안한다.

| 순서 | 논의할 내용 | 확인 후 구체화할 수 있는 내용 |
| --- | --- | --- |
| 1 | 단계 도전의 시간 제한 방식 | 단계별 제한 시간·도전 전체 공통 시간·시간 제한 없음 중 무엇을 적용할지 |
| 2 | 기본 작업과 제작 정보 | 공개 정보의 세부 표현, 새 옵션 수치의 상세 추첨과 등급별 확률·가중치, 실행 조건과 불가능한 작업의 처리 |
| 3 | 장비·옵션 구조와 수치 제작 | 기본·통제 재료의 이름·소모량·공급과 공통 추가 비용의 도입 여부, 수치 재추첨의 비용·실행 조건과 추가 통제·보호 수단의 도입 여부, 정확한 획득 구간과 개별 옵션의 적용 범위·예외, 장비 계열·기반과 개별 옵션 |
| 4 | 보존과 손실·특수 제작 | 기존 옵션을 보호할지, 특수 제작을 도입할지와 그 위험 |
| 5 | 재료와 득템 구조 | 자동 전투의 획득물, 제작 출발점과 완제품 드롭의 관계 |
| 6 | 장비·스킬 조합과 캐릭터 구성 | 제작한 장비가 어떤 빌드에서 유효한지 |
| 7 | 한 번 접속했을 때의 흐름 | 파밍 결과 확인, 제작 판단, 장비 변경과 도전의 연결 |
| 8 | 모바일 화면·세계관·아트 | 판단할 정보와 게임의 표현 기준 |
| 9 | 프로토타입 범위와 검증 목표 | 승인한 제작·전투 규칙의 구현 범위와 평가 방법 |
| 10 | 데이터와 수치 | 드롭 최소 옵션 개수·배치·분포, 제작 확률, 비용, 보상과 성장 속도의 실험 입력값 |

오프라인 진행, 과금과 운영 방식은 별도 질문으로 확인한다. 목표 이용자, 개발 인원과 일정도 정해지는 시점에 범위 논의에 반영한다. 임의의 목표 수치나 출시 일정을 채워 넣지 않는다.

## 다음 제안을 만들 때

선택지는 실제 플레이 경험의 차이가 드러나게 설명한다. 예를 들어 화면 방향을 질문할 때는 한 손 이용 가능성과 전투·장비 비교 공간을 함께 설명하고, 최종 배치와 버튼 규격은 방향을 확인한 뒤 제안한다. 서로 독립된 질문의 답을 하나의 승인으로 묶지 않는다.
