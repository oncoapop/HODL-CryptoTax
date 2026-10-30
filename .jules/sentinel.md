## 2024-05-24 - Secure SQLite DB Initialization
**Vulnerability:** Time-of-Check to Time-of-Use (TOCTOU) race condition when checking and deleting `cytotax.db`, combined with insecure default file permissions allowing unauthorized local read/write access.
**Learning:** Using `os.path.exists()` before `os.remove()` is vulnerable to race conditions. Furthermore, SQLite doesn't natively create databases with strict OS-level permissions by default.
**Prevention:** Use a `try...except FileNotFoundError` for deletion, and explicitly pre-create the DB file with `os.open()` using `O_CREAT | O_EXCL` and `0o600` permissions. Catch `FileExistsError` to thwart TOCTOU attacks.
