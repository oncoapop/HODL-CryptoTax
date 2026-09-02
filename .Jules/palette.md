## 2026-09-02 - Empty DataFrames UI Improvement
**Learning:** Rendering an empty DataFrame via `st.dataframe` presents users with a confusing, blank table without proper context, negatively impacting the UX.
**Action:** When a Pandas DataFrame `.empty` check returns true, use `st.info` with a helpful call-to-action or context instead of attempting to render the table. This clarifies the system state directly to the user.
