import os
from datetime import date, timedelta
from typing import List, Dict, Any

import pandas as pd
import requests
import streamlit as st

API_ENDPOINT = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"


def get_default_date() -> date:
    """Return yesterday as the default query date."""
    return date.today() - timedelta(days=1)


def format_date(target: date) -> str:
    """Format a date object into the YYYYMMDD string expected by KOBIS."""
    return target.strftime("%Y%m%d")


@st.cache_data(show_spinner=False)
def fetch_box_office(api_key: str, target: date) -> pd.DataFrame:
    """Call the KOBIS daily box office API and return a DataFrame."""
    params = {"key": api_key, "targetDt": format_date(target)}
    response = requests.get(API_ENDPOINT, params=params, timeout=10)
    response.raise_for_status()
    payload: Dict[str, Any] = response.json()

    items: List[Dict[str, Any]] = payload.get("boxOfficeResult", {}).get("dailyBoxOfficeList", [])
    records = []
    for item in items:
        records.append(
            {
                "순위": int(item["rank"]),
                "영화 제목": item["movieNm"],
                "개봉일": item.get("openDt") or "-",
                "관객 수": int(item.get("audiCnt", 0) or 0),
                "누적 관객 수": int(item.get("audiAcc", 0) or 0),
                "매출액": int(item.get("salesAmt", 0) or 0),
                "매출 점유율(%)": float(item.get("salesShare", 0) or 0),
                "전일 대비 변동": int(item.get("rankInten", 0) or 0),
            }
        )

    df = pd.DataFrame(records)
    if not df.empty:
        df = df.sort_values("순위").set_index("순위")
    return df


def main() -> None:
    st.set_page_config(page_title="박스오피스 대시보드", page_icon="🎬", layout="wide")
    st.title("🎬 영화 박스오피스 대시보드")
    st.caption("날짜를 선택하고 KOBIS API 키를 입력해 일간 박스오피스 Top 10을 확인하세요.")

    # Secrets > env > manual input 순으로 API 키를 채운다.
    # Secrets > env > manual input 순으로 API 키를 채운다.
    preset_api_key = os.getenv("KOBIS_API_KEY", "")
    try:
        if "KOBIS_API_KEY" in st.secrets:
            preset_api_key = st.secrets["KOBIS_API_KEY"]
    except Exception:
        # st.secrets는 Streamlit 환경 외부에서는 접근 시 예외가 날 수 있음
        pass

    with st.sidebar:
        st.subheader("🔑 API 설정")
        api_key = st.text_input("KOBIS API Key", value=preset_api_key, type="password")
        st.caption("`.streamlit/secrets.toml` 또는 환경 변수 KOBIS_API_KEY에 설정하면 자동으로 불러옵니다.")

    col1, col2 = st.columns([2, 1])
    with col1:
        selected_date = st.date_input(
            "조회 날짜",
            value=get_default_date(),
            max_value=get_default_date(),
            help="KOBIS는 과거 날짜 데이터만 제공합니다. 기본값은 어제입니다.",
        )
    with col2:
        st.write("")  # spacer
        fetch_clicked = st.button("순위 조회하기", type="primary")

    if fetch_clicked:
        if not api_key:
            st.error("API 키를 입력해주세요. (환경 변수 KOBIS_API_KEY 또는 사이드바 입력)")
            return

        with st.spinner("데이터를 불러오는 중..."):
            try:
                df = fetch_box_office(api_key, selected_date)
            except requests.HTTPError as exc:
                st.error(f"API 호출에 실패했습니다. 상태 코드: {exc.response.status_code}")
                return
            except requests.RequestException as exc:
                st.error(f"네트워크 오류가 발생했습니다: {exc}")
                return
            except ValueError:
                st.error("응답 데이터를 처리하는 중 문제가 발생했습니다.")
                return

        if df.empty:
            st.warning("조회된 데이터가 없습니다. 날짜를 다시 선택하거나 잠시 후 시도해주세요.")
            return

        st.success(f"{selected_date.strftime('%Y년 %m월 %d일')} 일간 박스오피스 Top 10 결과입니다.")

        chart_data = df.reset_index()
        st.bar_chart(chart_data, x="영화 제목", y="관객 수", height=400)

        st.subheader("상세 데이터")
        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()
