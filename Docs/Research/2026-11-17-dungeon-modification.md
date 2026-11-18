# 던전 변화 시스템을 위한 맵 모딩 조사

확인일: 2026-11-17. 문헌과 공개 저장소를 열람했다. PoE 클라이언트·오픈소스 도구 실행, Unity 연동, 드롭·비용 실험은 수행하지 않았다. 최신 시즌의 전체 규칙이나 수치를 재현하는 조사가 아니다.

## 출처와 확인 범위

| 출처 | 확인한 버전·기록 | 확인 내용과 적용 한계 |
| --- | --- | --- |
| [GGG: Stories from Development — The Map System](https://www.pathofexile.com/forum/view-thread/2071848) | 2018-01-11 공식 개발 회고. 2012년 논의와 0.9.11의 맵 도입 설명 | 콘텐츠 비용과 감당할 위험, 보상을 연결한 설계 의도. 현행 패치의 맵 수치나 입장 규칙을 증명하는 자료는 아님 |
| [PoEDB: Maps](https://poedb.tw/us/Maps) | 확인일의 동적 데이터와 Community Wiki를 구분해 열람 | 맵의 지역 변화와 보상 관련 표현을 확인. 위키에는 Watchstone·구형 아틀라스 설명도 남아 있어 같은 페이지를 단일 최신 패치 사양으로 취급하지 않음 |
| [poe.re 제작자의 업데이트 기록](https://www.reddit.com/r/pathofexile/comments/1rlpjcq/poere_update_for_localization_profile_sharing_and/) | 2026-03-05 게시 기록 | 실행할 수 있는 맵을 조건으로 찾는 검색 문자열과 설정 공유 기능의 소개. 도구 제작자의 설명이며 이용자 전체의 행동 통계는 아님 |
| [빌드별 맵 옵션 대응 토론](https://www.reddit.com/r/PathOfExileBuilds/comments/1vomwre/best_build_for_not_caring_about_map_mods/) | 2026-08-15~16 본문·댓글 | 회복 수단 등 빌드 조건에 따라 피하는 옵션이 달라지고 외부 필터를 사용하는 자기 보고. 특정 빌드가 현재 모든 옵션을 처리한다는 사실이나 평균 비용으로 일반화하지 않음 |
| [veiset/poe.re](https://github.com/veiset/poe.re/tree/ef8032d05ffc086e49558a8ecac732f57e4639d9) | 커밋 `ef8032d05ffc086e49558a8ecac732f57e4639d9`, 2026-11-13T20:49:31Z | PoE 1 맵·PoE 2 Waystone 등의 검색 도구. 커밋은 GitHub API, 문서는 고정 커밋의 원문으로 확인. 로컬 반입·설치·실행하지 않음 |

## 조사에서 얻은 설계 관점

GGG의 회고는 단순 반복 지역의 지루함과 난도 선택 문제를 다루며, 비용을 지불하고 감당할 수 있는 지역의 보상을 얻는 발상이 맵 시스템으로 발전했다고 설명한다. 우리 프로젝트에서는 사용자가 확인한 재도전 입장 무료를 유지하면서 던전 변화의 재화 소비를 별도 의사결정으로 다룬다. [공식 회고](https://www.pathofexile.com/forum/view-thread/2071848)

커뮤니티와 도구 기록에서 읽은 흐름은 **빌드의 약점 파악 → 피하거나 감당할 맵 옵션 정리 → 검색·설정으로 반복 적용 → 설정 공유**다. 이는 자료에 대한 기획적 해석이며, 모든 플레이어가 같은 흐름을 따른다는 관찰 결과는 아니다. 던전 옵션은 장비·스킬의 약점에 따라 가치가 달라지는 빌드 판단 요소가 될 수 있다. [제작자 기록](https://www.reddit.com/r/pathofexile/comments/1rlpjcq/poere_update_for_localization_profile_sharing_and/), [빌드별 토론](https://www.reddit.com/r/PathOfExileBuilds/comments/1vomwre/best_build_for_not_caring_about_map_mods/)

외부 필터에 의존하는 사례는 사용자가 앞서 지적한 외부 정보 확인의 부담과 연결해 검토할 부분이다. 패널티와 보상의 확인 방법, 내 빌드에 미치는 영향의 안내는 후속 제안 대상이며 특정 UI·경고·자동 차단 기능의 승인으로 취급하지 않는다.

## 오픈소스의 호환성·라이선스와 재사용 범위

고정 커밋의 [package.json](https://github.com/veiset/poe.re/blob/ef8032d05ffc086e49558a8ecac732f57e4639d9/package.json)은 패키지 버전 0.1.0과 React `^19.0.0`, Vite `^7.0.0`을 선언한다. 이 숫자는 게임 패치나 실제 설치 해석 버전이 아니다. 브라우저용 React/Vite 도구여서 Unity C#에 직접 가져오는 구성은 아니며, 연동 가능성은 실행 검증하지 않았다.

코드는 [AGPL v3](https://github.com/veiset/poe.re/blob/ef8032d05ffc086e49558a8ecac732f57e4639d9/LICENSE), 생성 데이터는 별도 [DATA-LICENSE](https://github.com/veiset/poe.re/blob/ef8032d05ffc086e49558a8ecac732f57e4639d9/DATA-LICENSE.md) 적용이다. 데이터 문서는 규모가 큰 도구나 수익을 내는 도구에 별도 허락을 요구하며 게임 원문은 GGG의 권리로 구분한다. 코드 라이선스를 데이터 사용 허락으로 확대하지 않는다.

이번 재사용 범위는 빌드별 조건 정리·필터·설정 공유라는 판단 과정의 참고다. 코드·게임 데이터·옵션 문구·이미지는 제품에 복사하지 않는다. PoEDB의 CC BY-NC-SA 3.0 표시는 Community Wiki에 대한 것으로, 사이트 전체 데이터나 게임 자산의 일괄 제품 재사용 허락으로 보지 않는다. 관련성이 있는 도구를 조사했지만 라이브러리는 도입하지 않는다.

## 적용 제안과 검증 계획

확인된 방향과 대안은 [던전 변화 제안](../Design/Proposals/Dungeon-Modification.md)에 구분한다. 후속 [DEC-0061](../Design/Decisions/DEC-0061-dungeon-modification-for-farming-only.md)에서 파밍에만 적용하고 최고 단계 경쟁은 공통 조건을 유지하는 방향을 확인했다. 부여 방식은 후속 [DEC-0062](../Design/Decisions/DEC-0062-randomly-assign-farming-dungeon-penalties.md)에서 무작위 부여로 확인했다. 교체 범위는 후속 [DEC-0064](../Design/Decisions/DEC-0064-reroll-one-selected-dungeon-penalty.md)에서 지정한 한 줄의 무작위 교체로, 조작 방향은 [DEC-0065](../Design/Decisions/DEC-0065-right-side-lock-checkbox-for-dungeon-penalty-rows.md)에서 각 줄 우측 잠금 토글로 확인했다. 연동 방식은 후속 [DEC-0066](../Design/Decisions/DEC-0066-allow-only-one-unlocked-dungeon-penalty-row.md)에서 최대 한 줄만 잠금 해제하고 대상 전환 시 기존 줄을 자동 잠금하는 것으로 확인했다. 새 결과 적용은 후속 [DEC-0067](../Design/Decisions/DEC-0067-apply-new-dungeon-penalty-result-directly.md)에서 즉시 적용으로 확인했다. 교체 실행마다 재화를 소모하는 원칙은 후속 [DEC-0068](../Design/Decisions/DEC-0068-consume-currency-for-each-dungeon-penalty-replacement.md)에서 확인했다. 후속 [DEC-0070](../Design/Decisions/DEC-0070-share-equipment-replacement-material-with-dungeon-penalty-replacement.md)에서 장비 옵션 교체의 기본 재료를 패널티 교체와 공유하는 것으로 확인했다. 후속 [DEC-0071](../Design/Decisions/DEC-0071-no-cost-escalation-for-repeated-dungeon-penalty-replacement.md)에서 같은 조건에서는 반복 횟수에 따른 교체 비용 증가를 두지 않는 것으로 확인했다. 후속 [DEC-0073](../Design/Decisions/DEC-0073-no-attempt-limit-for-dungeon-penalty-replacement.md)에서 패널티 교체에 별도 횟수 제한을 두지 않는 것으로 확인했다. 후속 [DEC-0074](../Design/Decisions/DEC-0074-reset-farming-dungeon-modifiers-after-successful-clear.md)에서 파밍 성공 후 패널티와 연결된 보상 강화 설정을 초기화하는 것으로 확인했다. 후속 [DEC-0075](../Design/Decisions/DEC-0075-reset-farming-dungeon-modifiers-after-failure.md)에서 파밍 실패 후에도 패널티와 연결된 보상 강화 설정을 초기화하는 것으로 확인했다. 후속 [DEC-0076](../Design/Decisions/DEC-0076-no-refund-of-dungeon-penalty-replacement-materials-after-failure.md)(2026-11-18)에서 실패한 도전의 패널티 교체에 사용한 재료는 환급하지 않는 것으로 확인했다. 후속 [DEC-0077](../Design/Decisions/DEC-0077-allow-farming-retries-without-separate-entry-cost.md)(2026-11-18)에서 실패 후 같은 파밍 대상에 새 도전을 허용하고 입장 자체에는 별도 비용을 두지 않는 것으로 확인했다. 후속 [DEC-0078](../Design/Decisions/DEC-0078-initial-farming-dungeon-penalties-generated-as-one-random-batch.md)(2026-11-18)에서 최초 기본 패널티들을 한 번에 무작위 부여하는 것으로 확인했다. 후속 [DEC-0082](../Design/Decisions/DEC-0082-currency-dependent-random-count-for-initial-dungeon-penalties.md)(2026-11-18)에서 최초 패널티 개수는 부여 재화에 따라 무작위로 결정하는 것으로 확인했다. 추가 문헌 확인은 [재화별 개수 추첨 조사](2026-11-18-currency-dependent-dungeon-penalty-counts.md)에 둔다. 다음에는 부여 재화 종류 수·공유 여부·개수 범위·확률·최대 개수·비용·재도전 횟수·기타 조건·공급·보상·나머지 지속 범위·기본 잠금 상태·전체 잠금 처리를 각각 확인한다.

후속 규칙을 승인받으면 서로 다른 빌드가 같은 패널티에 보이는 차이와 보상 대비 투자 판단 사례를 만든다. 수치 승인 뒤 시간당 재료 획득·클리어 성공·반복 조작 부담을 실제 실험한다. 최고 단계 경쟁에 모딩이 적용되지 않고 공통 도전 조건을 유지하는지도 확인한다. 현재 완료한 검증은 출처 열람과 버전·라이선스 문서 확인이며, 게임 재미·경제·전투 검증은 미실시다.
