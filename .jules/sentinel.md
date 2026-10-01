## 2023-10-24 - Initial Setup
**Vulnerability:** N/A
**Learning:** N/A
**Prevention:** N/A

## 2024-10-24 - Secure SQLite DB Initialization
**Vulnerability:** SQLite database (`cytotax.db`) was created with default world-readable permissions (0o644) containing sensitive financial tax data.
**Learning:** `sqlite3.connect()` creates files with default umask. Must pre-create the file securely with `os.open` and 0o600 permissions, handling `FileExistsError` by raising to prevent TOCTOU race condition attacks.
**Prevention:** Pre-create local DB files with `os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600` before SQLite connects.
