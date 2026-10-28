## 2024-03-24 - Streamlit Empty States for DataFrames
**Learning:** Streamlit renders completely blank white spaces when displaying empty Pandas DataFrames, which is confusing for users. Checking `df.empty` and rendering an `st.info` block instead provides a much better micro-UX empty state.
**Action:** Always check `df.empty` before `st.dataframe()` when writing Streamlit data apps to render helpful CTA empty states.
