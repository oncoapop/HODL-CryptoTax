## 2026-09-15 - Secure Database Creation
**Vulnerability:** Local SQLite database file containing sensitive financial transactions was created using `sqlite3.connect` with default file permissions, allowing read/write access to any user on the system depending on umask.
**Learning:** `sqlite3.connect` respects the system umask and does not provide an option to explicitly set strict permissions on database creation. It is vulnerable to Time-of-Check to Time-of-Use (TOCTOU) if not careful.
**Prevention:** Pre-create the database file using `os.open(DB_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)` and handle the `FileExistsError` to ensure strict permissions (read/write only by owner).
