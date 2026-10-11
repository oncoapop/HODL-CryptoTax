## 2024-05-30 - Added Empty States to Streamlit DataFrames
**Learning:** Streamlit displays confusing blank tables when rendering empty pandas DataFrames, which can look like a rendering error or missing data rather than an intended empty state.
**Action:** Always check `df.empty` before rendering a DataFrame in Streamlit, and use `st.info()` to display a helpful empty state message explaining why the data is missing and how the user can populate it.
