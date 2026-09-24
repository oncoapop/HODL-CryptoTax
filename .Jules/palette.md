
## 2024-05-14 - Handle Empty DataFrames in Streamlit
**Learning:** Displaying empty pandas DataFrames in Streamlit (e.g., using `st.dataframe`) results in a confusing blank space or an unhelpful column header layout.
**Action:** Always check if a DataFrame is empty using `df.empty` before rendering it. If empty, render a helpful empty state message (using `st.info` or similar) directing the user on how to populate the data.
