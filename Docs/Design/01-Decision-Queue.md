# 사용자와 확인할 기획 순서

확인된 방향은 [라이트한 PoE와 종결 장비 제작 중심](00-Concept.md)이다. 장비·스킬은 PoE 1, 제작은 PoE 2를 참조한다. 아래는 그 방향을 구체화하기 위해 남은 질문이며 답은 미정이다. 사용자가 다른 주제를 먼저 다루길 원하면 순서를 바꾼다.

종결 장비는 [빌드별 조합과 등급·수치 완성의 혼합형](Decisions/DEC-0010-endgame-definition.md), 추가 옵션은 [접두 최대 3개·접미 최대 3개](Decisions/DEC-0011-affix-slots.md)로 확인했다. [희귀 장비가 추가 옵션 제작의 중심이며 고유 장비는 특수 효과 역할](Decisions/DEC-0012-crafting-equipment-scope.md)을 맡는다. 제작은 [무작위 결과에 제한적인 통제 수단을 제공](Decisions/DEC-0013-crafting-randomness-control.md)하며, [접두·접미 중 대상 그룹을 선택](Decisions/DEC-0014-prefix-suffix-control.md)하는 방식이다.

기본 제작은 [옵션 한 개씩 추가·제거·교체하는 세 작업](Decisions/DEC-0015-basic-crafting-operations.md)으로 확인했다. [세 작업 모두 접두·접미 통제를 허용](Decisions/DEC-0016-control-all-basic-operations.md)하며 통제한 교체는 제거와 추가 모두 같은 그룹 안에서 진행한다. 기본 세 작업에는 [별도의 성공·실패 판정을 두지 않는다](Decisions/DEC-0018-basic-crafting-no-failure-roll.md). [그룹 지정에는 기본 비용 외에 추가 통제 재료를 사용](Decisions/DEC-0019-extra-material-for-affix-control.md)한다.

주력 제작은 [좋은 드롭 장비를 골라 다듬는 경로](Decisions/DEC-0020-drop-equipment-crafting-start.md)다. 희귀 장비는 [일부 옵션과 6개 옵션 구성을 함께 드롭](Decisions/DEC-0021-partial-and-full-affix-drops.md)한다. [기반 고정 특성은 추가 옵션 6칸과 별도로 제공](Decisions/DEC-0022-base-fixed-traits.md)한다. [같은 장비 계열의 기반들은 추가 옵션 후보를 공유](Decisions/DEC-0023-shared-affix-pool-by-equipment-family.md)한다.

제작 잠재력은 [진행 구간별 소수의 장비 등급을 직접 표시](Decisions/DEC-0024-visible-progression-equipment-grades.md)하는 방식으로 구분한다. 단계 수는 [5단계](Decisions/DEC-0025-five-equipment-grades.md)로 확인했다. 다음은 [5단계 장비 등급의 역할 배분](Proposals/Crafting-Endgame.md)을 확인하는 순서를 제안한다.

| 순서 | 논의할 내용 | 확인 후 구체화할 수 있는 내용 |
| --- | --- | --- |
| 1 | 구간별 장비 등급과 옵션 구조 | 5단계 장비 등급의 역할 배분, 획득 구간과 제작 가능 범위, 장비 계열·기반과 개별 옵션 |
| 2 | 기본 작업의 세부 규칙 | 무통제 교체의 그룹 관계, 실행 조건과 불가능한 작업의 처리 |
| 3 | 보존과 손실·특수 제작 | 기존 옵션을 보호할지, 특수 제작을 도입할지와 그 위험 |
| 4 | 재료와 득템 구조 | 자동 전투의 획득물, 제작 출발점과 완제품 드롭의 관계 |
| 5 | 경쟁의 평가 방식 | 장비 자체, 자동 전투 결과, 목표 기록 중 무엇을 비교할지 |
| 6 | 장비·스킬 조합과 캐릭터 구성 | 제작한 장비가 어떤 빌드에서 유효한지 |
| 7 | 한 번 접속했을 때의 흐름 | 파밍 결과 확인, 제작 판단, 장비 변경과 도전의 연결 |
| 8 | 모바일 화면·세계관·아트 | 판단할 정보와 게임의 표현 기준 |
| 9 | 프로토타입 범위와 검증 목표 | 승인한 제작·전투 규칙의 구현 범위와 평가 방법 |
| 10 | 데이터와 수치 | 드롭 최소 옵션 개수·배치·분포, 제작 확률, 비용, 보상과 성장 속도의 실험 입력값 |

오프라인 진행, 과금과 운영 방식은 별도 질문으로 확인한다. 목표 이용자, 개발 인원과 일정도 정해지는 시점에 범위 논의에 반영한다. 임의의 목표 수치나 출시 일정을 채워 넣지 않는다.

## 다음 제안을 만들 때

선택지는 실제 플레이 경험의 차이가 드러나게 설명한다. 예를 들어 화면 방향을 질문할 때는 한 손 이용 가능성과 전투·장비 비교 공간을 함께 설명하고, 최종 배치와 버튼 규격은 방향을 확인한 뒤 제안한다. 서로 독립된 질문의 답을 하나의 승인으로 묶지 않는다.
