## 2026-10-03 - [Secure SQLite DB Creation]
**Vulnerability:** TOCTOU (Time-of-Check to Time-of-Use) race condition and overly permissive default file permissions when creating local SQLite databases.
**Learning:** Checking for file existence and then creating it leaves a window for race conditions. SQLite databases created by default can have permissive read/write access.
**Prevention:** Use `os.open` with `os.O_CREAT | os.O_EXCL | os.O_RDWR` and strict permissions `0o600` to atomically create the file, explicitly raising an error if it fails.
