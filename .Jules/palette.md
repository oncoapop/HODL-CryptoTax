## 2024-10-27 - Empty States for Dataframes
**Learning:** Streamlit renders completely blank tables when rendering an empty pandas DataFrame using st.dataframe(). This causes a confusing experience for users.
**Action:** Always check `df.empty` before rendering dataframes in Streamlit, and show a helpful `st.info` empty state message instead.
