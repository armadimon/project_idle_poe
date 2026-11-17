---
id: "DEC-0073"
title: "패널티 교체에 별도 횟수 제한 없음"
layer: 1
status: "approved"
date: "2026-11-17"
depends_on: ["DEC-0064", "DEC-0068", "DEC-0071"]
approval: {"by": "user", "date": "2026-11-17", "evidence": "패널티 교체 횟수를 1안 별도 횟수 제한 없음, 2안 횟수 제한 적용으로 비교한 뒤 사용자 답변: 1. 1안은 재료를 소모하며 계속 교체할 수 있다는 범위이고 실제 소모량과 제한 횟수·집계 범위는 별도 확인한다고 명시한 질문에 대한 선택이다."}
---

# 패널티 교체에 별도 횟수 제한 없음

파밍 던전의 패널티 교체에는 **별도 횟수 제한을 두지 않는다**. 매번 필요한 재료와 실행 조건을 충족하면 계속 교체할 수 있다.

## 확인 근거와 범위

사용자는 1안 별도 횟수 제한 없음, 2안 횟수 제한 적용 중 1안을 선택했다. 사용자 답변은 “1”이다. 재료를 소모하며 계속 교체할 수 있는 안을 선택한 것으로 기록한다.

이번 결정은 패널티 교체에 별도 횟수 한도를 두지 않는 범위다. 실제 재료 이름·소모량·공급과 다른 실행 조건·실제 차감 처리 시점은 별도로 확인한다.

교체 실행마다 장비 옵션 교체의 기본 재료를 소모하며, 같은 조건에서는 반복 횟수가 늘어도 한 번의 비용을 유지한다. 한 줄 무작위 교체·나머지 보존·새 결과 즉시 적용도 유지한다.

성공 후 설정의 처리는 후속 [DEC-0074](DEC-0074-reset-farming-dungeon-modifiers-after-successful-clear.md)에서 클리어 시 패널티와 연결된 보상 강화 설정을 초기화하는 것으로 확인했다. 자동 연속 교체, 파밍 입장·재시도 횟수, 나머지 설정 유지 범위·실패 후 유지와 변경 가능 여부, 취소·되돌리기·환급, 보상 강화의 종류·수치·지급 조건은 별도로 확인한다. 던전 변화는 파밍에만 적용하고 최고 단계 경쟁의 공통 도전 조건은 유지한다.

이번 기록은 기획 문서 반영까지다. 실제 소모량·경제 밸런스·던전 변화 기능을 구현하거나 파밍 실험을 수행하지 않았다.

## 연결

- 전제: [패널티 한 개 교체](DEC-0064-reroll-one-selected-dungeon-penalty.md), [교체 실행마다 재화 소모](DEC-0068-consume-currency-for-each-dungeon-penalty-replacement.md), [반복 횟수에 따른 비용 증가 없음](DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md)
- 관련: [장비 옵션 교체 재료와 공유](DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md)
- 제안: [던전 변화와 파밍 실패 후 설정 유지](../Proposals/Dungeon-Modification.md)
- 반영: [현재 방향](../00-Concept.md), [기획 순서](../01-Decision-Queue.md), [제작 중심 적용 제안](../Proposals/Crafting-Endgame.md)
