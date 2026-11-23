# PoE 1 스킬·젬·빌드 계층 조사

**확인일 2026-11-23.** 사용자 요청은 PoE 원본을 면밀히 확인해 경량화한 스킬·젬 전체 기획과 조합 검증을 작성하는 것이다. [전체 초안](../Design/Proposals/Skill-Gems-and-Build-Diversity.md)과 [결과](../Design/Analysis/SkillGems/SUMMARY.md)를 함께 읽는다. 기존 [PoE 1 조사](PoE1/README.md)와 [11월 19일 조사](2026-11-19-skill-gem-links-growth-and-acquisition.md)를 확장했다.

## 조사 원칙과 버전

GGG의 공개 설명/공식 패치는 규칙의 공식 근거, PoEDB의 개별 젬은 데이터의 적용 관계, 공략 작성자와 이용자의 글은 빌드 제작·수정 과정의 당사자 기록으로 읽었다. 비공개 게임 소스 코드를 열람했다는 뜻이 아니다.

PoEDB 홈은 열람 시 **3.30, 3.30.0D 링크**를 표시했다. 개별 동적 페이지가 모두 같은 패치로 고정되거나 실제 클라이언트에서 검증됐다는 보장은 없다. 과거 공략과 현재 데이터를 합쳐 현재 성능으로 주장하지 않는다. 필요한 원리만 요약했고 외부 표·아트·아이콘·설명·코드를 제품 데이터로 반입하지 않았다.

## 원본 스킬/보조에서 확인한 계층

| 출처 · 열람 범위 | 확인한 관계 | 초안에서 남길 것과 차이 |
| --- | --- | --- |
| [GGG 게임 소개](https://www.pathofexile.com/game), Skill Gem System | 젬 아이템과 보조로 행동을 바꾸고 개별 성장 | 행동 조합과 개별 성장 유지. 실물/거래와 장비 소켓은 목록/3×2로 간소화 |
| [GGG 3.29.0 패치](https://www.pathofexile.com/forum/view-thread/3985332), Gem Socket Changes | 색 불일치 장착 허용과 일치 퀄리티 보너스로 변경 | 오래된 색상 강제 조건을 현재 규칙으로 오인하지 않음. 우리 게임 색 보너스 자동 도입 없음 |
| [PoEDB Fireball](https://poedb.tw/us/Fireball), 상단·Level Effect·퀘스트 | 기본 피해·요구치·경험치·퀄리티가 각각 다른 역할 | 성장, 요구치, 행동을 분리. 요구치를 레벨마다 올려 자동으로 빌드가 깨지는 방식은 생략 |
| [GMP](https://poedb.tw/us/Greater_Multiple_Projectiles_Support), 상단·성장 | 추가 투사체와 피해 감폭의 교환 | 단일 적 중복 제한으로 광역/단일 목표를 구분. 원본의 발사 수·수치 채택 아님 |
| [Chain](https://poedb.tw/us/Chain_Support), 상단·성장 | 도약 수·적중 손익과 적용 대상 | 군집 처리 변화. 관통과의 복잡한 우선순위 대신 첫 범위에서 배타적 경로 |
| [Returning Projectiles](https://poedb.tw/us/Returning_Projectiles_Support), 상단 | 귀환·귀환 중 감폭·관통의 관계 | 관통형의 왕복 빌드. 우리 모델의 고정 왕복 지연은 원본 규칙이 아님 |
| [Pierce](https://poedb.tw/us/Pierce_Support), 상단·지원 대상 | 한 투사체가 여러 적을 통과하는 방식 | 관통과 같은 적 반복 명중을 구분. 우리 첫 목록은 기본 관통 스킬을 이용 |
| [Multistrike](https://poedb.tw/us/Multistrike_Support), 상단 | 근접 반복·추가 반복 손익·지원 제외 대상 | 반복이 행동 시간을 차지하게 함. 우리의 추가 1회/65%는 자체 수치이며 원본과 다름 |
| [Spell Echo](https://poedb.tw/us/Spell_Echo_Support), 상단·지원 제외 | 반복 주문과 발동형 주문 등의 제한 | 공격 반복/주문 반복을 분리. 연동+반복으로 동작 손해를 지우는 조합 차단 |
| [Concentrated Effect](https://poedb.tw/us/Concentrated_Effect_Support), 상단 | 범위 손해와 범위 피해 증가 | 단일/군집 선택의 손익. 원본의 범위 효과와 우리 반경 배율을 동일 단위라고 주장하지 않음 |
| [Physical to Lightning](https://poedb.tw/us/Physical_to_Lightning_Support), 상단·튜토리얼 | 전환과 추가 피해는 별도 효과 | 전환된 성분과 원래 원소 정액을 분리. 첫 범위는 하나의 100% 전환, 추가 복제 없음 |
| [Chance to Bleed](https://poedb.tw/us/Chance_to_Bleed_Support), 상단 | 명중과 물리 지속 피해, 적용 조건 | 확률·이동 배율을 옮기지 않고 직접 물리 공격의 확정 출혈로 단순화 |
| [Combustion](https://poedb.tw/us/Combustion_Support), 상단 | 화염 명중·점화·저항 감소가 서로 구별됨 | 점화만 단순화. 원본의 저항 감소까지 자동 추가하지 않음 |
| [Cast on Critical Strike](https://poedb.tw/us/Cast_On_Critical_Strike_Support), 상단·Level Effect | 공격 치명타와 연결 주문, 제외 대상·재사용 | 사건/주체/재사용을 함께 정의. 우리 ‘치명 연동’은 다른 일반 직접 명중을 쓰는 자체 확장 |
| [CWDT](https://poedb.tw/us/Cast_when_Damage_Taken_Support), 상단·튜토리얼 | 피해 누적 조건·지원 젬 요구치 제한과 발동 | 준비 조건을 게임 안에 표시. 자기 비용으로 루프를 만들지 않도록 발동 깊이 제한 |
| [Lifetap](https://poedb.tw/us/Lifetap_Support), 상단 | 생명 비용과 버프/회복 관계 | 우리의 생명 4% 지불은 자체 수치. 마나를 생명으로 바꾸는 원본 전체 구조와 구분 |
| [Holy Relic of Conviction](https://poedb.tw/us/Summon_Holy_Relic_of_Conviction), 상단·퀄리티 | 플레이어 공격 명중과 소환수의 별도 주문/재사용 | 소환 주체와 플레이어 능력치 적용을 분리해야 함을 확인. 소환을 수치만 추가해 첫 목록에 끼워 넣지 않음 |
| [Righteous Fire](https://poedb.tw/us/Righteous_Fire), 상단 | 자기 소모·회복/저항과 외부 피해 성립의 관계 | 피해와 지속 가능성을 같이 비교. 우리 생명 지불은 피격/연동 원천으로 취급하지 않음 |

위 표는 동작 관계의 조사다. PoEDB 페이지 전체의 재배포 라이선스나 게임 콘텐츠의 재사용 허가를 확인한 것으로 취급하지 않는다. 게임 수치·아이콘·데이터 덤프를 복사하지 않았다. 세부 원본 수치는 기획에 반복 인용하지 않고 링크로 남겼다.

## 커뮤니티에서 빌드가 쌓이는 과정

| 당사자 기록 | 확인한 빌드 계층 | 이 프로젝트의 정보 요건 |
| --- | --- | --- |
| [Holy Relic 업그레이드 경로](https://www.reddit.com/r/PathOfExileBuilds/comments/1can751/what_does_the_holy_relic_upgrade_path_look_like/), 본문·관련 댓글 | 작성자가 부위별 단계와 젬/퀄리티·재사용 조건을 함께 설명. 댓글에서 제작·생존 선택을 보완 | 부품→조건 성립→성능 개선의 단계별 설명. 목록 제공만으로 빌드가 완성됐다고 간주하지 않음 |
| [Wardloop 작성자 공략](https://www.pathofexile.com/forum/view-thread/3261066), 목차·작동/수학/실패 진단 부분 | 3.26 표기, 과거 패치 자료도 포함. 비용·자기 피해·회복·재사용과 실패 점검을 함께 다룸 | 발동 조건, 비용과 회복, 재사용을 별도로 보여 주고 자동 루프의 깊이를 제한 |
| [RF 이용자 진단](https://www.reddit.com/r/PathOfExileBuilds/comments/1f7w0z6/psa_senior_citizens_and_newbies_playing_righteous/), 본문·관련 댓글 | 좋은 종결 아이템을 먼저 써도 회복/저항 등 준비가 부족하면 성립하지 않는다는 이용자 진단 | 현재 생존 가능 여부와 비용을 계산. ‘추천 고유’와 ‘지금 장착하면 유효한 고유’를 구별 |

과거 커뮤니티 글의 수치를 현재 정답으로 옮기거나 작성자의 의견을 GGG 공식 규칙으로 바꾸지 않는다. 연결 영상·외부 PoB 빌드 파일은 실행하지 않았다.

## 오픈소스·공식 기술 문서와 적용 방법

| 출처·확인 버전 | 재사용할 방법 | 호환성·라이선스·제약 |
| --- | --- | --- |
| [Path of Building README v2.67.2](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/v2.67.2/README.md), [CalcTriggers.lua](https://raw.githubusercontent.com/PathOfBuildingCommunity/PathOfBuilding/v2.67.2/src/Modules/CalcTriggers.lua), [LICENSE](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/v2.67.2/LICENSE.md) | 스킬/보조·장비·발동 조건을 분리한 계산, 지원 여부와 근거 표시 | 고정 태그 문서·발동 계산 소스를 열람. 프로젝트 코드는 MIT, 포함 구성요소는 개별 조건. Lua·PoE 전용 자료여서 Unity C#에 직접 호환되지 않음. 설치·실행·포팅·코드 복사 없음 |
| [Python unittest](https://docs.python.org/3.9/library/unittest.html), [heapq](https://docs.python.org/3.9/library/heapq.html) | 독립 산술/상태 테스트, 안정된 순번을 가진 사건 큐 | 실제 셸은 Python **3.9.6**, 열람한 3.9 문서 표기는 3.9.25. 기본 API만 사용해 실행 확인. Python은 PSF 라이선스이며 새 외부 패키지 도입 없음 |
| [Python 3.14 문서](https://docs.python.org/3.14/library/heapq.html)와의 대조 | 과거 환경의 Python 3.14.5 기록을 현재로 가정하지 않음 | 이번 런타임을 실제 확인하고 3.14 전용 API는 사용하지 않음 |

대안은 기존 PoB 실행/포팅, 스프레드시트만으로 계산, 독립 오프라인 모델이다. PoB는 원본 데이터와 현재 기획의 차이가 크고 Unity 호환도 직접적이지 않다. 표만으로는 순서·대기·발동·틱 갱신을 확인하기 어렵다. 따라서 **JSON 초안 데이터 + Python 표준 라이브러리 모델**을 권장하고 사용자 요청의 수치 검증 범위에 적용했다. Unity 전투 코드는 바꾸지 않는다.

## 조사와 실제 실행의 구분

문헌 조사에서는 원본 역할·제약·권리·적용 범위를 확인했다. 실제 실행은 자체 작성한 모델/테스트/전수 열거뿐이다. 기존 Unity 6000.3.11f1/uGUI 2.0.0 프로토타입 기록은 맥락이며 이번 새 성장/보조 구조를 Unity에서 실행했다는 근거가 아니다.

검증 계획은 ID·호환·상호 배제·고유 우선순위·피해 계산·XP 중복 정산 → 사건 순서/발동 깊이/상태이상 갱신/행동 병목 → 동일 장비 예산과 적 조건별 조합 → 별도 시드/적 조건 → 민감도 비교다. 전체 결과는 입력/도구/테스트 해시와 함께 저장했다. 실제 이동·충돌, 적 HP/오버킬·클리어 시간, 장기 경제·모바일 성능·사용자 재미는 수행하지 않았다.

원본 수치를 베껴 ‘균형’을 주장하지 않고 자체 데이터에서 발견한 편중을 기록했다. 출혈/주문 성장의 첫 문제와 조정, 아직 약한 치명 연동·생명 소모 및 고유 선택의 한계는 [결과 요약](../Design/Analysis/SkillGems/SUMMARY.md)에 남긴다.
