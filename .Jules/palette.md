## 2025-02-15 - Streamlit Empty State DataFrames
**Learning:** Displaying empty dataframes in Streamlit presents confusing blank tables. It is critical to render explicit empty states using `st.info()` or similar when datasets are empty.
**Action:** Always check `df.empty` before rendering a table and supply a helpful fallback message.
