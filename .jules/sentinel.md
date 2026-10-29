## 2026-10-29 - Secure SQLite Database Initialization
**Vulnerability:** TOCTOU race condition during database file deletion and insecure default file permissions when creating local SQLite databases.
**Learning:** Using `os.path.exists` followed by `os.remove` creates a race condition. Also, allowing SQLite to lazily create the file results in default permissions, which might be too permissive for sensitive tax data.
**Prevention:** Use `try/except FileNotFoundError` around `os.remove`. Pre-create the database file securely using `os.open` with `O_CREAT | O_EXCL` and `0o600` permissions before connecting with sqlite3.
