## 2024-11-04 - Blank Streamlit Dataframes
**Learning:** Streamlit dataframes render poorly (as blank UI components) when empty, which creates a confusing user experience.
**Action:** Always check if a dataframe is empty (using `df.empty`) before rendering it with `st.dataframe`. If empty, render a helpful `st.info` message with guidance instead.
