# Email + keyword SB123 + OCR slot

Example **Solution Pipeline Packet** (v1.1 `agent_ready`) for:

> When email arrives, scan attachments for keyword `SB123` in filename and body;
> OCR scanned images/PDFs first, then match.

## Files

| File | Description |
|------|-------------|
| `packet.v1.1.json` | Source of truth — validate against `schemas/pa_solution_pipeline_packet.v1.1.json` |
| `problem.yaml` | Problem fingerprint input (for harness benchmark of OCR slot) |

## Graph (summary)

```
email_ingress → attachment_extract → ocr_branch (AI slot)
                  └────────────────→ keyword_match → route_action → notify
ocr_branch ────────────────────────→ keyword_match
```

## Open items (expected)

- Notification channel (email reply / Teams / ticket) — confirm in RPA
- OCR policy per attachment type — confirm in RPA

`completeness.ready_for_implementation` may be `true` while
`ready_for_unattended_production` is `false` until open items are resolved.
