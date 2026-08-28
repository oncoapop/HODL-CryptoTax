## 2026-08-28 - Update insecure hashlib usage
**Vulnerability:** MD5 used for file hashing and deduplication, which is weak and susceptible to collision attacks (CWE-327).
**Learning:** File duplication checks shouldn't use weak hashes like MD5, especially when dealing with financial/tax user data.
**Prevention:** Use stronger hashing algorithms like SHA-256 for file duplication checks.
