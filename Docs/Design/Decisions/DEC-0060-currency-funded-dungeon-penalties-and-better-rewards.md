---
id: "DEC-0060"
title: "재화로 던전 패널티와 보상을 높이는 방향"
layer: 1
status: "approved"
date: "2026-11-17"
depends_on: ["DEC-0006", "DEC-0007"]
approval: {"by": "user", "date": "2026-11-17", "evidence": "사용자: 1로 가되, poe의 맵 모딩처럼 던전 변화 시스템을 통해 재화를 소모해 던전에 패널티 추가 + 보상 업그레이드 기획이 들어가면 좋을듯?"}
---

# 재화로 던전 패널티와 보상을 높이는 방향

PoE의 맵 모딩을 참고하여 **재화를 소모해 던전에 패널티를 추가하고 보상을 높이는 던전 변화 시스템**을 기획에 포함한다.

## 확인 근거와 범위

사용자는 무료 재도전 1안을 선택하면서 던전 변화 시스템을 통해 재화를 소모하고 패널티 추가와 보상 업그레이드를 연결하는 기획을 요청했다. 이번 확인은 이 시스템의 도입 방향까지다.

적용 범위는 후속 [DEC-0061](DEC-0061-dungeon-modification-for-farming-only.md)에서 파밍에만 적용하고 최고 단계 경쟁은 공통 조건을 유지하는 방향으로 확인했다. 부여 방식은 후속 [DEC-0062](DEC-0062-randomly-assign-farming-dungeon-penalties.md)에서 플레이어가 고르지 않는 무작위 부여로 확인했다. 재추첨 범위는 후속 [DEC-0064](DEC-0064-reroll-one-selected-dungeon-penalty.md)에서 지정한 한 줄만 무작위 교체하고 나머지를 보존하는 것으로, 조작 방향은 [DEC-0065](DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md)에서 각 줄 우측 잠금 토글로 확인했다. 잠금과 교체 대상의 연동 방식 및 패널티의 종류·개수·중첩·추첨 확률·삭제·재추첨 비용과 횟수 등은 별도로 확인한다. 보상을 더 많이 주는 방식과 더 좋은 보상을 주는 방식도 아직 선택하지 않았다.

재화의 종류·소모량·소모 시점·환급, 변화의 지속 범위와 재도전 시 유지·재소모, 보상 수치·지급 시점·실패 시 보상, 기록 인정·비교 조건은 미정이다. 무료 재도전 입장 원칙은 [DEC-0059](DEC-0059-no-separate-entry-cost-for-competition-retries.md)에 따로 기록한다.

PoE의 실제 맵 아이템·통화·옵션·아틀라스·입장 제한과 장비 제작 규칙을 던전 변화에 통째로 도입하지 않는다. 보상 강화만으로 장비 성급의 획득 구간이나 성급별 옵션 등급 허용 범위를 바꾸지 않는다. 이 결정은 기획 방향 기록이며 경쟁·던전 변화 코드의 구현 범위를 추가하지 않는다.

## 연결

- 전제: [라이트한 PoE](DEC-0006-light-poe-vision.md), [종결 장비 제작 중심](DEC-0007-endgame-crafting.md)
- 관련: [재도전 입장 자체의 별도 비용 없음](DEC-0059-no-separate-entry-cost-for-competition-retries.md), [최고 도달 단계 지표](DEC-0054-highest-stage-as-primary-competition-metric.md)
- 조사: [맵 모딩의 설계 의도와 커뮤니티·오픈소스 사례](../../Research/2026-11-17-dungeon-modification.md)
- 제안: [던전 변화와 패널티 부여 방식](../Proposals/Dungeon-Modification.md)
