# Codex execution conventions

- Worktrees: `.codex/.worktrees/<packet_id>` (gitignored)
- Packets: `.codex/packets/<packet_id>/`
- Evidence output: `.codex/out/<packet_id>/` (gitignored)
- Rule: All Codex execution occurs inside the packet worktree; repo root remains clean.
