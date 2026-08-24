## 2026-08-24 - Adding loading states to blocking Streamlit operations
**Learning:** Streamlit blocks the UI during synchronous operations like data ingestion. Without a loading indicator, users might click multiple times or think the app crashed.
**Action:** Always wrap blocking operations (e.g., CSV imports, database rebuilds) in `with st.spinner('...')` to provide immediate visual feedback.
