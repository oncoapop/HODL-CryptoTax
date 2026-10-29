## 2024-05-15 - Streamlit Empty States for DataFrames
**Learning:** Displaying empty pandas DataFrames in Streamlit results in confusing blank tables that don't give the user clear feedback on why the data is missing.
**Action:** Always check `df.empty` before rendering a DataFrame and display a helpful `st.info` message with guidance if it is empty.
