## 2024-10-03 - Streamlit Empty DataFrame Handling
**Learning:** Streamlit renders blank, confusing table shells when passing an empty pandas DataFrame to `st.dataframe()`. It does not have a built-in "empty state" property.
**Action:** Always check `df.empty` before rendering `st.dataframe` and display a helpful `st.info()` message with guidance instead.
