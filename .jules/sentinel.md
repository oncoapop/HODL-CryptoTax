## 2024-11-06 - TOCTOU and Insecure SQLite DB Permissions
**Vulnerability:** A TOCTOU race condition existed during database initialization, and the SQLite file was created with default loose permissions.
**Learning:** Always use atomic operations (`try-except` on file creation/deletion) and `os.open` with `0o600` for sensitive database files.
**Prevention:** Ensure tight local permissions for SQLite databases, specifically explicitly setting `0o600` flags and handling `FileExistsError`.
