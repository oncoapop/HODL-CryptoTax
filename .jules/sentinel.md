## 2026-09-11 - [TOCTOU Vulnerability in Database Initialization]
**Vulnerability:** Local file access vulnerability due to default permissive file permissions when creating a SQLite database.
**Learning:** `sqlite3.connect(DB_PATH)` creates the file with default mask, exposing sensitive financial data in local environments. This creates a TOCTOU race if one tries to change permissions *after* creating it.
**Prevention:** Pre-create sensitive local files using `os.open` with `os.O_CREAT | os.O_EXCL | os.O_RDWR` and strict permissions (e.g. `0o600`) before connecting with `sqlite3.connect`. Wrap in `try...except FileExistsError`.
