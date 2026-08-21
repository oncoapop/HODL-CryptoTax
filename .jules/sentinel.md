## 2024-05-18 - [Fix Weak Hash]
**Vulnerability:** Weak MD5 hash being used for file hashing/deduplication in `src/importer.py`
**Learning:** `hashlib.md5()` was flagged by Bandit as a high severity issue due to known collision vulnerabilities. Although used here just for file deduplication rather than security, using a weak cryptographic hash can set a bad precedent and trigger static analysis tools unnecessarily.
**Prevention:** Use stronger cryptographic hashes like SHA-256 (`hashlib.sha256()`) by default in Python projects for generic hashing needs, or use `usedforsecurity=False` (for Python 3.9+) if there's a strict requirement for a fast non-cryptographic hash algorithm.
