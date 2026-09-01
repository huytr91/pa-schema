# pa-schema

**The contract** for Pipeline Architect — JSON Schemas and handoff examples for
benchmark observations and Solution Pipeline Packets.

Part of the [Pipeline Architect](https://github.com/huytr91/pipeline-architect) open-core (MIT).

## Schemas

| File | Purpose |
|------|---------|
| `schemas/pa_solution_pipeline_packet.v1.1.json` | Export handoff: solution graph + business slots + AI sub-pipelines |
| `schemas/pa_observation_contribution.v1.json` | Opt-in community benchmark bundle (metrics only) |
| `docs/observation.md` | Observation / DuckDB fields (Problem × Pipeline × Hardware) |
| `docs/solution-pipeline-packet.md` | Packet v1.1 field guide |
| `docs/contribution-privacy.md` | **Pipeline evidence only** — AI agents must not ingest contributions |

## Examples

- [`examples/email-sb123/`](examples/email-sb123/) — Email trigger, keyword `SB123`, OCR slot (agent-ready packet)

Validate the example against the schema:

```bash
pip install jsonschema
python scripts/validate_examples.py
```

## Principles

- **JSON is source of truth** — Markdown is a human-readable projection.
- **Evidence at the leaf** — benchmark AI slots; design-only nodes (email, rules) stay spec-level.
- **PA vs RPA** — OAuth, PII, and connector setup live in the RPA/workflow app, not in this packet.

## Related repos

- [pa-harness](https://github.com/huytr91/pa-harness) — run local benchmarks, write observations
- [pa-adapters](https://github.com/huytr91/pa-adapters) — component wrappers (OCR, parsers, …)

## License

MIT — see [LICENSE](LICENSE).
