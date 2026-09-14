## 2026-09-14 - Insecure Database File Creation
**Vulnerability:** SQLite database (`cytotax.db`) was created implicitly by `sqlite3.connect()` with default permissive file permissions, allowing unauthorized local users to access sensitive financial data (Time-of-Check to Time-of-Use / TOCTOU).
**Learning:** In desktop/local tools storing sensitive data, databases must be initialized with strict `0o600` permissions (read/write only by owner) prior to connection.
**Prevention:** Pre-create the database file using `os.open()` with `os.O_CREAT | os.O_EXCL | os.O_RDWR` and `0o600` permissions inside a `try...except FileExistsError` block before passing the path to `sqlite3.connect()`.
