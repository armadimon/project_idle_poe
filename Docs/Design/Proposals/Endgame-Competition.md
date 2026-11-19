# 종결 장비 경쟁의 평가 기준과 세부 제안

확인된 방향은 [종결 장비를 통한 경쟁](../Decisions/DEC-0008-endgame-gear-competition.md)과 [빌드별 옵션 조합·등급·수치 완성](../Decisions/DEC-0010-endgame-definition.md)이다. 전투는 [완전 자동](../Decisions/DEC-0002-combat-control.md)으로 진행한다. 경쟁은 후속 [DEC-0053](../Decisions/DEC-0053-endgame-competition-centered-on-auto-combat-results.md)에 따라 자동 전투 성과를 중심으로 평가한다. 주 지표는 후속 [DEC-0054](../Decisions/DEC-0054-highest-stage-as-primary-competition-metric.md)에서 최고 도달 단계로 확인했다. 시간 제한은 후속 [DEC-0057](../Decisions/DEC-0057-separate-time-limit-for-each-competition-stage.md)에서 단계별 적용으로 확인했다. 재도전의 시작 지점은 후속 [DEC-0058](../Decisions/DEC-0058-retry-competition-from-the-failed-stage.md)에서 실패한 단계로 확인했다. 재도전 입장 자체의 별도 비용은 후속 [DEC-0059](../Decisions/DEC-0059-no-separate-entry-cost-for-competition-retries.md)에서 두지 않기로 확인했다. 재화로 던전 패널티와 보상을 높이는 방향은 [DEC-0060](../Decisions/DEC-0060-currency-funded-dungeon-penalties-and-better-rewards.md)에서 확인했다. 던전 변화는 후속 [DEC-0061](../Decisions/DEC-0061-dungeon-modification-for-farming-only.md)에서 파밍에만 적용하고 이 경쟁은 공통 도전 조건을 유지하는 것으로 확인했다.

## 확인된 경쟁의 중심 기준

같은 도전에서 제작한 장비·스킬 조합이 낸 **자동 전투 성과를 중심으로 평가**한다. 사용자는 장비 자체의 완성도 점수와 비교해 이 1안을 선택했다. 확인 근거는 [DEC-0053](../Decisions/DEC-0053-endgame-competition-centered-on-auto-combat-results.md)에 기록했다.

중심 기준은 자동 전투 성과이며 주 지표는 아래와 같이 최고 도달 단계로 확인했다. 구체적인 평가 조건·공식·보상과 장비 자체 점수의 보조 제공 여부는 별도 확인한다.

## 확인된 자동 전투 성과의 주 평가 지표

주 지표는 **최고 도달 단계**다. 점점 강해지는 도전을 어디까지 돌파했는지 비교한다. 사용자는 피해량·클리어 시간 대안과 비교해 최고 도달 단계를 선택했다. 확인 근거는 [DEC-0054](../Decisions/DEC-0054-highest-stage-as-primary-competition-metric.md)에 기록했다.

이번 결정은 주 지표까지다. 시간 제한을 단계별로 적용하는 원칙은 아래와 같이 확인했다. 기록으로 인정할 조건과 단계 구성·수·상한, 구체적인 시간과 실패·동률 처리 및 보조 지표의 도입 여부는 별도 확인한다. 무한 단계나 특정 보스·던전을 자동으로 채택하지 않는다.

## 확인된 단계 도전의 시간 제한 방식

**각 단계에 별도의 제한 시간을 적용**해 주어진 시간 안에 돌파해야 한다. 사용자는 세 대안 중 단계별 제한 시간을 선택했다. 확인 근거는 [DEC-0057](../Decisions/DEC-0057-separate-time-limit-for-each-competition-stage.md)에 기록했다.

이번 결정은 시간 제한의 적용 단위까지다. 실패 후 재도전은 아래와 같이 실패한 단계부터 시작한다. 구체적인 시간 수치와 모든 단계의 시간을 같게 둘지, 측정의 시작·정지 조건, 시간 초과와 그 밖의 실패 후 처리는 미정이다. 도전 전체의 공통 제한 시간을 함께 적용하는 구성은 채택하지 않았다.

## 확인된 실패 후 재도전의 시작 지점

**실패한 단계부터 재도전**한다. 이전에 돌파한 단계를 다시 등반하지 않고 막힌 단계를 다시 시험할 수 있다. 사용자는 처음부터 다시 등반하는 대안과 비교해 이 1안을 선택했다. 확인 근거는 [DEC-0058](../Decisions/DEC-0058-retry-competition-from-the-failed-stage.md)에 기록했다.

이번 결정은 재도전의 시작 지점까지다. 재도전 입장 자체의 별도 비용을 두지 않는 원칙은 아래와 같이 확인했다. 자동으로 재도전할지와 플레이어가 선택하는 방법, 단계 접근 권한과 해금 유지 기간·시즌 초기화, 체력·스킬 재사용 시간 등의 초기화, 적·시간의 재설정, 재도전 횟수와 보상·기록 인정은 별도 확인한다.

## 확인된 재도전의 입장 비용

**재도전 입장 자체에는 별도 재료·재화를 소모하지 않는다.** 사용자는 입장 비용이 없는 1안을 선택했다. 확인 근거는 [DEC-0059](../Decisions/DEC-0059-no-separate-entry-cost-for-competition-retries.md)에 기록했다.

이번 결정은 재도전 입장 비용까지다. 재도전 횟수·대기 시간·자동 반복 여부, 최초 입장 조건, 전투 중 소모품·부활 비용, 체력·적·스킬 재사용 시간·제한 시간의 재설정과 보상·기록 인정은 별도 확인한다.

## 확인된 던전 변화와 경쟁의 관계

사용자는 무료 재도전을 선택하면서 **재화 소모 → 던전 패널티 추가 + 보상 강화**의 던전 변화 시스템을 제안했다. 이 도입 방향은 [DEC-0060](../Decisions/DEC-0060-currency-funded-dungeon-penalties-and-better-rewards.md)에서 확인했다.

던전 변화는 **파밍에만 적용**하고, 최고 도달 단계 경쟁에는 적용하지 않으며 **공통 도전 조건을 유지**한다. 사용자는 경쟁에도 변화를 허용하는 대안과 비교해 이 1안을 선택했다. 확인 근거는 [DEC-0061](../Decisions/DEC-0061-dungeon-modification-for-farming-only.md)에 기록했다.

파밍에서 얻은 장비·재료를 제작과 빌드 개선에 활용하고, 그 빌드의 경쟁 성과는 공통 도전 조건에서 비교한다. 공통 조건의 세부 내용과 장비·스킬 외 성장 차이의 취급은 별도 확인한다. 캐릭터 능력치의 정규화나 장비 통일을 확정한 것은 아니다.

파밍 던전의 패널티는 후속 [DEC-0062](../Decisions/DEC-0062-randomly-assign-farming-dungeon-penalties.md)에서 무작위로 부여하는 것으로 확인했다. 재추첨은 [지정한 한 줄만 무작위 교체](../Decisions/DEC-0064-reroll-one-selected-dungeon-penalty.md)하며 [각 줄 우측에 잠금 토글](../Decisions/DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md)을 둔다. [잠금 해제는 최대 한 줄이며 대상 전환 시 기존 줄은 자동 잠금](../Decisions/DEC-0066-allow-only-one-unlocked-dungeon-penalty-row.md)으로 전환한다. [교체한 새 결과는 빌드에 더 불리해져도 바로 적용](../Decisions/DEC-0067-apply-new-dungeon-penalty-result-directly.md)한다. [패널티 교체 실행마다 재화를 소모](../Decisions/DEC-0068-consume-currency-for-each-dungeon-penalty-replacement.md)한다. [장비 옵션 교체의 기본 재료를 패널티 교체와 공유](../Decisions/DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md)한다. [같은 조건에서는 반복 횟수에 따른 교체 비용 증가를 두지 않는다](../Decisions/DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md). [패널티 교체에 별도 횟수 제한을 두지 않는다](../Decisions/DEC-0073-no-attempt-limit-for-dungeon-penalty-replacement.md). [파밍 성공 후 패널티와 연결된 보상 강화 설정을 초기화](../Decisions/DEC-0074-reset-farming-dungeon-modifiers-after-successful-clear.md)한다. [파밍 실패 후에도 패널티와 연결된 보상 강화 설정을 초기화](../Decisions/DEC-0075-reset-farming-dungeon-modifiers-after-failure.md)한다. [실패한 도전의 패널티 교체에 이미 쓴 재료는 환급하지 않는다](../Decisions/DEC-0076-no-refund-of-dungeon-penalty-replacement-materials-after-failure.md). [실패 후 같은 파밍 대상에 새 도전을 허용하고 입장 자체에는 별도 비용을 두지 않는다](../Decisions/DEC-0077-allow-farming-retries-without-separate-entry-cost.md). [최초 기본 패널티들을 한 번에 무작위 부여](../Decisions/DEC-0078-initial-farming-dungeon-penalties-generated-as-one-random-batch.md)한다. [최초 패널티 개수는 효과 부여에 사용하는 재화에 따라 무작위 결정](../Decisions/DEC-0082-currency-dependent-random-count-for-initial-dungeon-penalties.md)한다. [최초 패널티 부여에는 재화 2종을 사용](../Decisions/DEC-0083-two-currency-types-for-initial-dungeon-penalty-generation.md)한다. [최초 부여 재화 2종은 장비 제작 기본 재료 4종 중에서 골라 공유](../Decisions/DEC-0085-share-two-equipment-crafting-materials-with-initial-dungeon-penalty-generation.md)한다. [최초 부여에 공유할 두 재료는 옵션 추가·교체의 기본 재료](../Decisions/DEC-0086-use-affix-addition-and-replacement-materials-for-initial-dungeon-penalties.md)로 확인했다. [최초 부여 개수 범위는 추가 재료 1~2개·교체 재료 3~4개](../Decisions/DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md)로 확인했다. [각 재료의 두 개수는 각각 50%로 추첨](../Decisions/DEC-0089-initial-dungeon-penalty-generation-rules.md)한다. 현행 규칙은 [파밍 던전 변화 기획서](../Systems/Farming-Dungeon-Modification.md)에 모았으며, [던전 준비·변경 기본 동작 묶음](../Decisions/DEC-0090-farming-dungeon-preparation-and-modification-rules.md)을 확인했다. [패널티·보상 콘텐츠 묶음](../Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md)을 확인했다. [파밍 수급·정산 묶음](../Decisions/DEC-0094-farming-dungeon-supply-settlement-and-resume.md)을 확인했다. [장비 득템·파밍 대상 묶음](../Decisions/DEC-0095-equipment-drops-and-farming-targets.md)을 확인했고 현행 규칙은 [기능 기획서](../Systems/Equipment-Drops-and-Farming-Targets.md)에 모았다. [장비 편성·기반 구조 묶음](../Decisions/DEC-0096-equipment-catalog-and-base-structure.md)을 확인했고 현행 목록은 [장비 구성 기획서](../Systems/Equipment-Catalog-and-Base-Structure.md)에 모았다. [옵션·전투 수치표 묶음](../Decisions/DEC-0097-equipment-affixes-base-stats-and-combat-numbers.md)을 확인했고 현행 데이터는 [기능 기획서](../Systems/Equipment-Affixes-and-Combat-Numbers.md)에 모았다. 제작 실행·비용·확률·종료는 [DEC-0098](../Decisions/DEC-0098-crafting-execution-costs-odds-and-recovery.md)에서 확인했고 [기본 제작 기획서](../Systems/Equipment-Crafting.md)에 모았다. 장비 보관·비교·교체·분해는 [DEC-0100](../Decisions/DEC-0100-equipment-inventory-comparison-and-salvage.md)에서 확인했고 [장비 관리 기획서](../Systems/Equipment-Inventory-Comparison-and-Salvage.md)에 통합했다. [DEC-0102](../Decisions/DEC-0102-initial-crafting-scope-without-extra-special-crafting.md)에서 첫 제작은 기본 4종과 집중석부터 검증하는 A안으로 확인했다. 고유 공통 규칙은 [DEC-0104](../Decisions/DEC-0104-unique-equipment-with-multiple-equipped-items.md)의 2안(B)으로 확인했고 [기능 기획서](../Systems/Unique-Equipment-Role-Acquisition-and-Handling.md)에 통합했다. 첫 고유 효과·수치·중복과 빌드 검증 목표는 [DEC-0105](../Decisions/DEC-0105-first-unique-effects-stacking-and-build-goals.md)에서 확인했고 [고유 기획서](../Systems/Unique-Equipment-Role-Acquisition-and-Handling.md)에 통합했다. 후속 정식 스킬·젬 성장과 콘텐츠는 [기획 순서](../01-Decision-Queue.md)에서 확인한다. 파밍의 무료·무제한 반복 입장과 보상·재료 소모·종료·재접속은 [DEC-0094](../Decisions/DEC-0094-farming-dungeon-supply-settlement-and-resume.md)을 따른다. 첫 장비·옵션 후보는 확정 기획서를 따르며 구간별 실제 전투 구성과 다른 모드의 수급·정산은 후속 확인 사항이다. 파밍의 무료 재도전 입장은 경쟁과 별도로 사용자 확인을 기록했다.

## 후속 확인 범위

도전 조건과 장비·스킬 외 캐릭터 성장 차이의 취급, 측정 구간과 입장·재도전 조건은 별도 확인한다. 같은 도전에서 비교한다는 결정만으로 캐릭터 능력치의 정규화나 특정 성장 요소의 배제를 확정하지 않는다.

순위표 형식, 시즌·초기화·보상, 직접 PvP·매칭과 거래소도 미정이다. 보조 장비 점수나 다른 경쟁 지표의 동시 제공은 별도 확인한다. 특정 게임의 경쟁 규칙이나 실제 수치를 도입하지 않는다.

## 검증 계획

경쟁의 공통 도전 조건과 재도전 초기화 등 남은 사항을 확인받은 뒤 서로 다른 장비·스킬 조합의 사례를 만들고, 실패한 단계에서 재도전하며 단계별 제한 시간 안에서 제작으로 바뀐 옵션과 최고 도달 단계의 차이를 설명할 수 있는지 검토한다. 평가 조건과 수치를 합의한 뒤에 실제 전투 실험이나 점수 비교를 수행한다. 현재는 제안 문서만 작성하며 경쟁 시스템이나 평가 수치를 구현하지 않는다.

- 연결: [현재 방향](../00-Concept.md), [기획 순서](../01-Decision-Queue.md), [제작 중심 제안](Crafting-Endgame.md)
