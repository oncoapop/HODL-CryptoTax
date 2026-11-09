## 2026-11-09 - Secure Database Initialization
**Vulnerability:** Insecure default file permissions (0o644) for local SQLite database and Time-of-Check to Time-of-Use (TOCTOU) vulnerability during database recreation.
**Learning:** Using `os.path.exists()` before `os.remove()` leaves a race condition window. Default `sqlite3.connect()` creates files with overly permissive OS defaults, exposing sensitive tax data to local users.
**Prevention:** Use `try: os.remove() except FileNotFoundError` for atomic deletion, and explicitly create the file descriptor with strict `0o600` permissions (`os.open(..., 0o600)`) before connecting with SQLite.
