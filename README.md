# project_idle_poe

장비·스킬 조합이 핵심인 방치형 액션 RPG를 기획한다. 현재 확정된 방향은 **모바일 우선**, **완전 자동 전투**, **전투 사이에 장비·스킬·도전 대상 선택**이다. 프로젝트 이름은 작업용 이름이며 출시명과 세계관은 미정이다.

세부 기획은 선택지 제안 → 사용자 확인 → 결정 기록 순서로 진행한다. 확인하지 않은 사항을 게임 사양으로 확정하지 않는다. 현재 단계는 기획이며 Unity 프로젝트와 게임 코드는 아직 없다.

## 기획 읽기

| 문서 | 내용 |
| --- | --- |
| [현재 방향](Docs/Design/00-Concept.md) | 확인된 기획과 미정 범위 |
| [기획 안내](Docs/Design/README.md) | 문서 구조와 사용자 확인 절차 |
| [기획 순서](Docs/Design/01-Decision-Queue.md) | 다음에 확인할 질문과 의존 관계 |
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
