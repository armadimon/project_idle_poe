# project_idle_poe

**라이트한 PoE**를 지향하는 모바일 방치형 RPG를 기획한다. 전투는 완전 자동으로 진행하고 제작과 득템에 무게를 둔다. **종결 장비 제작이 핵심이며, 종결 장비를 통해 경쟁하는 게임**을 목표로 한다. 프로젝트 이름은 작업용 이름이며 출시명과 세계관은 미정이다.

종결 장비는 빌드별로 좋은 옵션 조합을 찾고, 그 조합의 옵션 등급과 수치까지 완성하는 혼합형을 기준으로 한다.

주력 제작 경로는 전투에서 얻은 장비의 기반과 기존 옵션을 보고 제작할 대상을 선별해 다듬는 방식이다.

기본 제작 장비의 추가 옵션은 접두 최대 3개와 접미 최대 3개를 기준으로 한다.

추가 옵션 제작은 희귀 장비를 중심으로 한다. 기본 제작 작업은 옵션 한 개씩 추가·제거·교체하는 세 종류를 각각 제공한다. 기본 세 작업에는 별도의 성공·실패 판정을 두지 않는다. 고유 장비는 정해진 특수 효과를 제공하며 추가 옵션 제작에서 제외한다.

제작 결과는 기본적으로 무작위이며, 재료나 작업으로 추첨 범위를 제한적으로 좁히는 통제 수단을 제공한다. 통제는 접두·접미 중 대상 그룹을 고르는 방식이며, 선택한 그룹 안의 개별 결과는 무작위다. 그룹 지정에는 기본 제작 비용 외에 추가 재료를 사용하고, 추가 통제 재료 없이 진행하는 제작도 제공한다. 세 작업 모두 통제를 허용하며 통제한 교체의 제거·추가는 같은 그룹 안에서 진행한다.

장비·스킬의 작동 구조는 **PoE 1**, 아이템 제작은 **PoE 2**를 기준으로 삼는다. 공식 자료와 PoEDB 계열 데이터, 제작자·커뮤니티 기록을 조사해 기획에 활용한다.

세부 기획은 선택지 제안 → 사용자 확인 → 결정 기록 순서로 진행한다. 확인하지 않은 사항을 게임 사양으로 확정하지 않는다. 현재 단계는 기획이며 Unity 프로젝트와 게임 코드는 아직 없다.

## 기획 읽기

| 문서 | 내용 |
| --- | --- |
| [현재 방향](Docs/Design/00-Concept.md) | 확인된 기획과 미정 범위 |
| [기획 안내](Docs/Design/README.md) | 문서 구조와 사용자 확인 절차 |
| [기획 순서](Docs/Design/01-Decision-Queue.md) | 다음에 확인할 질문과 의존 관계 |
| [제작과 종결 장비 연구](Docs/Research/Crafting/README.md) | PoE 2 제작과 토치라이트 인피니트 사례 비교 |
| [제작 중심 적용 제안](Docs/Design/Proposals/Crafting-Endgame.md) | 확인된 종결·옵션·주력 제작 경로와 다음 희귀 장비 드롭 구성, 경쟁의 논의 항목 |
| [PoE 1 빌드 연구](Docs/Research/PoE1/README.md) | 장비·스킬 구조와 커뮤니티 공략의 축적 사례 |
| [장비와 스킬 적용 제안](Docs/Design/Proposals/PoE1-Equipment-Skills.md) | 조사 결과를 바탕으로 사용자와 확인할 항목 |
| [도입 조사](Docs/Research/2026-11-13-design-workflow.md) | 참고 방식, 대안, 호환성과 검증 범위 |
| [참고자료](References/README.md) | 원본 출처, 고정 버전과 라이선스 |

## 내려받기

```sh
git clone --recurse-submodules https://github.com/armadimon/project_idle_poe.git
cd project_idle_poe
python3 Tools/validate_design.py
```

이미 복제한 저장소에서 원본 참고자료를 받으려면 다음 명령을 실행한다.

```sh
git submodule update --init --recursive
```

원본은 `References/game-design-ai-practice/`에서 읽을 수 있다. 서브모듈을 포함하지 않는 GitHub ZIP 다운로드에는 원문이 들어 있지 않다.

## 라이선스 범위

외부 원고에는 원저자의 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)이 적용된다. 자세한 출처와 활용 범위는 [참고자료 안내](References/README.md)를 따른다. 이 프로젝트 자체의 배포 라이선스는 아직 정하지 않았다.
