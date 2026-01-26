Objective:
- Add optional OpenTelemetry bridge (no hard dependency).
  - otel_available(): bool
  - otel_bind(lens): binds lens fields into baggage/span attrs when OTel installed

Contract:
- .codex/packets/packet-ctrlr-05-otel/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-05-otel
- Keep OTel behind an extra in pyproject (do not force-install in base).
- Run: uv sync --frozen; uv run pytest -q
- Evidence: out/packet-ctrlr-05-otel/

Tasks:
1) Create src/ctrlr/otel.py:
   - defensive imports; no-op when missing
2) Add optional dependency group to pyproject.toml (extras)
3) Tests:
   - otel_available() == False in base env (unless already installed)
   - otel_bind() does not raise when OTel absent

Evidence bundle (out/packet-ctrlr-05-otel/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
