## Sentinel Journal

## 2026-09-01 - [Insecure Database File Permissions]
**Vulnerability:** The SQLite database `cytotax.db` used for storing sensitive financial transaction records was created with default permissions, making it readable by all users.
**Learning:** Default file creation doesn't ensure strict read/write constraints.
**Prevention:** Pre-create local databases using `os.open` with strict flags (`os.O_CREAT | os.O_RDWR, 0o600`) before establishing connections using `sqlite3`.
