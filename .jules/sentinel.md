## 2026-09-29 - [TOCTOU in DB Initialization]
**Vulnerability:** Local privilege escalation/information disclosure via insecure SQLite file creation and Time-of-Check to Time-of-Use (TOCTOU) race condition.
**Learning:** Checking for file existence before creation without atomic operations allows an attacker to create a symlink or file in the gap, leading to writing data to unintended locations or giving unauthorized access. Also, SQLite does not enforce strict permissions on new DB files.
**Prevention:** Use os.open with os.O_CREAT | os.O_EXCL | os.O_RDWR and 0o600 permissions. If FileExistsError is caught, fail securely instead of proceeding.
