## 2024-11-11 - [Secure File Creation and TOCTOU]
**Vulnerability:** A Time-of-Check to Time-of-Use (TOCTOU) vulnerability existed during SQLite database initialization, combined with insecure default file permissions.
**Learning:** Checking for file existence before deletion (`if os.path.exists`) allows an attacker to swap files between the check and deletion. Relying on default SQLite permissions leaves the file open to unauthorized local readers.
**Prevention:** Use atomic operations like `try/except FileNotFoundError` for deletion. Pre-create the database file securely using `os.open` with `O_CREAT | O_EXCL` and `0o600` permissions before passing it to `sqlite3.connect()`.
