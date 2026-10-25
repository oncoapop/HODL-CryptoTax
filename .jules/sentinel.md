## 2026-10-25 - [Fix TOCTOU and Insecure DB Creation]
**Vulnerability:** The SQLite database was being deleted using an insecure `if os.path.exists` check, leading to a Time-of-Check to Time-of-Use (TOCTOU) race condition. Also, the db file was created with default OS permissions which could allow unauthorized local access.
**Learning:** Using `os.path.exists` before deletion is prone to race conditions. Using default sqlite3 connection to create databases uses default umask permissions.
**Prevention:** Always use a `try...except FileNotFoundError` for deletions. Explicitly pre-create sensitive local SQLite database files with `os.open` and strict `0o600` permissions before passing them to the sqlite driver.
