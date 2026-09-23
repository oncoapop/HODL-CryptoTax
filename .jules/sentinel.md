## 2024-10-24 - Secure Database Initialization TOCTOU Vulnerability
**Vulnerability:** The SQLite database initialization in `src/db.py` created the `cytotax.db` file without explicit permission restrictions, leaving the database readable/writable by unauthorized system users. Also, deleting and re-creating it had a Time-of-Check to Time-of-Use (TOCTOU) race condition.
**Learning:** Sensitive local SQLite database files need to be explicitly created with strict permissions (`0o600`).
**Prevention:** Always use `os.open(path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)` wrapped in a `try...except FileExistsError` block when initially creating sensitive local databases to ensure restricted permissions and prevent TOCTOU attacks.
