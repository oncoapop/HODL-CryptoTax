## 2024-11-07 - Empty States for DataFrames in Streamlit
**Learning:** Streamlit renders completely blank tables when a pandas DataFrame is empty (`df.empty`), which confuses users who might think the table is broken or still loading.
**Action:** Always check `if df.empty:` before calling `st.dataframe()` and render a helpful `st.info()` message guiding the user on how to populate the data.
