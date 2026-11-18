# 파밍 던전 변화 기획

상태: 사용자에게 확인받은 현행 규칙. 승인 근거는 연결된 결정 이력에서 확인한다. 미정 사항은 [기능별 후속 제안](../Proposals/Dungeon-Modification.md)에서 묶어 검토한다.

## 목적과 적용 범위

재화를 투자해 던전에 패널티를 부여하고 보상을 높인다. 파밍에만 적용하며 최고 도달 단계 경쟁은 공통 도전 조건을 유지한다. 경쟁의 장비·능력치를 평준화하는 규칙은 아니다. 근거: [DEC-0060](../Decisions/DEC-0060-currency-funded-dungeon-penalties-and-better-rewards.md), [DEC-0061](../Decisions/DEC-0061-dungeon-modification-for-farming-only.md).

기본 흐름은 파밍 대상 선택 → 패널티 없이 입장하거나 최초 패널티 부여 → 필요에 따라 한 줄 교체 → 자동 전투 도전 → 성공·실패 후 패널티와 연결된 보상 강화 설정 초기화다.

## 던전 준비·변경 기본 동작

아래 동작을 [DEC-0090](../Decisions/DEC-0090-farming-dungeon-preparation-and-modification-rules.md)에서 하나의 기능 묶음으로 확인했다.

| 항목 | 확인된 동작 |
| --- | --- |
| 패널티 없이 도전 | 패널티를 부여하지 않은 상태로도 입장 허용 |
| 최초 부여 비용 | 추가·교체 재료 중 하나를 선택해 해당 재료 1개 소모 |
| 한 줄 교체 비용 | 교체할 때마다 옵션 교체 재료 1개 소모 |
| 부여 후 조정 | 같은 도전 준비에서 최초 부여는 1회. 이후 추가·전체 재추첨 없이 한 줄 교체만 제공 |
| 잠금 | 최초 부여 직후 전부 잠금. 선택한 줄은 교체 뒤에도 해제 상태 유지 |
| 실행 불가 | 전부 잠겼거나 재료가 부족하면 교체 버튼 비활성화·사유 안내, 차감 없음 |
| 변경 시점 | 전투 시작 전 준비 중에만 변경 가능 |

패널티 없는 입장 허용이 최초 입장 자체의 비용을 정하는 것은 아니다. 최초 부여 재료의 환급·취소·중단 처리는 아직 미정이다. 장비 제작의 재료 소모량을 던전 변화와 같은 1개로 확정하는 결정도 아니다.

## 최초 패널티 생성

한 번의 작업으로 최초 패널티들을 함께 무작위 생성한다. 장비 제작 기본 재료 4종 중 옵션 추가·교체의 두 기본 재료를 공유한다. 이 최초 부여를 위한 별도 전용 재화는 추가하지 않는다.

| 사용하는 기본 재료 | 생성할 패널티 개수와 확률 |
| --- | --- |
| 옵션 추가 재료 | 1개 50%, 2개 50% |
| 옵션 교체 재료 | 3개 50%, 4개 50% |

표는 생성할 패널티 개수다. 최초 부여는 두 재료 중 선택한 한 종류를 1개 소모한다. 패널티 종류는 유효 후보 중 같은 확률로 추첨하며 종류별 고정 강도는 아래 콘텐츠 묶음을 따른다. 기본 드롭 테이블과 다른 실행 조건은 미정이다. 최초 부여와 장비 제작에 같은 재료를 쓰더라도 작업 효과·비용·확률이 같다는 뜻은 아니다.

근거: [DEC-0078](../Decisions/DEC-0078-initial-farming-dungeon-penalties-generated-as-one-random-batch.md), [DEC-0082](../Decisions/DEC-0082-currency-dependent-random-count-for-initial-dungeon-penalties.md), [DEC-0083](../Decisions/DEC-0083-two-currency-types-for-initial-dungeon-penalty-generation.md), [DEC-0085](../Decisions/DEC-0085-share-two-equipment-crafting-materials-with-initial-dungeon-penalty-generation.md), [DEC-0086](../Decisions/DEC-0086-use-affix-addition-and-replacement-materials-for-initial-dungeon-penalties.md), [DEC-0088](../Decisions/DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md), [DEC-0089](../Decisions/DEC-0089-initial-dungeon-penalty-generation-rules.md).

## 패널티 조정

| 항목 | 확인된 동작 | 승인 근거 |
| --- | --- | --- |
| 교체 범위 | 플레이어가 지정한 한 줄을 무작위 교체하고 나머지 줄과 전체 개수를 보존 | [DEC-0064](../Decisions/DEC-0064-reroll-one-selected-dungeon-penalty.md) |
| 조작 | 각 패널티 줄 우측에 잠금 체크박스 토글, 체크한 줄 보존 | [DEC-0065](../Decisions/DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md) |
| 대상 전환 | 잠금 해제는 최대 한 줄, 다른 줄 해제 시 기존 줄 자동 잠금 | [DEC-0066](../Decisions/DEC-0066-allow-only-one-unlocked-dungeon-penalty-row.md) |
| 결과 | 새 결과가 빌드에 더 불리해져도 바로 적용 | [DEC-0067](../Decisions/DEC-0067-apply-new-dungeon-penalty-result-directly.md) |
| 재료 | 교체 실행마다 장비 옵션 교체의 기본 재료 소모 | [DEC-0068](../Decisions/DEC-0068-consume-currency-for-each-dungeon-penalty-replacement.md), [DEC-0070](../Decisions/DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md) |
| 비용과 횟수 | 같은 조건에서는 반복 횟수에 따른 비용 증가 없음. 별도 교체 횟수 제한 없음 | [DEC-0071](../Decisions/DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md), [DEC-0073](../Decisions/DEC-0073-no-attempt-limit-for-dungeon-penalty-replacement.md) |

교체는 매번 옵션 교체 재료 1개를 소모한다. 기본 잠금·교체 뒤 해제 유지·실행 불가 처리는 위 준비 묶음을 따른다. 종류 추첨·중복 금지·재등장과 고정 강도는 아래 콘텐츠 묶음을 따른다. 이 준비 기능에서는 최초 부여 뒤 추가·삭제·전체 재추첨을 제공하지 않으므로 해당 도전의 패널티 개수는 최초 생성 개수로 유지된다.

## 패널티·보상 콘텐츠

종류·강도·추첨·추가 드롭·정산과 표시를 [DEC-0092](../Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md)에서 하나의 콘텐츠 묶음으로 확인했다. 초기 패널티는 아래 6종이며 각 종류는 고정 강도 하나로 시작한다.

| 패널티 | 고정 효과 |
| --- | --- |
| 몬스터 생명력 강화 | 몬스터 최대 생명력 30% 증가 |
| 몬스터 공격 강화 | 몬스터가 주는 피해 20% 증가 |
| 몬스터 공격 가속 | 몬스터 공격속도 15% 증가 |
| 플레이어 회복 약화 | 받는 생명력 회복량 ×0.7 |
| 플레이어 치명타 약화 | 치명타 확률 ×0.7 |
| 플레이어 지속 피해 약화 | 주는 지속 피해 ×0.7 |

비율은 해당 효과 적용 전 계산값에 한 번 곱한다. 치명타 확률은 30%p 차감이 아니라 기존 확률의 0.7배다. 공격속도 효과는 몬스터의 공격에 적용한다. 현재 초기 콘텐츠에 별도 강도 등급·수치 재추첨을 두지 않는다.

### 종류 추첨과 교체

- 최초 부여는 승인된 개수에 맞춰 6종에서 같은 확률로 중복 없이 추첨한다. 매 추첨 때 유효한 후보 사이에서 균등하게 고른다.
- 같은 종류는 한 도전에 한 줄만 허용한다.
- 한 줄 교체는 잠긴 나머지 줄에 있는 종류를 제외한 후보에서 같은 확률로 추첨한다.
- 방금 제거한 종류도 후보에 포함하므로 같은 결과가 다시 나올 수 있다. 나머지 줄과 전체 개수는 보존한다.
- 현재 6종에서는 종류 중복 외 별도 조합 금지를 두지 않는다. 규칙·수치 변경은 검증 결과와 사용자 확인을 거친다.

### 추가 드롭과 정산

강화 대상은 장비·제작재료의 추가 드롭 기회다. 기본 드롭 추첨마다 패널티 수 × 20% 확률로 같은 범주의 기본 테이블에서 추가로 한 번 독립 추첨한다. 추가 추첨에는 보너스를 다시 적용하지 않는다.

| 패널티 수 | 기본 추첨마다 추가 1회 추첨할 확률 | 성공 시 평균 드롭 기대량의 배율 |
| --- | --- | --- |
| 0개 | 0% | 1.0배 |
| 1개 | 20% | 1.2배 |
| 2개 | 40% | 1.4배 |
| 3개 | 60% | 1.6배 |
| 4개 | 80% | 1.8배 |

평균 배율은 매번 보장되는 획득량이 아니다. 기본 추첨의 성공·실패와 별개로 추가 여부를 추첨한다. 장비 성급·옵션 등급·희귀도와 후보 가중치는 같은 기본 드롭 테이블을 따른다. 경험치·골드·랭킹 등 다른 보상에 이 보너스를 자동 적용하지 않는다.

한 줄 교체에서는 줄 수가 유지되므로 추가 드롭 확률도 유지된다. 모딩으로 생긴 추가 보상은 클리어 성공 때 정산하고 실패하면 그 추가분은 지급하지 않는다. 기본 드롭 테이블·공급량·기본 실패 보상·도중 획득물의 처리는 후속 수급·정산 묶음에서 확인한다.

### 정보 표시

준비 화면에 각 패널티의 실제 효과·현재 줄 수·장비와 제작재료의 추가 드롭 확률을 함께 표시한다. 예를 들어 3줄이면 추가 추첨 확률 60%라고 안내한다. 생존·회복·치명타·지속 피해 같은 영향 태그로 확인할 대상을 설명한다. 이 표시가 자동 안전 판정이나 성공 보장을 뜻하지 않는다.

## 도전 종료와 재도전

| 상황 | 확인된 처리 | 승인 근거 |
| --- | --- | --- |
| 클리어 성공 | 패널티와 연결된 보상 강화 설정 초기화 | [DEC-0074](../Decisions/DEC-0074-reset-farming-dungeon-modifiers-after-successful-clear.md) |
| 클리어 실패 | 패널티와 연결된 보상 강화 설정 초기화 | [DEC-0075](../Decisions/DEC-0075-reset-farming-dungeon-modifiers-after-failure.md) |
| 모딩 추가 보상 | 성공 때 지급, 실패하면 그 추가분은 지급하지 않음 | [DEC-0092](../Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md) |
| 실패한 도전의 교체 재료 | 이미 쓴 패널티 교체 재료는 환급하지 않음 | [DEC-0076](../Decisions/DEC-0076-no-refund-of-dungeon-penalty-replacement-materials-after-failure.md) |
| 실패 후 재도전 | 같은 파밍 대상에 새 도전 허용, 재도전 입장 자체의 별도 비용 없음 | [DEC-0077](../Decisions/DEC-0077-allow-farming-retries-without-separate-entry-cost.md) |

재도전 횟수·대기 시간·기타 조건, 최초 입장 비용, 최초 부여 재료의 환급과 취소·중단·접속 종료 처리, 기본 실패 보상은 아직 미정이다. 설정 초기화가 새 패널티의 자동 부여나 자동 반복 입장을 뜻하지 않는다.

## 후속 확인 묶음

| 기능·개념 | 한 번에 확인할 범위 |
| --- | --- |
| 파밍 수급·정산 | 입장·재도전 조건, 기본 보상과 재료 공급, 최초 부여 재료와 취소·중단의 환급, 재접속·대상 전환과 중복 정산 방지 |

사용자가 확인한 기능 묶음은 이 문서에 통합하고 결정 파일 하나를 승인 이력으로 연결한다. 아직 승인되지 않은 제안을 현행 규칙에 섞지 않는다.

## 조사와 검증

[맵 모딩 조사](../../Research/2026-11-17-dungeon-modification.md), [재화별 개수 생성 조사](../../Research/2026-11-18-currency-dependent-dungeon-penalty-counts.md), [패널티·보상 콘텐츠 조사](../../Research/2026-11-18-dungeon-penalties-and-rewards.md)에 출처·확인 버전·라이선스·Unity 호환성과 재사용 한계를 기록했다. 이 기능을 위해 외부 코드·데이터·리소스를 반입하지 않았다.

현재 이 기획의 변경은 문서 정리까지다. 문서 구조·승인 필드·참조·링크 검사를 게임 실행이나 확률·난도·경제 검증으로 취급하지 않는다. 관련 기능 묶음을 승인받은 뒤 실제 추첨 분포·한 줄 교체의 보존·종료 후 초기화·재료 소비와 보상 균형을 검증한다.
