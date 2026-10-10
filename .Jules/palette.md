## 2024-05-24 - Add Helpful Empty States to DataFrames
**Learning:** Streamlit dataframes render as confusing blank blocks when pandas DataFrames are empty. Adding explicit `df.empty` checks with `st.info` messages provides clear guidance to users on how to populate the data.
**Action:** Always verify if a dataframe might be empty before passing it to `st.dataframe` and provide actionable fallback UI.
