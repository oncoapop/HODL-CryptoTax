## 2024-09-04 - SQLite Local File Permissions
**Vulnerability:** SQLite database file created without strict file permissions, potentially exposing sensitive financial data to unauthorized local users.
**Learning:** Python's sqlite3 driver does not automatically enforce strict permissions (e.g. 0o600) on newly created local database files. Explicit creation with restricted permissions using `os.open` is required before establishing a database connection.
**Prevention:** Pre-create sqlite database files with strict file permissions before initial use when the database contains sensitive data.
