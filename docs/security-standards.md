
### `docs/security-standards.md`
```md
# Security Standards (Baseline)

- Secrets: never stored in repo; `.env` is local only.
- Auth: default deny (all endpoints require auth unless explicitly public).
- Logging: do not log sensitive data (PII/PHI). Use request IDs for tracing.
- Audit events: auth events, exports, admin/config changes, permission changes.
