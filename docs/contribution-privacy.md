# Contribution privacy — pipeline evidence only

> **Rule:** User contributions serve **pipeline benchmark evidence** only.  
> **AI agents (interview, architecture, web chat) must NOT ingest contribution data.**

## What users may contribute (allowlist)

| Category | Fields | Purpose |
|----------|--------|---------|
| **Hardware** | `cpu_class`, `cores`, `ram_bucket`, `gpu_class`, coarse `os_family` | Match observations to machine class |
| **Problem (public)** | `domain`, `language`, `document_type`, `quality_target`, `throughput_target`, `budget` | Group benchmarks by workload — **no `notes`** |
| **Pipeline (public)** | `pipeline_id`, `version`, `checksum`, `component_names[]` | Identify topology — **no step config secrets** |
| **Metrics** | latency p50/p95, RAM, quality, success_rate, run_count, variance | Leaderboard / evidence aggregation |

## What is NEVER contributed

| Forbidden | Reason |
|-----------|--------|
| `problem.notes` / business intent / chat transcripts | Not pipeline evidence; may contain PII |
| Sample documents (PDF, images, email bodies) | User content |
| `runs.output_text` / OCR raw output | Derived user content |
| File paths (`sample_file`, home directory) | Fingerprinting / PII |
| API keys, OAuth tokens, email addresses | Secrets |
| Session IDs, web agent exports, Solution Pipeline Packet | Product handoff — separate from benchmark flywheel |
| Hostname, username, MAC, serial numbers | Device PII |

## Who may consume contributions

| Consumer | Allowed |
|----------|---------|
| Benchmark leaderboard (aggregate) | ✅ |
| Evidence aggregation / outlier detection | ✅ |
| **Interview agent** | ❌ |
| **Architecture agent** | ❌ |
| **Web chat / LLM context** | ❌ |
| LLM training / fine-tuning | ❌ |
| Marketing / user profiling | ❌ |

The ranking engine may use **verified observation statistics** internally. It must not pass contribution payloads into LLM prompts for interview or architecture generation.

## Opt-in

- Default: **local only** (`benchmarks.duckdb` on user machine).
- Upload only after explicit CLI confirmation + ODC-BY terms.
- No silent background upload.

## Schema

`schemas/pa_observation_contribution.v1.json` — bundle format for export/upload.

## Harness command

```bash
python cli.py contribute export \
  --db benchmarks.duckdb \
  --experiment-id <id> \
  --problem problem.yaml \
  --pipelines pipelines/a.yaml \
  --out contribution.json \
  --i-agree-to-terms
```

Without `--i-agree-to-terms`, export is blocked.
