---
id: "DEC-0089"
title: "던전 최초 패널티 생성 규칙"
layer: 1
status: "approved"
date: "2026-11-18"
depends_on: ["DEC-0088"]
approval: {"by": "user", "date": "2026-11-18", "evidence": "개수별 확률을 1안 추가 재료의 1개·2개 각각 50% 및 교체 재료의 3개·4개 각각 50%, 2안 각 범위에서 적은 개수 70%·많은 개수 30%로 비교한 뒤 사용자 답변: 1. 재료 소모량과 보상 수치는 별도로 확인한다고 명시한 질문에 대한 선택이다. 기존 최초 부여 단위·재료·개수 범위는 연결한 선행 승인에 근거해 함께 정리한다."}
---

# 던전 최초 패널티 생성 규칙

최초 패널티 생성의 기존 승인 규칙과 이번에 확인한 개수별 확률을 기능 단위로 정리한다. 현행 기능 전체는 [파밍 던전 변화 기획서](../Systems/Farming-Dungeon-Modification.md)에서 확인한다.

## 확인된 규칙

| 항목 | 규칙 | 승인 근거 |
| --- | --- | --- |
| 작업 단위 | 한 번의 작업으로 최초 패널티들을 함께 무작위 생성 | [DEC-0078](../Decisions/DEC-0078-initial-farming-dungeon-penalties-generated-as-one-random-batch.md) |
| 사용하는 재료 | 기존 옵션 추가·교체 기본 재료 2종 공유 | [DEC-0085](../Decisions/DEC-0085-share-two-equipment-crafting-materials-with-initial-dungeon-penalty-generation.md), [DEC-0086](../Decisions/DEC-0086-use-affix-addition-and-replacement-materials-for-initial-dungeon-penalties.md) |
| 개수 범위 | 추가 재료는 1~2개, 교체 재료는 3~4개 | [DEC-0088](../Decisions/DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md) |
| 개수별 확률 | 추가 재료의 1개·2개는 각각 50%, 교체 재료의 3개·4개도 각각 50% | 이번 사용자 답변 |

## 이번 확인 근거와 범위

사용자는 1안 각 범위의 두 개수를 각각 50%로 추첨, 2안 적은 개수 70%·많은 개수 30% 중 1안을 선택했다. 사용자 답변은 “1”이다. 재료 소모량과 보상 수치는 별도로 확인한다고 명시한 질문에 대한 선택이다.

이번 답변으로 새로 확정한 내용은 최초 부여의 개수별 확률이다. 표의 다른 규칙은 선행 승인에 근거한다. 같은 재료를 쓴다는 이유로 패널티 종류·수치별 확률이나 장비 제작의 옵션 추첨 확률을 50%로 정하지 않는다. 실제 재료 소모량·공급·이름·실행 조건·보상 강화는 미정이다.

이후 지정한 한 줄 교체는 나머지 줄과 전체 개수를 보존한다. 최초 부여 후 추가 허용·전체 최대 개수·중복·패널티 없는 입장·최초 부여의 반복과 다른 변화 작업은 별도 확인 사항이다.

## 기록과 검증

사용자가 기능·개념 단위로 묶어 질문하고 기록하도록 요청했으므로 이후 연결된 세부 사항은 기능 묶음으로 제안하고 한 승인 기록에 모은다. 기존 승인 이력은 기능 기획서에서 연결한다.

이번 변경은 문서 정리까지다. 추첨 기능·실제 확률을 구현하거나 게임·경제 실험을 수행하지 않았다. 관련 기능을 승인받은 뒤 범위·확률 분포·한 줄 교체의 개수 보존과 재료 소비를 검증한다.

- 전제: [재료별 최초 개수 범위](DEC-0088-initial-dungeon-penalty-count-ranges-by-crafting-material.md)
- 기능 기획서: [파밍 던전 변화](../Systems/Farming-Dungeon-Modification.md)
- 후속 제안: [던전 준비·변경 규칙 묶음](../Proposals/Dungeon-Modification.md)
- 조사: [재화별 개수 생성](../../Research/2026-11-18-currency-dependent-dungeon-penalty-counts.md)
