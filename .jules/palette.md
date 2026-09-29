## 2024-05-18 - Handling empty DataFrames in Streamlit
**Learning:** Displaying an empty DataFrame without context causes confusion, as the UI simply shows an empty space or a bare table outline. Checking `df.empty` and replacing the empty table with a helpful state message gives users clear guidance on how to populate the dataset.
**Action:** Always check `df.empty` before rendering DataFrames in Streamlit, and substitute empty states with `st.info` blocks containing actionable instructions.
