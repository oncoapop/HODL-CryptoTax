## 2026-09-09 - [Insecure SQLite File Creation]
**Vulnerability:** SQLite database file `cytotax.db` containing sensitive financial data was being created with default file permissions, and it was vulnerable to Time-of-Check to Time-of-Use (TOCTOU) race conditions if another user creates the file just before SQLite tries to.
**Learning:** Default SQLite behavior doesn't enforce strict file permissions, potentially exposing tax and crypto transaction data to other users on a shared system.
**Prevention:** Pre-create the database file using `os.open` with `os.O_CREAT | os.O_EXCL` flags and strict permissions (`0o600`) inside a `try...except FileExistsError:` block before calling `sqlite3.connect()`.
