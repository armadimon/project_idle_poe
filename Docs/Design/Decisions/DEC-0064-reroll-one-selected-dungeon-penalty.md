---
id: "DEC-0064"
title: "지정한 패널티 한 개만 무작위 교체"
layer: 1
status: "approved"
date: "2026-11-17"
depends_on: ["DEC-0062"]
approval: {"by": "user", "date": "2026-11-17", "evidence": "사용자 원문: 2번으로 하고, 간단하게 페널티 줄 우측에 잠금 버튼 체크박스 토글로 하면 단순할듯. 앞선 2안은 바꿀 패널티 하나를 지정해 무작위로 교체하고 나머지를 보존하는 범위이며 비용·횟수·새 결과 적용 방식은 별도 확인한다고 제시했다."}
---

# 지정한 패널티 한 개만 무작위 교체

파밍 던전의 패널티 중 **바꿀 한 개를 플레이어가 지정해 무작위로 교체하고 나머지는 보존**한다.

## 확인 근거와 범위

사용자는 1안 전체 무작위 재추첨, 2안 하나를 지정해 무작위 교체, 3안 재추첨 없음 중 2안을 선택했다. 같은 답변에서 각 패널티 줄 우측의 잠금 체크박스 토글을 제안했으며, 그 조작 방향은 [DEC-0065](DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md)에 따로 기록한다.

이번 결정은 한 개 교체와 나머지 보존까지다. 연동 방식은 후속 [DEC-0066](DEC-0066-allow-only-one-unlocked-dungeon-penalty-row.md)에서 최대 한 줄만 잠금 해제하고 다른 줄을 해제하면 기존 줄을 자동 잠금하는 것으로 확인했다. 결과 적용은 후속 [DEC-0067](DEC-0067-apply-new-dungeon-penalty-result-directly.md)에서 새 결과를 즉시 적용하는 것으로 확인했다. 기본 잠금 상태·전체 잠금 처리와 재추첨 비용·횟수·소모 시점·실행 조건·보상 변화는 별도로 확인한다. 종류·수치의 상세 추첨과 동일 패널티 재등장·중복·취소·환급도 미정이다.

후속 DEC-0066은 한 줄 교체 범위를 유지한다. 여러 줄을 한꺼번에 교체하는 구성은 채택하지 않았다.

던전 변화는 파밍에만 적용하고 최고 도달 단계 경쟁은 공통 조건을 유지한다. 이 결정에는 기능·수치·화면 구현을 추가하지 않는다.

## 연결

- 전제: [파밍 던전의 패널티는 무작위 부여](DEC-0062-randomly-assign-farming-dungeon-penalties.md)
- 관련: [각 패널티 줄 우측의 잠금 토글](DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md)
- 제안: [던전 변화의 잠금 토글과 교체 대상](../Proposals/Dungeon-Modification.md)
- 반영: [현재 방향](../00-Concept.md), [기획 순서](../01-Decision-Queue.md), [제작 중심 제안](../Proposals/Crafting-Endgame.md)
