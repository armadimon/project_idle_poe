# PoE 1 조사 출처와 확인 범위

확인일은 2026년 11월 13일이다. GGG 자료는 규칙과 패치의 공식 근거로, PoEDB는 개별 데이터와 버전 기록을 조회하는 자료로, 제작자·이용자의 글은 공략 작성과 문제 해결의 당사자 기록으로 사용했다.

## 규칙과 데이터

| 출처 | 확인한 부분 | 버전과 범위 |
| --- | --- | --- |
| [GGG 게임 소개](https://www.pathofexile.com/game) | 젬·보조 젬, 패시브와 핵심 노드 | 일반 구조 설명. 세부 변경은 패치와 대조 |
| [GGG 아이템 소개](https://www.pathofexile.com/item-data) | 기반 아이템과 접두·접미 옵션 | 일반 구조 설명 |
| [GGG 3.29 패치](https://www.pathofexile.com/forum/view-thread/3985332) | Gem Socket Changes와 Dialla 변경 | 3.29.0 공식 규칙 변경 |
| [GGG 3.30 패치](https://www.pathofexile.com/forum/view-thread/4013680) | 공식 패치 노트 공개와 버전 | 공지 확인. 출시 이후 빌드 성능 검증은 아님 |
| [PoEDB 홈페이지](https://poedb.tw/kr/) | 표시 버전 | 열람 시 3.30 표시 |
| [PoEDB 옵션](https://poedb.tw/us/Modifiers) | 아이템 종류별 옵션과 적용 범위 | 열람 시점의 동적 페이지 |
| [PoEDB CoC](https://poedb.tw/us/Cast_On_Critical_Strike_Support) | 발동 조건과 보조 제한 | 열람 시점의 개별 젬 데이터 |
| [PoEDB 성유물](https://poedb.tw/us/Summon_Holy_Relic_of_Conviction) | 공격 명중과 소환수 주문의 관계, 퀄리티 | 열람 시점 데이터. 소환 스킬과 소환수 행동을 구분 |
| [PoEDB Dialla](https://poedb.tw/us/Diallas_Malefaction) | 소켓별 효과와 3.29 변경 기록 | 상단 데이터와 하단 Community Wiki의 역사 설명을 구분 |
| [PoEDB Darkness Enthroned](https://poedb.tw/us/Darkness_Enthroned) | 장착한 주얼 효과의 변화 | 아이템과 다른 부품의 상호작용 사례 |
| [PoEDB Olroth](https://poedb.tw/us/Olroths_Resolve) | Ward 조건과 3.25 변경 기록 | 과거 Wardloop와 현재 데이터 혼합 금지 |
| [PoEDB RF](https://poedb.tw/us/Righteous_Fire) | 자기 피해와 주변 피해의 연결 | 현재 데이터는 과거 공략 수치를 입증하지 않음 |

## 공략과 문제 해결 기록

| 출처 | 확인한 기록 | 열람 범위와 제한 |
| --- | --- | --- |
| [BalorMage FAQ](https://www.poe-vault.com/guides/balormage-holy-relic-necromancer-faq) | 시작 구성, 중독 확률, 임계점, 질문별 진단 | 본문 확인. 표시 갱신일 2026-11-12, 3.30 표기와 과거 패치 설명 포함 |
| [성유물 교체 경로](https://www.reddit.com/r/PathOfExileBuilds/comments/1can751/what_does_the_holy_relic_upgrade_path_look_like/) | 작성자의 부위별 교체와 다른 사용자의 보완 의견 | 본문·댓글 확인. 정확한 게시일은 연구에서 단정하지 않음 |
| [성유물 임계점 계산 질문](https://www.reddit.com/r/PathOfExileBuilds/comments/1chmfle) | 2024-05-01 본문, 수정 내용과 틱 관련 답변 | 검색 도구가 제공한 원문·댓글 확인. 직접 페이지와 JSON 열람은 실패했으므로 스레드 전체를 검토했다고 주장하지 않음 |
| [성유물 경험 토론](https://www.reddit.com/r/PathOfExileBuilds/comments/1ohfkib/holy_relic_necromancer_your_experience_with_the/) | 2025-10-27의 패시브·FAQ 갱신 토론 | 본문·관련 댓글 확인. 날짜는 검색 도구가 제공한 댓글 시각과 대조 |
| [성유물 방어 문제 해결](https://www.reddit.com/r/PathOfExileBuilds/comments/1vmcois/holy_relic_helpquestions/) | 2026-08-12 잘못 선택한 Offering 확인 | 질문·답변과 사용자 확인을 열람 |
| [Akshay Wardloop 공략](https://www.pathofexile.com/forum/view-thread/3261066) | 작동 원리, 계산기, 실패 점검, 버전·예산별 PoB | 3.26 표기. 작성 2022-04-04, 수정 2025-06-22. 다른 패치의 항목이 함께 남음 |
| [RF 커뮤니티 진단](https://www.reddit.com/r/PathOfExileBuilds/comments/1f7w0z6/psa_senior_citizens_and_newbies_playing_righteous/) | 2024-09-03 기초 조건과 공격 전환, 댓글 반영 | 본문·관련 댓글 확인. 당시 작성자의 조언으로 취급 |
| [Pohx의 RF 자료](https://pohx.net/) | 시작 구성과 변형, 과거 자료 구분 | 홈페이지 본문 확인. 3.30, 2026-11-12 갱신 표기. 연결 영상의 내용은 검증하지 않음 |

## 오픈소스 계산 도구

| 출처 | 확인한 버전과 부분 | 재사용 가능성과 제약 |
| --- | --- | --- |
| [Path of Building Community](https://github.com/PathOfBuildingCommunity/PathOfBuilding) | [v2.67.2](https://github.com/PathOfBuildingCommunity/PathOfBuilding/releases/tag/v2.67.2), [발동 계산](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/v2.67.2/src/Modules/CalcTriggers.lua), [라이선스](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/v2.67.2/LICENSE.md) | 프로젝트 코드는 MIT, 포함 구성요소는 개별 조건. Lua·PoE 전용 데이터 기반이므로 Unity 직접 호환 없음. 모듈 분리와 계산 근거 추적을 참고할 수 있으나 설치·실행·포팅하지 않음 |

PoEDB 하단의 Community Wiki 영역에는 CC BY-NC-SA 3.0 표기가 있으며 페이지의 다른 자료까지 같은 허락이라고 추정하지 않는다. 이 저장소에는 출처 링크와 자체 조사 요약을 남긴다. 자료 조사와 코드 라이선스 확인은 PoE의 문구·아트·게임 데이터를 제품에 포함하기로 한 결정이 아니다.
