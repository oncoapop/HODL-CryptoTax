## 2024-05-18 - [Streamlit UX and Deprecation Warnings]
**Learning:** Long blocking tasks initiated by UI buttons require explicit visual feedback (like `st.spinner`) to prevent the UI from appearing frozen. Additionally, Streamlit has deprecated `use_container_width=True` in favor of `width="stretch"`.
**Action:** Always wrap blocking backend operations triggered by UI elements in a loading indicator. Check runtime logs for deprecation warnings related to layout properties and update them to current standards.
