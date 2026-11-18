# 희귀 장비 기본 제작 기획

상태: 사용자에게 확인받은 현행 제작 원칙을 모은 문서. [기본 제작의 실행·비용·확률](../Proposals/Crafting-Execution-Costs-and-Odds.md)은 아직 미승인 제안이다.

## 목적·대상과 장비 구조

좋은 드롭 장비의 기반과 기존 옵션을 보고 제작 출발점을 고른 뒤 빌드에 맞는 조합·단계·수치를 완성한다. 희귀 장비가 추가 옵션 제작의 중심이며 고유 장비는 정해진 특수 효과를 제공하고 일반 추가 옵션 제작에서는 제외한다.

희귀 장비의 추가 옵션은 접두 최대 3개·접미 최대 3개, 합계 최대 6개다. 같은 종류는 장비당 1개이며 단계·값이 달라도 같은 종류로 본다. 기반 고정 특성은 6칸과 별개이며 기본 4종 제작으로 변경하지 않는다. 획득한 성급은 고정이고 장비 간 추가 옵션 이전은 없다.

기반 목록과 특성의 역할은 [장비 구성](Equipment-Catalog-and-Base-Structure.md), 실제 기본 성능·특성 수치와 34종 후보·7단계 범위는 [장비 옵션·전투 데이터](Equipment-Affixes-and-Combat-Numbers.md)를 따른다.

## 기본 작업 4종

| 작업 | 확인된 효과 | 접두/접미 통제 |
| --- | --- | --- |
| 추가 | 빈 자리에 추가 옵션 1개 생성 | 선택한 그룹에 1개 추가 |
| 제거 | 기존 추가 옵션 1개 제거 | 선택한 그룹의 기존 옵션 중 1개 제거 |
| 교체 | 기존 추가 옵션 1개 제거 후 새 옵션 1개 생성 | 제거·새 생성 모두 선택한 같은 그룹 |
| 수치 재추첨 | 현재 모든 추가 옵션의 종류·단계를 유지하고 해당 범위에서 수치만 재추첨 | 그룹 지정 대상에 포함하지 않은 별도 전체 수치 작업 |

추가·제거·교체는 필요한 실행 조건과 비용을 만족하면 별도의 성공/실패 판정 없이 작업한다. 원하는 옵션 보장과는 다르며 좋은 옵션을 잃거나 새 결과가 나빠질 수 있다. 세 작업의 유효 대상과 정확한 추첨·비용은 다음 묶음에서 확인한다.

수치 재추첨은 현재 붙은 모든 추가 옵션을 함께 대상으로 하며 종류·단계는 유지한다. 새 수치는 나빠져도 바로 적용하고 기존 값과 새 값 중 고르지 않는다. 각 옵션 값의 정확한 분포·독립성·실행 조건과 비용은 후속 확인 사항이다.

## 교체·중복·단계

통제 없이 교체해도 방금 제거한 옵션과 같은 접두/접미 그룹에서 새 옵션을 생성한다. 접두·접미의 개수는 각각 유지된다. 나머지 옵션과 같은 종류를 동시에 중복시키지 않는다.

방금 제거한 종류는 새 후보에 다시 포함하므로 같은 종류가 재등장할 수 있다. 통제 여부나 같은 종류 재등장 여부와 관계없이 새 옵션의 단계는 장비 성급의 허용 범위에서 다시 추첨하며 기존보다 높거나 낮거나 같을 수 있다.

성급별 허용 단계는 1성 1~3·2성 2~4·3성 3~5·4성 4~6·5성 5~7이다. 단계별 정수 수치 범위는 [공통 데이터](Equipment-Affixes-and-Combat-Numbers.md)다. 공통 범위를 쓰는 것과 드롭/제작의 추첨 확률을 같게 정하는 것은 구분하며 제작 가중치·단계/값 확률은 아직 미정이다.

## 재료와 통제

추가·제거·교체·수치 재추첨에 서로 다른 전용 기본 재료를 한 종류씩 배정해 기본 재료 4종으로 구성한다. 추가·제거·교체의 접두/접미 지정에는 별도의 공통 통제 재료 1종을 추가로 사용한다. 같은 통제 재료로 접두 또는 접미를 지정하고 그룹 안의 개별 결과는 무작위다. 통제 재료 없는 제작도 제공한다.

기본 제작의 재료 이름·한 번 소모량·통제 비용과 그 밖의 공통 추가 비용은 아직 미정이다. [파밍 공급](Farming-Dungeon-Modification.md)의 재료 비율과 던전 소모량을 장비 제작 비용으로 자동 확대하지 않는다. 다음 [제작 실행 묶음](../Proposals/Crafting-Execution-Costs-and-Odds.md)의 이름·비용은 확인할 추천값이다.

## 횟수·정보와 남은 범위

기본 4종에는 장비당 제작 횟수 제한이 없다. 실행 조건과 비용을 만족하면 같은 장비를 계속 다듬을 수 있다. 반복했다고 제작 가능 횟수가 소진되는 구조는 두지 않는다.

현재 장비·작업·통제 조건에 맞는 옵션 후보·허용 단계·수치 범위와 종류/단계별 추첨 확률을 게임 안에서 공개한다. 정확한 제작 확률·값별 확률·복합 결과·반복 기대 비용과 정보 화면은 후속 확인 사항이다.

다음 묶음은 재료 이름·비용·유효 대상·추첨·무효 동작과 통제·차감·취소/중단·복원·장착 중 제작이다. 보호/특수 제작·직접 옵션 지정·자동/일괄 제작·장비 처분과 투자 재료 회수, 재료 교환/다른 공급은 별도로 확인한다.

## 승인 이력·조사·검증

- 제작 출발점·희귀/고유 역할: [DEC-0020](../Decisions/DEC-0020-drop-equipment-crafting-start.md), [DEC-0012](../Decisions/DEC-0012-crafting-equipment-scope.md)
- 기본 3종·그룹 통제·별도 실패 판정 없음: [DEC-0015](../Decisions/DEC-0015-basic-crafting-operations.md), [DEC-0016](../Decisions/DEC-0016-control-all-basic-operations.md), [DEC-0018](../Decisions/DEC-0018-basic-crafting-no-failure-roll.md)
- 전체 수치 재추첨·즉시 결과: [DEC-0035](../Decisions/DEC-0035-reroll-affix-values-keeping-types-and-tiers.md), [DEC-0036](../Decisions/DEC-0036-reroll-values-of-all-existing-affixes.md), [DEC-0037](../Decisions/DEC-0037-apply-new-rerolled-values-directly.md)
- 재료 4+1종·교체 그룹/중복/재등장/새 단계: [DEC-0038](../Decisions/DEC-0038-dedicated-basic-materials-for-each-crafting-operation.md), [DEC-0039](../Decisions/DEC-0039-shared-material-for-prefix-suffix-control.md), [DEC-0040](../Decisions/DEC-0040-keep-affix-group-in-uncontrolled-replacement.md), [DEC-0041](../Decisions/DEC-0041-one-affix-of-each-kind-per-rare-equipment.md), [DEC-0046](../Decisions/DEC-0046-allow-removed-affix-kind-to-reappear-in-replacement.md), [DEC-0047](../Decisions/DEC-0047-reroll-replacement-affix-tier-within-equipment-grade.md)
- 제작 횟수·정보 공개: [DEC-0048](../Decisions/DEC-0048-no-per-equipment-crafting-attempt-limit.md), [DEC-0051](../Decisions/DEC-0051-disclose-crafting-candidates-ranges-and-probabilities.md)

[PoE 2 제작 조사](../../Research/Crafting/README.md)와 [출처/라이선스](../../Research/Crafting/Sources.md)를 참고한다. 이번 문서는 선행 승인 원칙을 통합한 것이며 새로운 비용·확률을 확정하지 않는다. 실제 게임의 제작·저장·경제를 실행 검증한 결과도 아니다.

제작 실행 묶음을 확인받고 구현 전 기술 조사와 적용·검증 계획을 제안한다. 이후 유효/무효 작업·상한/중복·교체 보존과 분포·전체 수치 재추첨·차감/종료/복원과 정보 일치, 실제 파밍 공급과 제작 소모·완성 비용을 검증한다.
