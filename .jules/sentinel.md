## 2023-10-06 - Insecure SQLite Database Permissions & TOCTOU
**Vulnerability:** The SQLite database `cytotax.db` containing sensitive financial data was created with default, overly permissive system permissions, and the check-then-create logic was vulnerable to Time-of-Check to Time-of-Use (TOCTOU) race conditions.
**Learning:** Using standard `sqlite3.connect()` creates files using the default umask. Explicit file descriptor handling via `os.open()` with `os.O_CREAT | os.O_EXCL` is necessary to guarantee safe file creation, atomic operations, and strict 0o600 permissions.
**Prevention:** Pre-create sensitive local files using `os.open()` with explicit mode flags and `O_EXCL` before accessing them with higher-level library APIs.
