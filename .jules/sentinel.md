## 2026-10-09 - [Local SQLite Initialization TOCTOU]
**Vulnerability:** `os.remove()` is called before `sqlite3.connect()` in `db.py`. A local attacker could create a symbolic link or a file at `DB_PATH` between these two calls, potentially leading to unauthorized access, denial of service, or arbitrary file overwrite.
**Learning:** Local file operations (deletion followed by creation) must be done securely to avoid Time-of-Check to Time-of-Use (TOCTOU) race conditions.
**Prevention:** Use `os.open` with `os.O_CREAT | os.O_EXCL` flags for atomic creation when sensitive files are involved, or strictly manage permissions.
