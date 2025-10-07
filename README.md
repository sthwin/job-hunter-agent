# Job Hunter Agent

AI 기반 구직 에이전트로 관련된 채용 공고를 찾고 지원하는 자동화된 시스템입니다.

## 🚀 프로젝트 개요

이 프로젝트는 CrewAI 프레임워크를 사용하여 구직 과정을 자동화하는 AI 에이전트입니다. 이력서를 분석하고, 관련 채용 공고를 찾아서 자동으로 지원하는 기능을 제공합니다.

## 📋 주요 기능

- **이력서 분석**: 개인 이력서를 기반으로 적합한 직무 파악
- **채용 공고 검색**: 다양한 채용 사이트에서 관련 공고 자동 검색
- **자동 지원**: 발견된 채용 공고에 자동으로 지원서 작성 및 제출
- **진행 상황 추적**: 지원 현황 및 결과 모니터링

## 🛠️ 기술 스택

- **Python 3.13+**
- **CrewAI**: AI 에이전트 프레임워크
- **Firecrawl**: 웹 스크래핑 도구
- **uv**: 빠른 Python 패키지 관리자

## 📦 설치 방법 (macOS)

### 1. uv 설치

uv는 Rust로 작성된 빠른 Python 패키지 관리자입니다. Homebrew를 사용하여 설치할 수 있습니다:

```bash
# Homebrew가 설치되어 있지 않은 경우
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# uv 설치
brew install uv
```

또는 공식 설치 스크립트를 사용할 수 있습니다:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 프로젝트 클론

```bash
git clone https://github.com/sthwin/job-hunter-agent.git
cd job-hunter-agent
```

### 3. 가상환경 생성 및 의존성 설치

```bash
# 가상환경 생성 및 활성화
uv venv

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 의존성 동기화
uv sync
```

### 4. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 필요한 API 키를 설정하세요:

```bash
# .env 파일 생성
touch .env
```

`.env` 파일에 다음 내용을 추가하세요:

```env
# OpenAI API 키 (필수)
OPENAI_API_KEY=your_openai_api_key_here

# Firecrawl API 키 (웹 스크래핑용)
FIRECRAWL_API_KEY=your_firecrawl_api_key_here

# 기타 필요한 API 키들
# LINKEDIN_API_KEY=your_linkedin_api_key_here
# INDEED_API_KEY=your_indeed_api_key_here
```

## 🚀 프로젝트 실행

### 1. 기본 실행

```bash
# 가상환경이 활성화된 상태에서
python main.py
```

### 2. 개발 모드 실행

```bash
# 디버그 모드로 실행
uv run python main.py --debug
```

### 3. 특정 작업 실행

```bash
# 특정 에이전트 작업만 실행
uv run python main.py --task resume_analysis
```

## 📁 프로젝트 구조

```
job-hunter-agent/
├── config/
│   ├── agents.yaml      # AI 에이전트 설정
│   └── tasks.yaml       # 작업 정의
├── knowledge/
│   └── resume.txt       # 이력서 데이터
├── main.py              # 메인 애플리케이션
├── pyproject.toml       # 프로젝트 설정
├── README.md            # 프로젝트 문서
└── .env                 # 환경 변수 (생성 필요)
```

## ⚙️ 설정 파일

### agents.yaml
AI 에이전트들의 역할과 설정을 정의합니다.

### tasks.yaml
수행할 작업들의 정의와 워크플로우를 설정합니다.

### knowledge/resume.txt
분석할 이력서 내용을 저장합니다.

## 🔧 개발 도구

### 의존성 관리

```bash
# 새 패키지 추가
uv add package_name

# 개발 의존성 추가
uv add --dev package_name

# 패키지 제거
uv remove package_name

# 의존성 업데이트
uv sync --upgrade
```

### 코드 포맷팅 및 린팅

```bash
# 코드 포맷팅 (black 사용)
uv run black .

# 린팅 (ruff 사용)
uv run ruff check .
```

## 🐛 문제 해결

### 일반적인 문제들

1. **Python 버전 오류**
   ```bash
   # Python 3.13 이상이 설치되어 있는지 확인
   python --version
   
   # uv로 Python 설치
   uv python install 3.13
   ```

2. **의존성 설치 실패**
   ```bash
   # 캐시 정리 후 재설치
   uv cache clean
   uv sync --reinstall
   ```

3. **API 키 오류**
   - `.env` 파일이 프로젝트 루트에 있는지 확인
   - API 키가 올바르게 설정되었는지 확인
   - API 키의 권한과 할당량 확인

## 📝 사용법

1. **이력서 업데이트**: `knowledge/resume.txt` 파일에 최신 이력서 내용을 작성
2. **설정 조정**: `config/` 폴더의 YAML 파일들을 필요에 따라 수정
3. **API 키 설정**: `.env` 파일에 필요한 API 키들을 입력
4. **실행**: `python main.py` 명령으로 프로그램 실행

## 🤝 기여하기

1. 이 저장소를 포크합니다
2. 새 기능 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 지원

문제가 발생하거나 질문이 있으시면 [Issues](https://github.com/sthwin/job-hunter-agent/issues) 페이지에서 문의해 주세요.

---

**Happy Job Hunting! 🎯**
