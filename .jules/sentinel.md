## 2024-10-06 - Secure SQLite Database Creation
**Vulnerability:** SQLite database file was created with default permissions (often `0o644`), which might allow unauthorized local users to read sensitive transaction data. The check-then-create pattern also suffered from a Time-of-Check to Time-of-Use (TOCTOU) vulnerability.
**Learning:** Default file creation by sqlite3 is not secure for sensitive data on multi-user systems. Deleting and recreating files must be done securely to avoid TOCTOU races.
**Prevention:** Always use `os.open` with `os.O_CREAT | os.O_EXCL` and `0o600` permissions when creating sensitive local database files to ensure strict ownership and prevent race conditions. Explicitly handle `FileExistsError` to abort on TOCTOU.
