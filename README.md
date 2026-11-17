# 한국어 글 검토

ChatGPT·Claude 등이 한국어 비문학 글을 검토할 때 사용하는 지침 묶음입니다. **글의 장점을 근거와 함께 설명하고, 중요한 문제부터 개선안을 제안합니다.** 스킬 이름은 `review-korean-writing`입니다.

보고서, 설명문, 논설문, 업무 메일, 안내문, 기술 문서를 대상으로 합니다. 기본 동작은 분석과 부분 수정 제안이며, 전체 재작성은 요청했을 때 수행합니다.

## ChatGPT 플러그인으로 사용하기

기존 스킬을 포함한 `korean-writing-review` 플러그인을 제공합니다. **공개 플러그인 디렉터리에는 아직 등록되지 않았습니다.** 현재는 GitHub 마켓플레이스를 지원하는 로컬 클라이언트에서 설치하거나, 아래 개발·배포 절차로 플러그인 ZIP을 만들 수 있습니다.

### GitHub 마켓플레이스로 설치

`codex plugin marketplace` 명령을 지원하는 최신 Codex CLI에서 실행합니다.

```sh
codex plugin marketplace add youngminnnn/korean-writing-review
```

ChatGPT 데스크톱 앱의 로컬 실행 환경에서 Plugins Directory를 새로고침하고, 소스 **한국어 글 검토**에서 플러그인을 설치합니다. 새 대화에서 `@`로 **한국어 글 검토**를 선택하고 원문을 보냅니다. 메뉴·로컬 마켓플레이스 지원 여부는 클라이언트와 워크스페이스 설정에 따라 다릅니다. 이 명령은 ChatGPT 웹 계정에 플러그인을 공개하거나 등록하지 않습니다. [공식 패키징·마켓플레이스 안내](https://developers.openai.com/plugins/build/plugins)

스킬 ZIP으로 이미 설치했다면 같은 지침이 중복 적용되지 않도록 한 경로만 활성화하세요. **플러그인 형식과 ZIP 내용은 검증했지만 ChatGPT 앱에서 실제 설치·호출은 아직 검증하지 않았습니다.**

## 앱에 스킬로 설치하기 — 터미널 없이

**[설치용 ZIP 다운로드](https://github.com/youngminnnn/korean-writing-review/releases/latest/download/review-korean-writing.zip)** · [버전별 다운로드](https://github.com/youngminnnn/korean-writing-review/releases)

ZIP 하나를 내려받아 앱의 스킬 업로드 메뉴에서 등록합니다. Node.js·Python·Git 설치는 필요하지 않습니다. 스킬은 글 검토 지침과 참고 문서로 동작합니다.

**GitHub의 Code → Download ZIP이나 Release의 Source code (zip)은 설치용 파일이 아닙니다.** 위 링크의 `review-korean-writing.zip`을 받으세요. 앱이 폴더 업로드를 요구하면 압축을 풀고, 바로 안에 `SKILL.md`가 있는 `review-korean-writing` 폴더를 선택합니다. 참고 문서도 함께 유지합니다.

### ChatGPT 앱

Skills 업로드 기능이 제공되는 계정에서 다음 순서로 등록합니다.

1. **Plugins → Skills**를 엽니다. 데스크톱 앱에서는 사이드바에 **Skills**가 직접 표시될 수도 있습니다.
2. **Create → Upload from your computer**를 선택하고 다운로드한 설치용 ZIP을 등록합니다. 선택 창이 폴더를 요구하면 압축을 푼 스킬 폴더를 선택합니다.
3. 업로드 검사가 끝나면 스킬 목록에서 **한국어 글 검토** 또는 **review-korean-writing**을 확인합니다.
4. 새 대화에서 `@`로 스킬을 선택하고 아래 첫 요청 예시와 원문을 보냅니다.

메뉴와 제공 여부는 계정·워크스페이스 설정·앱 버전에 따라 다릅니다. 메뉴가 없으면 [공식 Skills 안내](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)를 확인하세요. 일반 대화에 ZIP을 첨부하는 것만으로 영구 설치되는 것은 아닙니다.

### Claude 데스크톱 앱·웹

1. **Settings → Capabilities**에서 **Code execution and file creation** 또는 **Create and edit files**를 활성화합니다. 조직 계정은 관리자 설정이 필요할 수 있습니다.
2. **Customize → Skills → + → Create skill → Upload a skill**을 선택합니다.
3. `review-korean-writing.zip`을 업로드하고 목록에서 스킬을 활성화합니다.
4. 새 대화에서 “review-korean-writing 스킬로 아래 글을 검토해줘”라고 요청합니다.

앱에서 업로드 메뉴가 보이지 않으면 같은 계정의 Claude 웹에서 **Customize → Skills**를 확인하세요. 조직 정책에 따라 업로드가 제한될 수 있습니다. [Claude 공식 설치 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### 첫 요청

> 한국어 글 검토(review-korean-writing) 스킬로 아래 글을 검토해줘. 독자는 해당 업무를 처음 맡은 동료야. 유지할 장점을 짚고 중요한 개선점부터 원문과 수정안을 비교해줘. 원문 용어가 더 이해하기 쉬우면 유지해줘.

이 요청 뒤에 원문을 붙여넣거나 검토할 문서를 첨부합니다.

앱별 설치 절차는 2026년 11월 17일 공식 문서를 참고했습니다. **ChatGPT·Claude 앱에서의 실제 업로드와 실행은 아직 검증하지 않았습니다.**

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

Codex에서는 `$review-korean-writing`으로 호출할 수도 있습니다.

## 검토 범위 바꾸기

첫 요청에 조건을 덧붙이거나, 검토 결과를 받은 뒤 다음과 같이 요청할 수 있습니다.

- “논리와 문단 흐름만 검토해줘. 원문은 수정하지 마.”
- “전문가 대상 보고서야. 전문 용어와 격식은 유지해줘.”
- “제안한 수정 중 의미가 달라지는 것은 따로 표시해줘.”
- “검토 후 전체 수정본도 작성해줘. 확인되지 않은 사실은 추가하지 마.”

## 검토 관점과 결과

이해하기 쉬운지, 표현이 정확하고 자연스러운지, 문장과 문단이 잘 이어지는지 살핍니다. 글의 목적과 독자에 맞춰 내용의 관련성, 논리·근거, 정보량, 전체 구성도 검토합니다. 세부 기준은 [스킬 본문](skills/review-korean-writing/SKILL.md)에 있습니다.

결과는 전체 진단 → 유지할 장점 → 우선 개선점 → 대목별 제안 → 확인할 사항 순서입니다. 짧은 글이나 부분 검토는 간소화합니다. 오류·전달 개선·선택적 문체 제안·확인 필요를 구별하고, 억지로 문제를 만들어내지 않습니다.

**우리말화보다 이해와 정확성을 우선합니다.** 원문 용어·외래어·영어가 독자에게 더 익숙하면 유지하고, 필요할 때 첫 등장에만 풀이를 붙입니다. 기계적인 한국어 직역은 하지 않습니다.

## 업데이트

- **GitHub 마켓플레이스로 설치했다면:** `codex plugin marketplace upgrade korean-writing-review`로 소스를 갱신하고 앱에서 해당 플러그인을 업데이트한 뒤 새 대화에서 확인합니다. 공개 디렉터리에 게시된 플러그인은 별도로 관리됩니다.

- **앱에 ZIP으로 설치했다면:** [최신 릴리스](https://github.com/youngminnnn/korean-writing-review/releases/latest)에서 새 ZIP을 받습니다. 앱에 교체·업데이트 기능이 있으면 이를 사용하고, 없다면 기존 스킬을 비활성화하거나 제거한 뒤 새 ZIP을 등록합니다. 직접 수정한 내용은 먼저 보관하세요. GitHub의 변경이 업로드한 스킬에 자동 반영되지는 않습니다. 등록 후 새 대화에서 스킬을 확인합니다.
- **npx로 설치했다면:** `npx skills check`로 확인하고 `npx skills update`로 갱신합니다. CLI 버전에 따라 범위 선택을 확인하세요.

설치 경로에 따라 받는 버전이 다를 수 있습니다. 상단 ZIP 링크는 최신 정식 릴리스를, 위의 버전 미지정 `npx` 명령은 저장소 기본 브랜치(`main`)의 최신 내용을 가져옵니다. CLI에서도 특정 릴리스와 같은 내용을 설치하려면 다음처럼 버전을 지정합니다. [설치 도구의 버전 지정 안내](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#source-formats)

```sh
npx skills add youngminnnn/korean-writing-review@v0.1.0 --skill review-korean-writing
```

## 개발·배포

아래 내용은 스킬을 수정하거나 배포하는 관리자를 위한 안내입니다. 앱에 ZIP으로 설치해서 사용하는 데는 Python이나 Git이 필요하지 않습니다.

### 파일 구성과 검증

```text
plugin.json                         # 플러그인 정보·앱 표시 정보
.agents/plugins/marketplace.json    # GitHub 마켓플레이스 목록
skills/review-korean-writing/
  SKILL.md
  agents/openai.yaml   # 앱 표시 이름·설명·기본 요청
  references/
    criteria.md
    korean-style.md
    examples.md
scripts/validate.py    # 형식·참조 파일 검증 및 두 종류 ZIP 생성
```

`agents/openai.yaml`은 앱 표시 이름·설명·기본 요청을 지정합니다. [공식 스킬 문서](https://learn.chatgpt.com/docs/build-skills)의 메타데이터 형식을 따릅니다.

```sh
python3 scripts/validate.py
```

검증을 통과하면 `dist/review-korean-writing.zip`을 만듭니다. ZIP 안의 최상위 폴더는 `review-korean-writing`이며 스킬 본문과 참고 문서가 함께 들어 있습니다. ZIP 업로드를 지원하는 환경에서는 해당 환경의 안내에 따라 사용합니다. GitHub 전체 소스 ZIP과 구별하세요.

같은 명령으로 `dist/korean-writing-review-plugin.zip`도 만듭니다. 이 ZIP은 루트에 `plugin.json`, `LICENSE`, `skills/`를 포함하며, 일반 스킬 업로드용 ZIP과 구별해야 합니다. 두 패키지는 동일한 스킬 원본에서 생성합니다. 빌드 도구나 GitHub Actions 파일은 플러그인 ZIP에 포함하지 않습니다.

CI는 패키지 형식과 참조 누락을 검사합니다. 글 검토 품질은 자동으로 보증하지 않습니다.

### 릴리스 발행

관리자는 `plugin.json`의 `version`을 갱신하고 검증된 커밋에 같은 버전의 태그를 붙여 push합니다. 태그와 플러그인 버전이 다르면 검증이 실패합니다. GitHub Actions가 두 ZIP을 해당 버전의 GitHub Release에 자동으로 첨부합니다. 태그는 새 버전마다 새로 만들며 이미 배포한 버전은 덮어쓰지 않습니다.

```sh
git tag v0.2.0
git push origin v0.2.0
```

위 명령의 버전은 예시입니다. 다음 발행 시에는 아직 사용하지 않은 버전으로 바꿉니다. README 상단 다운로드 링크는 최신 정식 릴리스를 가리킵니다.

### ChatGPT 공개 플러그인 제출

1. `python3 scripts/validate.py`로 생성한 `dist/korean-writing-review-plugin.zip`을 준비합니다.
2. OpenAI Platform의 Plugins에서 게시 주체와 제작자 신원을 확인하고 플러그인 ZIP을 업로드합니다.
3. 메타데이터·스킬 자동 검사 결과를 해결한 뒤 심사를 요청합니다. 승인 후 공개 여부를 결정합니다. 제출 화면이 요구하는 추가 제작자 정보는 실제 정보로 작성합니다.
4. 스킬이나 표시 정보를 수정하면 버전을 올려 새 ZIP을 제출합니다. GitHub push나 GitHub Release만으로 공개 디렉터리의 플러그인이 갱신되지는 않습니다.

이 플러그인은 스킬만 포함하며 별도 MCP 서버나 외부 서비스 인증을 요구하지 않습니다. 로컬 프로그램 실행을 필수로 요구하지 않으므로 Desktop only로 지정하지 않습니다. [공식 제출 안내](https://developers.openai.com/plugins/deploy/submission)
