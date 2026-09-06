## 2026-09-06 - [Strict File Permissions for SQLite Local Database]
**Vulnerability:** The SQLite database `cytotax.db` containing sensitive local financial transactions is initialized without explicit file permission constraints, allowing any user on the shared system to potentially access or modify this data.
**Learning:** Default file creation by `sqlite3` leaves files with open permissions (based on environment umask), increasing the blast radius if an attacker gets read access to the local machine context.
**Prevention:** Pre-create the local database file using `os.open` with strict `0o600` flags (`os.O_CREAT | os.O_RDWR`) before performing the standard database connection to enforce secure ownership automatically upon creation.
