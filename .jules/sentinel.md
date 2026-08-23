## 2024-08-23 - Avoid Weak Hashes for Non-Cryptographic Purposes

**Vulnerability:** The use of `hashlib.md5()` was flagged by the security scanner (bandit) with a `B324:hashlib` warning, as MD5 is considered a weak hash function and is vulnerable to collision attacks. Even though it was used only for file deduplication (non-cryptographic), security tooling flags it as a vulnerability.

**Learning:** Static analysis tools like `bandit` will flag `md5` usage. To prevent warnings and ensure best practices, we should use modern hashes like `sha256` by default for non-performance critical hashing, or use `usedforsecurity=False` when instantiating the MD5 hash if MD5 must be used (available in Python 3.9+).

**Prevention:** Default to `hashlib.sha256()` instead of `hashlib.md5()` for tasks like generating file checksums or deduplication in Python.
