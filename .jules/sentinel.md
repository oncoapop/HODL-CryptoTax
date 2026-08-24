## 2026-08-24 - [Avoid Weak Hashing for Deduplication]
**Vulnerability:** The codebase was using `hashlib.md5()` to calculate file hashes for deduplicating CSV transaction imports. MD5 is a weak, collision-prone hashing algorithm.
**Learning:** Even for non-cryptographic purposes like simple file deduplication, using weak hashing algorithms triggers static analysis (bandit) high-severity flags and introduces unnecessary risk if malicious identical-hash files are supplied.
**Prevention:** Always use cryptographically secure hashing functions (like SHA-256 via `hashlib.sha256()`) for hashing operations to maintain defense in depth and keep security scanners happy.
