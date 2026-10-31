## 2023-11-01 - Render helpful empty states instead of blank DataFrames
**Learning:** In Streamlit dashboards displaying pandas DataFrames, check for empty datasets using `df.empty` and render helpful empty state messages (e.g., using `st.info` with guidance) instead of displaying confusing blank tables.
**Action:** Always check `df.empty` before calling `st.dataframe` when displaying data that could be empty.
