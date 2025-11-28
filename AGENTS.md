# AGENTS.md - Codex Instructions

## 🤖 Role & Objective
You are **Codex**, an AI developer tasked with building a **Streamlit + OpenAPI Playground**. 
This project is based on **Chapter 16 (CH16)**, which covers:
1.  **Open API Integration**: Fetching external data (e.g., Movie Box Office) using APIs.
2.  **Web Crawling**: Scraping data (e.g., News) using Playwright when APIs are unavailable.
3.  **Visualization**: Displaying data using Streamlit charts and tables.

## 🧠 Memory Bank & Context Management
To maintain context across sessions, we use a **Memory Bank** structure in the `memory-bank/` directory.
**Rules for Codex:**
1.  **Start of Session**: Read `memory-bank/activeContext.md` and `memory-bank/projectbrief.md` to understand the current state.
2.  **During Work**: Check `memory-bank/techContext.md` for constraints and libraries.
3.  **End of Session**: Update `memory-bank/activeContext.md` with what was accomplished and what is next.

## 🛠 Project Roadmap
### Phase 1: Environment & Setup
- [ ] Create virtual environment (if not exists).
- [ ] Install dependencies: `streamlit`, `requests`, `pandas`, `playwright`.
- [ ] Configure `.gitignore` (Done).

### Phase 2: Box Office Dashboard (API)
- [ ] Implement `app.py` based on [CH16] > [Streamlit으로 3분 만에 만드는 영화 대시보드].
- [ ] Features:
    - Date picker input.
    - Fetch KOBIS Box Office API.
    - Display Bar Chart (Audience Count).
    - Display Data Table.
    - **Note**: Use a placeholder or environment variable for `YOUR_API_KEY`.

### Phase 3: News Scraper (Crawler)
- [ ] Implement `news_crawler.py` (or integrate into Streamlit) based on [CH16] > [Playwright MCP].
- [ ] Features:
    - Input keywords (e.g., "AI", "Metaverse").
    - Scrape Naver News titles/links.
    - Display results in the app or save to CSV.

## 📂 Directory Structure
```
.
├── .gitignore
├── AGENTS.md
├── CH16.md
├── memory-bank/          # Context storage
│   ├── activeContext.md
│   ├── productContext.md
│   ├── projectbrief.md
│   ├── systemPatterns.md
│   └── techContext.md
├── app.py                # Main Streamlit App (To be created)
└── requirements.txt      # Dependencies (To be created)
```

