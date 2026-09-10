## 2024-09-10 - Empty States for Streamlit DataFrames
**Learning:** In Streamlit applications, displaying empty pandas DataFrames using `st.dataframe()` can lead to confusing UI for end-users, rendering a blank block without context. Empty states are essential to clarify that a section relies on yet-to-be-imported data.
**Action:** When working with Streamlit dashboards displaying pandas DataFrames, always check `df.empty` and use `st.info` or similar informative elements to render an empty state message before falling back to displaying the DataFrame itself.
