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
