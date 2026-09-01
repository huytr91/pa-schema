# Observation schema (V0)

An **observation** records the outcome of running a **pipeline** on a user's machine
for a given **problem fingerprint** and **hardware fingerprint**.

Pipeline Architect stores observations locally (DuckDB in `pa-harness`) using fields
aligned with this spec so data can migrate to a central DB later without breaking changes.

## Identity

| Field | Description |
|-------|-------------|
| `experiment_id` | Batch run identifier |
| `pipeline_id` | Pipeline under test |
| `pipeline_version` | Config version |
| `problem_fingerprint_id` | Stable hash of problem constraints |

## Hardware fingerprint (auto-detected only)

| Field | Description |
|-------|-------------|
| `cpu_class` | CPU tier label |
| `cores` | Logical cores |
| `ram_bucket` | RAM bucket (`8-16GB`, …) |
| `gpu_class` | `none` \| `entry` \| `mid` \| `high` \| `datacenter` |

Users must **not** hand-enter hardware specs for official contributions.

## Benchmark results

| Field | Description |
|-------|-------------|
| `latency_p50_ms` / `latency_p95_ms` | From N≥3 runs per sample |
| `peak_ram_mb` | Peak RSS during run |
| `quality_estimate` | Relative score (Bradley-Terry when multiple candidates) |
| `quality_confidence` | Confidence in quality signal |
| `success_rate` | Fraction of successful runs |

## Anti-fraud metadata (required)

| Field | Description |
|-------|-------------|
| `harness_version` | Protocol version |
| `run_count` | Must be ≥ 3 for official observations |
| `checksum` | Hash of pipeline config — no hand-edited metrics |
| `source_type` | `internal` for user harness runs |

## Problem fingerprint (input)

```yaml
problem_fingerprint:
  domain: document-ocr
  language: vi
  document_type: table-heavy
  quality_target: 0.96
  throughput_target: batch-offline
  budget_constraint_usd_per_unit: null
  notes: Optional business context
```

See `pa-harness/problem.example.yaml` for a runnable sample.

## Contribution

Observations must come from `pa-harness` runs — not manually submitted JSON.
See [pa-harness CONTRIBUTING](https://github.com/huytr91/pa-harness/blob/main/CONTRIBUTING.md).
