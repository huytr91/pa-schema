# Email + keyword SB123 + OCR slot

**Reference workflow** for Solution Pipeline Packet v1.1 — not the only supported domain.

> Pipeline Architect supports **multiple AI domains** (`document-ocr`, `audio-transcription`, `image-classification`, …). This example uses **email orchestration + one OCR slot** because it is the V0 vertical slice. The same packet schema applies when slots use other domains.

## Scenario

> When email arrives, scan attachments for keyword `SB123` in filename and body;
> OCR scanned images/PDFs first, then match.

## Files

| File | Description |
|------|-------------|
| `packet.v1.1.json` | Source of truth — validate against `schemas/pa_solution_pipeline_packet.v1.1.json` |
| `problem.yaml` | Problem fingerprint for the **OCR slot** benchmark (domain: `document-ocr`) |

## Graph (summary)

```
email_ingress → attachment_extract → ocr_branch (AI slot: document-ocr)
                  └────────────────→ keyword_match → route_action → notify
ocr_branch ────────────────────────→ keyword_match
```

## Other domains

- Harness: `problem.audio.example.yaml`, `problem.image.example.yaml` in [pa-harness](https://github.com/huytr91/pa-harness)
- Model: [multi-domain.md](../../docs/multi-domain.md)

## Open items (expected)

- Notification channel — confirm in RPA
- OCR policy per attachment type — confirm in RPA

`completeness.ready_for_implementation` may be `true` while `ready_for_unattended_production` is `false`.
