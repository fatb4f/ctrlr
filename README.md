# Codex execution conventions

- Worktrees: `.codex/.worktrees/<packet_id>` (gitignored)
- Packets: `.codex/packets/<packet_id>/`
- Evidence output: `.codex/out/<packet_id>/` (gitignored)
- Rule: All Codex execution occurs inside the packet worktree; repo root remains clean.

## Plant A updates
`.codex/` is managed as a git subtree from `fatb4f/codex-plant-a`.
```bash
git subtree pull --prefix .codex https://github.com/fatb4f/codex-plant-a.git main --squash
```

## v0.2.0 Public API contracts (P0)

Lock these behaviors early to avoid churn and nondeterminism.

### Budget
- API: `Budget(limit, used=0, label=None)` with `remaining` and `consume(amount)`.
- Semantics: define mutable vs immutable; define overflow rule (deny/raise/clamp).
- Invariants: `limit >= 0`, `used >= 0`, plus explicit `used <= limit` policy.

### seeded(...)
- Scope: which RNGs are controlled (Python `random` required; NumPy optional if installed).
- State: whether RNG state is restored on exit (recommended: yes).
- Nesting: deterministic behavior for nested contexts.

### Mermaid helpers
- Inputs: explicit schema for trace steps/spans (required fields + optional fields).
- Determinism: stable node IDs, stable ordering, deterministic label escaping.
- Errors: clear behavior for invalid graphs (missing parent, cycles).

### Optional deps policy
- `import ctrlr` must succeed on minimal install.
- Optional feature calls must raise a helpful error naming the extra to install.
