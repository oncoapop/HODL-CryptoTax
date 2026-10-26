## 2024-10-26 - [File Permissions for SQLite Database]
**Vulnerability:** The SQLite database `cytotax.db` containing sensitive transaction data could be accessible to other users on a shared system.
**Learning:** `os.path.exists` followed by `os.remove` is susceptible to a TOCTOU race condition. Pre-creating the file using `os.open` with `O_CREAT | O_EXCL` and secure permissions (0o600) prevents other users from accessing it, and gracefully handling `FileNotFoundError` during deletion mitigates the TOCTOU issue.
**Prevention:** Use `try: os.remove(...) except FileNotFoundError: pass` for deletion. Create files containing sensitive data with `0o600` permissions.
