## 2024-05-23 - Added Loading Feedback to Ingestion Action
**Learning:** Adding a spinner to long-running Streamlit actions prevents users from repeatedly clicking buttons by providing immediate visual feedback.
**Action:** Always wrap long-running Streamlit operations with `st.spinner()` and consider using `type="primary"` for major actions. Note: Use `use_container_width=True` for full-width buttons in this older Streamlit version.
