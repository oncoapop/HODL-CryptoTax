## 2024-11-04 - Secure SQLite initialization and TOCTOU prevention
**Vulnerability:** The sqlite database was initialized insecurely (default permissions) and had a TOCTOU race condition during recreation (`if os.path.exists` followed by `os.remove`).
**Learning:** SQLite doesn't natively provide permission control for db files. We must manually create the file with strict permissions (0o600) before letting SQLite connect. Using `if os.path.exists` is prone to race conditions, so it's better to try to remove and catch `FileNotFoundError`.
**Prevention:** Use `try: os.remove(path) except FileNotFoundError: pass` for deletion. Pre-create sensitive files with `os.open(path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)` before interacting with them.
