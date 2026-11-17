# 한국어 글 검토

한국어 비문학 글의 **장점을 근거와 함께 설명하고, 중요한 문제부터 개선안을 제안하는 Agent Skill**입니다. 스킬 이름은 `review-korean-writing`입니다.

보고서, 설명문, 논설문, 업무 메일, 안내문, 기술 문서를 대상으로 합니다. 기본 동작은 분석과 부분 수정 제안이며, 전체 재작성은 요청했을 때 수행합니다.

## npx로 설치

Node.js 22.20 이상과 Git을 준비하고 사용할 프로젝트에서 실행합니다. 요구 버전은 [skills CLI 공식 문서](https://github.com/vercel-labs/skills)를 기준으로 합니다.

```sh
npx skills add youngminnnn/korean-writing-review --skill review-korean-writing
```

에이전트를 지정하려면:

```sh
# Codex
npx skills add youngminnnn/korean-writing-review --skill review-korean-writing -a codex

# Claude Code
npx skills add youngminnnn/korean-writing-review --skill review-korean-writing -a claude-code
```

여러 프로젝트에서 사용하려면 `-g`를 추가합니다. 설치 후 새 에이전트 세션에서 사용합니다. 설치 내용만 확인하려면 `npx skills add youngminnnn/korean-writing-review --list`를 실행합니다.

`npx`는 Vercel의 `skills` 설치 도구를 실행하고 이 GitHub 저장소에서 스킬을 가져옵니다. 이 저장소를 별도 npm 패키지로 발행할 필요가 없습니다. 이 명령은 로컬 에이전트용이며 ChatGPT·Claude 웹 계정에 직접 등록하지 않습니다.

## 사용 예

```text
review-korean-writing 스킬로 아래 글을 검토해줘.
독자는 해당 업무를 처음 맡은 동료야.
유지할 장점을 짚고, 중요한 개선점부터 원문과 수정안을 비교해줘.

[원문]
```

Codex에서는 `$review-korean-writing`으로 호출할 수도 있습니다.

- “논리와 문단 흐름만 검토해줘. 원문은 수정하지 마.”
- “전문가 대상 보고서야. 전문 용어와 격식은 유지해줘.”
- “제안한 수정 중 의미가 달라지는 것은 따로 표시해줘.”
- “검토 후 전체 수정본도 작성해줘. 확인되지 않은 사실은 추가하지 마.”

## 검토 관점과 결과

이해 용이성 / 명확성·정확성 / 문법·표현 / 문장·문단 연결 / 맥락·관련성 / 목적·독자 적합성 / 논리·근거 / 정보의 충분성·간결성 / 전체 구조·강조를 살핍니다.

결과는 전체 진단 → 유지할 장점 → 우선 개선점 → 대목별 제안 → 확인할 사항 순서입니다. 짧은 글이나 부분 검토는 간소화합니다. 오류·전달 개선·선택적 문체 제안·확인 필요를 구별하고, 억지로 문제를 만들어내지 않습니다.

**우리말화보다 이해와 정확성을 우선합니다.** 원문 용어·외래어·영어가 독자에게 더 익숙하면 유지하고, 필요할 때 첫 등장에만 풀이를 붙입니다. 기계적인 한국어 직역은 하지 않습니다.

## 관리와 검증

```text
skills/review-korean-writing/
  SKILL.md
  references/
    criteria.md
    korean-style.md
    examples.md
scripts/validate.py    # 형식·참조 파일 검증 및 설치 ZIP 생성
```

```sh
python3 scripts/validate.py
```

검증을 통과하면 `dist/review-korean-writing.zip`을 만듭니다. ZIP 안의 최상위 폴더는 `review-korean-writing`이며 스킬 본문과 참고 문서가 함께 들어 있습니다. ZIP 업로드를 지원하는 환경에서는 해당 환경의 안내에 따라 사용합니다. GitHub 전체 소스 ZIP과 구별하세요.

CI는 패키지 형식과 참조 누락을 검사합니다. 글 검토 품질은 자동으로 보증하지 않습니다.

업데이트 확인은 `npx skills check`, 업데이트는 `npx skills update`를 사용합니다. CLI 버전에 따라 범위 선택을 확인하세요.
