## 2024-11-07 - Secure SQLite Database Initialization

**Vulnerability:** A Time-of-Check to Time-of-Use (TOCTOU) vulnerability existed in `src/db.py` where `os.path.exists` was followed by `os.remove`, and the SQLite database was initialized without strict permissions.
**Learning:** Checking for file existence before acting on it in Python is prone to TOCTOU attacks. Additionally, SQLite files created by default may have permissive permissions, exposing sensitive financial data.
**Prevention:** Avoid `os.path.exists` for files. Instead, use a `try: os.remove(path) except FileNotFoundError: pass` block. Pre-create sensitive database files using `os.open(..., os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)` to securely enforce permissions and prevent concurrent creation.
