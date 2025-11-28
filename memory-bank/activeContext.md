# Active Context

## Current Session
-   **Date**: 2025-11-28
-   **Goal**: Build the Streamlit 박스오피스 대시보드 and wire it to the KOBIS API.

## Recent Changes
-   Added `requirements.txt` with `streamlit`, `requests`, and `pandas`.
-   Implemented `app.py` for the 박스오피스 대시보드: date picker defaulting to 어제, sidebar API key input (env-backed), KOBIS fetch with caching/error handling, bar chart of Top 10 audience counts, and detailed dataframe output.
-   Verified syntax via `python3 -m compileall app.py`.
-   Updated `README.md` to use `uv` for package management and app execution (no venv steps), added quick install snippet and `uv run` usage.
-   Added support for `.streamlit/secrets.toml` KOBIS_API_KEY fallback (no export needed) and documented secrets-based setup in README.
-   Fixed API key preload to use `st.secrets["KOBIS_API_KEY"]` safely (supports secrets when running via `streamlit run`).

## Next Steps
1.  Run `uv run streamlit run app.py` to manually verify the UI and data flow with a valid API key (set `.streamlit/secrets.toml` or `KOBIS_API_KEY`, or use sidebar input).
2.  Extend Chapter 16 scope by adding the news scraper (Playwright) when ready.
3.  Consider adding lightweight tests or mocks for the API layer to catch formatting regressions.
