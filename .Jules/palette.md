## 2024-10-06 - Streamlit Empty State UX
**Learning:** Displaying empty dataframes in Streamlit creates confusing UI (blank tables).
**Action:** Always check `if df.empty:` and render helpful `st.info` guidance before attempting to display a dataframe.
