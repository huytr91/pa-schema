# Multi-domain pipelines

Pipeline Architect is **not an OCR tool**. It recommends and measures **end-to-end solution pipelines** where each **AI slot** can target a different domain.

## Model

```
Solution Pipeline (one user problem)
├── design-only nodes     email, rules, storage, notify — spec only, not benchmarked like AI
└── ai_pipeline_slot(s)   each slot has its own domain + TOP N sub-pipelines + evidence
        ├── document-ocr
        ├── audio-transcription
        ├── image-classification
        ├── rag-retrieval
        └── … (extensible via Problem Fingerprint + catalog)
```

- **Evidence at the leaf** — benchmarks apply to **AI slots**, not every integration node.
- **One solution graph** can mix orchestration (email, workflow) with **one or more** AI domains in V1+.

## Problem Fingerprint `domain`

The harness and ranking use `problem_fingerprint.domain` to select candidates and feasibility rules. Examples in the open repos:

| Domain | Example problem file (pa-harness) | Mock adapter components |
|--------|-----------------------------------|-------------------------|
| `document-ocr` | `problem.example.yaml` | `pdf-native-parser`, `ocr-engine`, … |
| `audio-transcription` | `problem.audio.example.yaml` | `audio-loader`, `whisper-asr`, … |
| `image-classification` | `problem.image.example.yaml` | `image-loader`, `resnet-classifier`, … |

## Why so many OCR examples?

V0 uses **document OCR (Vietnamese)** as the **first reference vertical** — end-to-end case study (email → attachment → OCR slot → export).  
The schema, harness protocol, and adapters are **domain-agnostic**; OCR is documentation convenience, not a product boundary.

## pa-adapters

Community PRs can add **any** component (`ocr-engine`, `whisper-asr`, embedders, parsers).  
See [pa-adapters](https://github.com/huytr91/pa-adapters) — not an “OCR adapters only” repo.
