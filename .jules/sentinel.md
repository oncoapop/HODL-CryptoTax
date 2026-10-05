## 2024-05-24 - [Fix TOCTOU vulnerability and enforce strict DB permissions]
**Vulnerability:** The SQLite database was being created using default permissions after removing the old one, creating a Time-of-Check to Time-of-Use (TOCTOU) race condition and resulting in overly permissive file permissions.
**Learning:** Always use `os.open` with `os.O_CREAT | os.O_EXCL` and explicitly specify secure permissions (like `0o600` for databases) before connecting using higher-level abstractions like `sqlite3`. Wrap the creation in a try-except block and securely fail if `FileExistsError` is raised.
**Prevention:** Pre-create files securely before handing them to libraries that rely on default permissions.
