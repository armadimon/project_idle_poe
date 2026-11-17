---
id: "DEC-0068"
title: "패널티 교체 실행마다 재화 소모"
layer: 1
status: "approved"
date: "2026-11-17"
depends_on: ["DEC-0064"]
approval: {"by": "user", "date": "2026-11-17", "evidence": "패널티 교체 비용에서 1안 교체할 때마다 재화 소모, 2안 교체 자체는 무료를 비교한 뒤 사용자 답변: 1. 재화 종류·소모량·횟수 제한은 별도 확인한다고 명시한 질문에 대한 선택이다."}
---

# 패널티 교체 실행마다 재화 소모

파밍 던전의 **패널티 한 줄을 교체할 때마다 재화를 소모**한다.

## 확인 근거와 범위

사용자는 1안 교체할 때마다 재화 소모, 2안 교체 자체는 무료 중 1안을 선택했다. 사용자 답변은 “1”이다. 재화 종류·소모량·횟수 제한은 별도로 확인한다고 명시한 질문에 대한 선택이다.

이번 결정은 패널티 교체 실행마다 재화를 소모하는 원칙까지다. 사용할 재료는 후속 [DEC-0070](DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md)에서 장비 옵션 교체의 기본 재료와 공유하는 것으로 확인했다. 후속 [DEC-0071](DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md)에서 같은 조건에서는 반복 횟수에 따른 비용 증가를 두지 않는 것으로 확인했다. 재료 이름·실제 소모량·공급과 교체 횟수 제한·실행 조건·실제 차감 처리 시점·취소·환급은 별도로 확인한다. 서로 다른 던전 조건 사이의 동일 비용이나 결과의 유불리에 따른 소모량 차이는 이번 결정으로 정하지 않는다.

최초 패널티 부여 등 다른 던전 변화 작업의 비용이나 잠금 조작에 따른 비용 변화를 함께 확정하지 않는다. 파밍 실패 후 재시도 조건과 변화 유지·재소모, 보상 강화의 종류·수치·지급 조건도 미정이다.

기존에 확인한 한 줄 교체·나머지 보존, 줄 우측 잠금 체크박스, 최대 한 줄만 잠금 해제와 대상 전환 시 기존 줄 자동 잠금, 새 결과 즉시 적용은 유지한다. 던전 변화는 파밍에만 적용하며 경쟁 재도전 입장 자체의 별도 비용 없음은 유지한다.

이번 기록에는 재화 수치·경제 밸런스·기능·화면 구현이나 실제 파밍 실험을 추가하지 않는다.

## 연결

- 전제: [지정한 패널티 한 개만 무작위 교체](DEC-0064-reroll-one-selected-dungeon-penalty.md)
- 관련: [새 교체 결과 즉시 적용](DEC-0067-apply-new-dungeon-penalty-result-directly.md), [재화를 소모하는 던전 변화 방향](DEC-0060-currency-funded-dungeon-penalties-and-better-rewards.md)
- 제안: [던전 변화와 교체 횟수 제한](../Proposals/Dungeon-Modification.md)
- 반영: [현재 방향](../00-Concept.md), [기획 순서](../01-Decision-Queue.md), [제작 중심 제안](../Proposals/Crafting-Endgame.md)
