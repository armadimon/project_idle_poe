# 게임 기획 참고자료

『게임 기획 실무에서 바로 쓰는 AI·클로드 코드 활용법』의 한국어 원고를 Git 서브모듈로 보관한다. 게임 기획을 작은 결정 단위로 관리하는 방식을 학습하기 위한 자료다.

## 출처와 버전

| 항목 | 값 |
| --- | --- |
| 저자 | 이민수 Minsoo Lee, 조지희 Jihee Jo |
| 저장소 | [eremes81/game-design-ai-practice](https://github.com/eremes81/game-design-ai-practice) |
| 정본 | [원저자 웹 원고](https://eremes81.github.io/game-design-ai-practice/) |
| 로컬 위치 | `References/game-design-ai-practice/` |
| 확인일 | 2026-11-13 |
| 고정 커밋 | [`72d58a86a9f467347c16583c4f4570140f1f2453`](https://github.com/eremes81/game-design-ai-practice/tree/72d58a86a9f467347c16583c4f4570140f1f2453) |
| 커밋 시각 | 2026-10-30T21:35:34+09:00 |
| 버전 기준 | 태그 대신 실제 확인한 커밋에 고정 |
| 라이선스 | [원본 LICENSE](game-design-ai-practice/LICENSE), [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| 원문 변경 | 없음 |

기계가 읽는 출처 기록은 [sources.lock.json](sources.lock.json)에 둔다. 부모 저장소는 원본 파일을 합쳐 커밋하지 않고 원본 주소와 커밋을 참조한다.

## 먼저 읽을 부분

| 원고 | 이 프로젝트에서 참고할 작업 원리 |
| --- | --- |
| [2.1 문서 메타데이터](game-design-ai-practice/manuscript/part02-info-architecture/chapter-4-yaml-frontmatter.md) | 문서의 상태와 위치를 명시 |
| [2.2 작은 결정 문서](game-design-ai-practice/manuscript/part02-info-architecture/chapter-5-page-atom.md) | 결정을 나누고 이유와 연결 관계를 기록 |
| [2.3 기획 계층](game-design-ai-practice/manuscript/part02-info-architecture/chapter-6-layer-design.md) | 비전에서 규칙, 콘텐츠, 데이터, 검증으로 구체화 |
| [3.2 스키마 우선](game-design-ai-practice/manuscript/part03-system-design/chapter-10-schema-first.md) | 형식을 합의한 뒤 실제 데이터를 작성 |
| [10.2 결정 검증](game-design-ai-practice/manuscript/part10-qa-design/chapter-2-decision-validation-3-layer.md) | 형식 검사와 기획의 타당성 검토를 구분 |
| [18.1 의사결정 추적](game-design-ai-practice/manuscript/part18-decision-impact/chapter-1-decision-tracking-system.md) | 사용자 확인 근거와 영향 범위를 남김 |
| [19.1 비전과 결정](game-design-ai-practice/manuscript/part19-team-lead/chapter-1-vision-and-delegation.md) | 새 결정이 게임 방향과 맞는지 확인 |
| [부록 K 도구 중립 이식](game-design-ai-practice/manuscript/part99-appendix/appendix-K-tool-neutral-porting.md) | 특정 실행 도구보다 작업 절차를 참고 |

## 활용 범위

원고는 공개된 참고 저작물이며 MIT나 Apache 라이선스의 실행형 기획 프레임워크가 아니다. 원고에는 저작자표시, 비영리, 동일조건변경허락 조건이 있다. 원문이나 그 각색을 상업적 제품·서비스에 포함하는 용도는 현재 작업 범위에 포함하지 않는다. 원문의 구체적 문장, 예제 코드, 게임 데이터와 도식을 우리 게임 사양으로 복사하지 않는다. [원본 라이선스](game-design-ai-practice/LICENSE)

작은 문서, 결정 이력, 계층화, 형식 검사라는 일반적인 작업 원리를 참고하고, 프로젝트의 문서 규격·템플릿·검사 도구와 게임 내용은 자체 작성한다. CC는 저작권이 적용되는 표현에 관한 라이선스이며, 구체적인 재사용의 권리 판단은 해당 표현과 이용 방식에 따라 달라진다. [Creative Commons 공식 FAQ](https://creativecommons.org/faq/#what-do-the-terms-and-conditions-of-a-cc-license-apply-to)

## 참조 버전 관리

```sh
git submodule update --init --recursive
git -C References/game-design-ai-practice rev-parse HEAD
```

원고를 갱신할 때는 변경 내용을 검토하고 서브모듈 커밋, `sources.lock.json`, 이 문서의 버전 기록을 함께 갱신한다. 기획 문서가 바뀌어야 한다면 사용자 확인 절차를 별도로 거친다.
