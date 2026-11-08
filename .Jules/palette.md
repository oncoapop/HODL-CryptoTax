## 2024-05-14 - Improve empty state for DataFrames
**Learning:** Streamlit DataFrames display as confusing blank tables when empty, which is a poor micro-UX for users starting with fresh databases.
**Action:** Use `df.empty` to conditionally render a helpful `st.info` empty state message instead of the raw `st.dataframe`.
