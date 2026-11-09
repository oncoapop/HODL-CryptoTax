## 2024-11-20 - Empty state messages for DataFrames in Streamlit
**Learning:** In Streamlit dashboards displaying pandas DataFrames natively, empty datasets render as confusing blank tables.
**Action:** Implement explicit `df.empty` checks and render helpful empty state messages (e.g., using `st.info` with guidance) to improve user experience.
