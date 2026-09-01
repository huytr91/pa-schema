# Solution Pipeline Packet v1.1

`export_profile: agent_ready` — structured handoff for implementation agents and RPA builders.

## Top-level fields

| Field | Purpose |
|-------|---------|
| `document` | Meta + `schema: pa_solution_pipeline_packet.v1.1` |
| `agent_instructions` | Task, `do_not`, `rpa_app_builds` |
| `requirements` | Summary, constraints, overview prose |
| `business_slots` | Fillable framework: `value`, `source`, `confidence`, `confirm_in_rpa` |
| `open_items` | Fields to confirm in RPA |
| `completeness` | `ready_for_implementation`, `ready_for_unattended_production` |
| `solution_graph` | Nodes + edges (topology) |
| `data_flow` | Edge contracts for parsers |
| `integrations[]` | OAuth specs (`pending_rpa`) — no tokens |
| `selected_sub_pipelines[]` | Per-slot architecture + evidence |
| `architecture_decision_report` | Sanitized ADR |

## Fill model

1. **Deterministic** — graph topology, `match_targets` from edges, pattern templates
2. **Optional LLM enrich** — business slot details (`enrichment_sources` may include `llm`)
3. **Open items** — gaps flagged for RPA (`confirm_in_rpa: true`)

## PA vs RPA

| PA (this packet) | RPA app |
|------------------|---------|
| Solution graph + contracts | Build real flows |
| `integrations[]` design spec | OAuth popups, connectors |
| Benchmark / rank AI slots | User confirms uncertain steps |

## JSON Schema

`schemas/pa_solution_pipeline_packet.v1.1.json`

## Example

[`examples/email-sb123/packet.v1.1.json`](../examples/email-sb123/packet.v1.1.json) —
email ingress → attachment extract → OCR branch → keyword `SB123` → notify.
