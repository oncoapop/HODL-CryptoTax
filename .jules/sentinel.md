## 2024-09-07 - [Insecure SQLite File Permissions]
**Vulnerability:** SQLite database file (`cytotax.db`) storing sensitive financial data was created with default OS permissions, allowing read/write access to other users on the system.
**Learning:** `sqlite3.connect()` creates files with default umask permissions, which is often too permissive (e.g. `644`) for local databases containing sensitive user data.
**Prevention:** Pre-create the database file with strict OS-level permissions (e.g., `0o600` via `os.open(DB_PATH, os.O_CREAT | os.O_RDWR, 0o600)`) before connecting with `sqlite3`.
