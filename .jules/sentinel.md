## 2024-05-15 - [Weak Hashing Algorithm Replaced]
**Vulnerability:** Weak MD5 hash used in file deduplication in `src/importer.py`. Hardcoded local windows path for CSV import exposing local filesystem path structure.
**Learning:** `hashlib.md5()` is a weak cryptographic hash and throws a Bandit B324 error. Absolute paths expose internal paths which can be a minor information leakage risk or lead to environment-specific errors.
**Prevention:** Use stronger hashes like `hashlib.sha256()` instead. Use `os.path.join(os.path.dirname(__file__), ...)` to build paths relative to the current file rather than hardcoding local specific user paths.
