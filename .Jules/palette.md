## 2024-10-13 - [Empty States in Streamlit DataFrames]
**Learning:** Empty pandas dataframes in Streamlit dashboards display as confusing blank tables if not handled explicitly.
**Action:** Always check `if df.empty` and render a helpful `st.info` message with guidance instead of a blank table.
