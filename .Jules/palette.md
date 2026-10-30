## 2024-05-24 - Empty States Added
**Learning:** Displaying blank dataframes for empty data sets creates a confusing experience for the user. Adding explicit messages guiding the user to action is better.
**Action:** Implemented `st.info` blocks when `df.empty` is true.
