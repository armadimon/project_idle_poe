---
id: "DEC-0083"
title: "최초 패널티 부여에 사용할 재화는 2종"
layer: 1
status: "approved"
date: "2026-11-18"
depends_on: ["DEC-0082"]
approval: {"by": "user", "date": "2026-11-18", "evidence": "효과 부여에 사용할 재화 종류 수를 1안 2종으로 시작, 2안 3종으로 시작으로 비교한 뒤 사용자 답변: 1. 각 재화의 개수 범위·확률과 기존 제작 재료 공유 여부는 별도로 확인한다고 명시한 질문에 대한 선택이다."}
---

# 최초 패널티 부여에 사용할 재화는 2종

파밍 던전의 **최초 패널티 부여에 사용할 재화는 2종으로 시작**한다. 사용하는 재화에 따라 패널티 개수를 무작위로 결정하는 기존 원칙을 유지한다.

## 확인 근거와 범위

사용자는 1안 2종으로 시작, 2안 3종으로 시작 중 1안을 선택했다. 사용자 답변은 “1”이다. 각 재화의 개수 범위·확률과 기존 제작 재료 공유 여부는 별도로 확인한다고 명시한 질문에 대한 선택이다.

이번 결정은 최초 부여에 사용할 재화 종류 수까지다. 후속 [DEC-0085](DEC-0085-share-two-equipment-crafting-materials-with-initial-dungeon-penalty-generation.md)에서 장비 제작 기본 재료 4종 중 2종을 골라 공유하는 것으로 확인했다. 구체적인 두 재료는 후속 [DEC-0086](DEC-0086-use-affix-addition-and-replacement-materials-for-initial-dungeon-penalties.md)에서 옵션 추가·교체의 기본 재료로 확인했다. 최초 부여 개수 범위는 후속 [DEC-0088](DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md)에서 추가 재료 1~2개·교체 재료 3~4개로 확인했다. 이름·개수별 확률·전체 상한·소모량·공급과 보상 강화 규칙은 별도로 확인한다.

두 종류라는 이유로 가격·희소성·성능의 등급 순서나 한 재화가 항상 더 많은 패널티를 만든다는 규칙을 확정하지 않는다. 기존 장비 제작 기본 재료 4종과 별도 통제 재료를 변경하거나, 장비 옵션 교체 재료를 쓰는 패널티 교체의 비용 규칙을 바꾸는 결정도 아니다.

최초 패널티 일괄 부여와 한 줄 교체·나머지 보존, 성공·실패 후 설정 초기화, 실패 시 교체 재료 환급 없음과 파밍 재도전 입장 자체의 별도 비용 없음은 유지한다.

이번 기록은 기획 문서 반영까지다. 재화·개수 추첨 기능이나 실제 수치를 구현하지 않았으며 확률·난도·경제 실험은 수행하지 않았다.

## 연결

- 전제: [최초 패널티 개수는 부여 재화에 따라 무작위 결정](DEC-0082-currency-dependent-random-count-for-initial-dungeon-penalties.md)
- 관련: [장비 제작 기본 재료 4종](DEC-0038-dedicated-basic-materials-for-each-crafting-operation.md), [패널티 교체 재료 공유](DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md)
- 제안: [던전 변화와 최초 부여 개수별 확률](../Proposals/Dungeon-Modification.md)
- 반영: [현재 방향](../00-Concept.md), [기획 순서](../01-Decision-Queue.md), [제작 중심 적용 제안](../Proposals/Crafting-Endgame.md)
