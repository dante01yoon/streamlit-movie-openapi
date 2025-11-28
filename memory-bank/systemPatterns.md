# System Patterns

## Architecture
-   **Frontend**: Streamlit (Python-based web UI).
-   **Backend Logic**: Python scripts embedded in Streamlit app.
    -   `requests` for API calls.
    -   `playwright` for scraping (async).
-   **Data Processing**: `pandas` DataFrames.

## Design Patterns
-   **Single Script App**: The entire dashboard logic primarily resides in `app.py` for simplicity (Streamlit model).
-   **Function Separation**: Separate data fetching (`get_boxoffice_data`) from UI rendering.
-   **Error Handling**: Use `try-except` blocks and Streamlit's `st.error` / `st.warning` for user feedback.
-   **Configuration**: API keys should be managed via `st.secrets` or environment variables, not hardcoded.

## Directory Structure
-   `memory-bank/`: Context documentation.
-   `app.py`: Main application entry point.
-   `requirements.txt`: Python dependencies.

