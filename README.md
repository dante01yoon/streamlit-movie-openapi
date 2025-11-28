# 영화 박스오피스 대시보드 실행 가이드

Streamlit으로 만든 간단한 박스오피스 대시보드입니다. 날짜를 선택하고 KOBIS API 키를 입력하면 일간 Top 10 관객 수 그래프와 상세 표를 볼 수 있습니다.

## 1) 준비물
- Python 3.9 이상
- 패키지 관리 도구 [uv](https://github.com/astral-sh/uv)

### uv 설치 (없다면 먼저 실행)
```bash
# 맥/리눅스 (권장)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 또는 pip로 설치
pip install uv
```

## 2) 프로젝트 설정
터미널을 열고 프로젝트 폴더로 이동한 뒤 아래를 실행하세요.

```bash
# 필요한 패키지 설치 (uv가 내부적으로 격리 환경을 관리)
uv pip install -r requirements.txt
```

## 3) KOBIS API 키 설정
앱은 아래 순서로 키를 찾습니다.
1. `.streamlit/secrets.toml` 의 `KOBIS_API_KEY`
2. 환경 변수 `KOBIS_API_KEY`
3. (없다면) 실행 후 사이드바 입력

### 권장: `.streamlit/secrets.toml` 사용 (export 없이)
프로젝트 루트에 `.streamlit/secrets.toml` 파일을 만들고 아래처럼 넣어주세요.

```toml
KOBIS_API_KEY = "여기에_본인_API_키"
```

### 대안: 환경 변수로 설정
```bash
# 맥/리눅스
export KOBIS_API_KEY="여기에_본인_API_키"

# PowerShell
setx KOBIS_API_KEY "여기에_본인_API_키"
```

> 둘 다 설정하지 않았다면, 앱 실행 후 사이드바에 직접 API 키를 입력하면 됩니다.

## 4) 앱 실행
uv로 바로 실행할 수 있습니다.

```bash
uv run streamlit run app.py
```

터미널에 표시되는 로컬 URL(예: http://localhost:8501)을 브라우저에서 열면 됩니다.

## 5) 사용 방법
1. 사이드바에 KOBIS API 키가 자동으로 채워졌는지 확인하거나 직접 입력합니다.
2. 화면의 날짜 선택 위젯에서 조회할 날짜를 고릅니다. (기본값은 어제)
3. "순위 조회하기" 버튼을 누르면 Top 10 막대그래프와 상세 표가 나타납니다.

## 6) 문제 해결 팁
- API 키 오류: 키를 다시 확인하거나 사이드바에 새로 입력 후 버튼을 다시 누르세요.
- 데이터가 없을 때: 과거 날짜를 선택해 보거나 잠시 후 다시 시도하세요.
- 모듈 오류: `pip install -r requirements.txt`를 다시 실행해 패키지를 설치하세요.
