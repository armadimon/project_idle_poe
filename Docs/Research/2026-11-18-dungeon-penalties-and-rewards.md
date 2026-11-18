# 파밍 던전 패널티·보상 콘텐츠 조사

확인일: 2026-11-18. 준비·변경 묶음 DEC-0090 승인 후 다음 콘텐츠 제안을 위한 문헌 조사다. 출처를 읽은 결과와 우리 게임의 미승인 제안, 실제 실행 검증을 구분한다.

## 확인한 출처와 버전

| 출처 | 이번에 확인한 내용과 시점 | 적용 한계 |
| --- | --- | --- |
| [PoEDB Maps](https://poedb.tw/us/Maps) | 열람일의 동적 데이터와 Community Wiki의 모디파이어·보상 수량 설명 | Watchstone·Sextant 등 과거 설명이 섞여 있다. 단일 최신 패치의 전체 사양·정확한 현행 수치로 채택하지 않음 |
| [GGG Stories from Development: The Map System](https://www.pathofexile.com/forum/view-thread/2071848) | 2018년 개발 회고. 2012년 논의와 0.9.11 도입 배경에서 투자 비용·지역 위험·보상을 연결한 과정을 설명 | 역사적 설계 의도이며 현행 게임 규칙·우리 게임의 경제 수치를 검증하는 자료가 아님 |
| [Pohx RF FAQ](https://pohx.net/faq/) | 맵 옵션 회피 항목의 표시 갱신일 2026-11-11. 특정 빌드에서 회복 저하·회복 차단 등의 회피 필요성을 설명 | 작성자의 해당 빌드 공략이며 모든 빌드에 동일한 위험 순위를 부여하는 자료가 아님. 페이지 표시 날짜와 게임 패치 버전을 구분 |
| [PathOfExileBuilds: Best build for not caring about map mods?](https://www.reddit.com/r/PathOfExileBuilds/comments/1vomwre/best_build_for_not_caring_about_map_mods/) | 직접 게시물에서 회복 수단을 다변화하거나 특정 의존도를 줄이는 대응을 확인 | 개인 사례이며 완주율·보상 수급의 통계가 아님. 검색 결과의 절대 날짜와 본문 상대 날짜가 달라 정확한 게시일은 이번 조사로 확정하지 않음 |

## 조사에서 얻은 설계적 해석

비용을 투자해 더 큰 위험과 획득 기회를 선택하는 구조를 참고할 수 있다. 빌드의 회복·공격 수단 의존도가 다르면 같은 패널티의 부담이 달라질 수 있다는 해석은 커뮤니티 사례에 근거한 설계 판단이다. 이것이 우리 게임의 모든 패널티 조합이나 실제 수치의 적정성을 검증한 결과는 아니다.

라이트한 PoE의 초기 콘텐츠로 기능을 완전히 차단하는 효과보다 고정 비율의 약화와 강화에 집중하고, 장비·제작재료 획득 기회를 줄 수에 연결하는 안을 제안한다. 6종·각 고정 수치·중복 금지·동일 추첨 확률·한 줄당 추가 추첨 확률 20%p와 성공 정산은 우리 게임을 위한 자체 설계이며 후속 [DEC-0092](../Design/Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md)에서 사용자 승인을 기록했다. 원본 게임의 효과 이름·문장·수치·확률·보상 공식을 복사한 것이 아니다.

## 오픈소스·호환성·라이선스

관련 오픈소스 poe.re의 확인 커밋, React/Vite 버전·AGPL 및 별도 데이터 라이선스·Unity 직접 호환 불가와 재사용 제약은 [기존 맵 모딩 조사](2026-11-17-dungeon-modification.md)에 기록되어 있다. 그 도구는 맵 조건을 정리하는 사례로 참고하며 이번 제안에 새 라이브러리나 코드를 도입하지 않는다.

PoEDB Community Wiki에 표시된 CC BY-NC-SA 3.0을 PoEDB 데이터·GGG 텍스트·게임 이미지 전체의 제품 재사용 허락으로 확대하지 않는다. GGG·Pohx·게시물의 원문·이미지와 게임 데이터도 제품에 복사하지 않는다. 외부 자료는 출처 링크와 자체 요약으로 기록하며 콘텐츠와 데이터는 자체 작성한다.

이번 변경은 Unity와 결합할 외부 라이브러리를 선정하거나 설치하는 작업이 아니다. 호환성 판단은 기존 도구의 기술 구성을 문서로 확인한 수준이며 실제 설치·실행·PoE 클라이언트 플레이·Unity 검증을 수행하지 않았다.

## 적용 범위와 검증 계획

준비·변경은 [DEC-0090](../Design/Decisions/DEC-0090-farming-dungeon-preparation-and-modification-rules.md), 패널티·보상 콘텐츠는 후속 [DEC-0092](../Design/Decisions/DEC-0092-farming-dungeon-penalties-and-bonus-drops.md)에서 사용자 확인을 기록하고 [현행 기획서](../Design/Systems/Farming-Dungeon-Modification.md)에 통합했다. 다음 [파밍 수급·정산 제안](../Design/Proposals/Dungeon-Modification.md)은 미승인 상태로 구분한다.

콘텐츠 규칙은 승인되었으나 이번 변경은 문서 반영까지이며 실제 실행은 미검증이다. 구현 승인 후 종류 추첨의 중복 방지·같은 결과 재등장·개수 보존, 추가 추첨의 기대량·비재귀·성공 정산을 검증한다. 정식 빌드와 수급을 정한 뒤 완주 성과·재료 순소비·시간당 획득·특정 패널티 회피 비용을 비교한다. 현재 완료한 범위는 문헌 열람과 제안 작성이다.
