# 한국어 글 검토

한국어 비문학 글의 **장점을 근거와 함께 설명하고, 중요한 문제부터 개선안을 제안하는 Agent Skill**입니다. 스킬 이름은 `review-korean-writing`입니다.

보고서, 설명문, 논설문, 업무 메일, 안내문, 기술 문서를 대상으로 합니다. 기본 동작은 분석과 부분 수정 제안이며, 전체 재작성은 요청했을 때 수행합니다.

## 앱에서 설치하기 — 터미널 없이

**[설치용 ZIP 다운로드](https://github.com/youngminnnn/korean-writing-review/releases/latest/download/review-korean-writing.zip)** · [버전별 다운로드](https://github.com/youngminnnn/korean-writing-review/releases)

ZIP 하나를 내려받아 앱의 스킬 업로드 메뉴에서 등록합니다. Node.js·Python·Git 설치는 필요하지 않습니다. 스킬은 글 검토 지침과 참고 문서로 동작합니다.

**GitHub의 Code → Download ZIP이나 Release의 Source code (zip)은 설치용 파일이 아닙니다.** 위 링크의 `review-korean-writing.zip`을 받으세요. 앱이 폴더 업로드를 요구하면 압축을 풀고, 바로 안에 `SKILL.md`가 있는 `review-korean-writing` 폴더를 선택합니다. 참고 문서도 함께 유지합니다.

### ChatGPT 앱

Skills 업로드 기능이 제공되는 계정에서 다음 순서로 등록합니다.

1. **Plugins → Skills**를 엽니다. 데스크톱 앱에서는 사이드바에 **Skills**가 직접 표시될 수도 있습니다.
2. **Create → Upload from your computer**를 선택하고 다운로드한 설치용 ZIP을 등록합니다. 선택 창이 폴더를 요구하면 압축을 푼 스킬 폴더를 선택합니다.
3. 업로드 검사가 끝나면 스킬 목록에서 **한국어 글 검토** 또는 **review-korean-writing**을 확인합니다.
4. 새 대화에서 `@`로 스킬을 선택하고 아래 첫 요청 예시와 원문을 보냅니다.

메뉴와 제공 여부는 계정·워크스페이스 설정·앱 버전에 따라 다릅니다. 메뉴가 없으면 [공식 Skills 안내](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)를 확인하세요. 일반 대화에 ZIP을 첨부하는 것만으로 영구 설치되는 것은 아닙니다. 표시 이름 등 앱 메타데이터는 [공식 스킬 문서](https://learn.chatgpt.com/docs/build-skills)를 따릅니다.

### Claude 데스크톱 앱·웹

1. **Settings → Capabilities**에서 **Code execution and file creation** 또는 **Create and edit files**를 활성화합니다. 조직 계정은 관리자 설정이 필요할 수 있습니다.
2. **Customize → Skills → + → Create skill → Upload a skill**을 선택합니다.
3. `review-korean-writing.zip`을 업로드하고 목록에서 스킬을 활성화합니다.
4. 새 대화에서 “review-korean-writing 스킬로 아래 글을 검토해줘”라고 요청합니다.

앱에서 업로드 메뉴가 보이지 않으면 같은 계정의 Claude 웹에서 **Customize → Skills**를 확인하세요. 조직 정책에 따라 업로드가 제한될 수 있습니다. [Claude 공식 설치 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### 첫 요청

> 한국어 글 검토(review-korean-writing) 스킬로 아래 글을 검토해줘. 독자는 해당 업무를 처음 맡은 동료야. 유지할 장점을 짚고 중요한 개선점부터 원문과 수정안을 비교해줘. 원문 용어가 더 이해하기 쉬우면 유지해줘.

이 요청 뒤에 원문을 붙여넣거나 검토할 문서를 첨부합니다. 설치 안내는 2026년 11월 17일 공식 문서 기준이며, 각 앱에서의 실제 업로드·실행 검증과는 구분합니다.

## CLI에서 npx로 설치

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
  agents/openai.yaml   # 앱 표시 이름·설명·기본 요청
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

## 업데이트

- **앱에 ZIP으로 설치했다면:** [최신 릴리스](https://github.com/youngminnnn/korean-writing-review/releases/latest)에서 새 ZIP을 받습니다. 앱에 교체·업데이트 기능이 있으면 이를 사용하고, 없다면 기존 스킬을 비활성화하거나 제거한 뒤 새 ZIP을 등록합니다. 직접 수정한 내용은 먼저 보관하세요. GitHub의 변경이 업로드한 스킬에 자동 반영되지는 않습니다. 등록 후 새 대화에서 스킬을 확인합니다.
- **npx로 설치했다면:** `npx skills check`로 확인하고 `npx skills update`로 갱신합니다. CLI 버전에 따라 범위 선택을 확인하세요.

## 릴리스 발행

관리자는 검증된 커밋에 `v0.1.0` 같은 버전 태그를 붙여 push합니다. GitHub Actions가 패키지를 검증하고 설치용 ZIP을 해당 버전의 GitHub Release에 자동으로 첨부합니다. 태그는 새 버전마다 새로 만들며 이미 배포한 버전은 덮어쓰지 않습니다.

```sh
git tag v0.1.0
git push origin v0.1.0
```

위 명령의 버전은 예시입니다. 다음 발행 시에는 아직 사용하지 않은 버전으로 바꿉니다. README 상단 다운로드 링크는 최신 정식 릴리스를 가리킵니다.
