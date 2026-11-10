## 2024-11-10 - Secure SQLite Database Initialization
**Vulnerability:** The database initialization used a TOCTOU-vulnerable check (`if exists: remove`) and created the database file with default (overly permissive) system permissions.
**Learning:** SQLite doesn't offer a native way to set strict permissions on creation. Attackers could theoretically race the initialization to pre-create a symlink or read the newly created DB before data is inserted if run in a shared environment.
**Prevention:** Use `try...except FileNotFoundError` for deletion and pre-create the DB file using `os.open` with `O_CREAT | O_EXCL | O_RDWR` and `0o600` permissions.
