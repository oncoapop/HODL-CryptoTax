## 2026-09-21 - Empty states for Streamlit DataFrames
**Learning:** Blank tables in Streamlit can be confusing to users. Checking `df.empty` and providing a helpful `st.info` message with clear guidance significantly improves the UX.
**Action:** Always verify if a DataFrame can be empty before rendering it, and provide a helpful empty state instead.
