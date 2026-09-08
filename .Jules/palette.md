## 2024-09-08 - Helpful empty states for Streamlit DataFrames
**Learning:** By default, Streamlit renders empty pandas DataFrames as awkward blank tables that offer no user guidance.
**Action:** Always check `df.empty` before calling `st.dataframe()` and use `st.info()` with a call-to-action (e.g., "Please import transactions") to create an accessible empty state.
