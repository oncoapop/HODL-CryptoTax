## 2024-10-12 - Empty State Helpful Messages
**Learning:** Streamlit displays confusing blank tables when a pandas DataFrame is empty.
**Action:** Always check `df.empty` and provide a helpful empty state message using `st.info` when the dataset is empty, guiding the user on how to populate the data.
