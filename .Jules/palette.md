## 2024-05-24 - Streamlit Empty States
**Learning:** Streamlit `st.dataframe` renders confusing blank tables when passed an empty pandas DataFrame.
**Action:** Always check `df.empty` before rendering a dataframe and use `st.info` to provide a helpful empty state message instead.
