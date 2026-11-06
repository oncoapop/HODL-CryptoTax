## 2024-05-15 - Streamlit Empty States UX
**Learning:** Streamlit displays confusing blank, empty tables when pandas DataFrames are empty, which can make users think the application is broken rather than just missing data.
**Action:** Always check `df.empty` before rendering `st.dataframe` and provide a helpful `st.info` call-to-action instead.
