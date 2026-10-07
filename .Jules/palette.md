## 2024-10-07 - Add Helpful Empty States to Dataframes
**Learning:** Displaying empty dataframes in Streamlit can be confusing to users. A better UX is to check for empty datasets (`df.empty`) and display a helpful `st.info` message with a clear call-to-action explaining how to populate the data.
**Action:** Always check `df.empty` before rendering dataframes in Streamlit, and fallback to informational alerts.
