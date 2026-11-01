## 2024-05-24 - Empty DataFrame States
**Learning:** Rendering an empty pandas DataFrame in Streamlit (`st.dataframe(df)`) displays an ugly, confusing blank table with column headers but no content. This is poor UX when users haven't uploaded data yet.
**Action:** Always check `if df.empty:` before rendering DataFrames in Streamlit, and fallback to rendering a helpful `st.info()` message directing the user on what action to take.
