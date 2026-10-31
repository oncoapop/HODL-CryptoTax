## 2026-10-31 - Secure File Creation and TOCTOU Prevention
**Vulnerability:** The SQLite database file was being created with default permissions, and its previous deletion was vulnerable to a Time-of-Check to Time-of-Use (TOCTOU) race condition using `os.path.exists()`.
**Learning:** Checking for file existence before deletion allows an attacker to manipulate the file system between the check and the action. Creating database files with default permissions can expose sensitive financial data locally.
**Prevention:** Use `try/except FileNotFoundError` for deletion. Create files using `os.open` with strict permissions (`0o600`) and the `os.O_CREAT | os.O_EXCL` flags to ensure atomic, secure creation.
