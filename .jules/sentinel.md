## 2023-10-11 - [Secure SQLite DB initialization]
**Vulnerability:** The SQLite database `cytotax.db` was created with default permissions and was vulnerable to a Time-of-Check to Time-of-Use (TOCTOU) race condition because it just deletes the DB file and connects to it, not preventing unauthorized access.
**Learning:** By pre-creating the database file with `os.open(DB_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)` and handling `FileExistsError`, we can ensure secure initialization and mitigate TOCTOU vulnerabilities. Strict permissions (0o600) protect local data.
**Prevention:** Always use `os.open` with `O_CREAT | O_EXCL` flags and apply strict file permissions when handling sensitive local databases. Ensure to fail securely if the file gets created simultaneously.
