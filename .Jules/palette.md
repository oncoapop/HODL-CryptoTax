## 2023-10-27 - [Empty States in Streamlit]
**Learning:** Streamlit dataframes (`st.dataframe`) render as confusing, small blank boxes when populated with empty Pandas DataFrames.
**Action:** Always check `if df.empty:` before rendering dataframes, and provide a helpful fallback state using `st.info` or `st.warning` that guides the user on how to populate the data.
