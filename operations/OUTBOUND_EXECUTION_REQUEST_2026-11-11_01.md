# METANODA outbound execution request — 2026-11-11

Status: QUEUED_FOR_GITHUB_ACTIONS_VALIDATION
Request ID: METANODA-OUTBOUND-2026-11-11-01
Source branch: agents/social-media-execution

## Objective
Move the METANODA content workflow from repository source to an external execution adapter, with provider receipts returned to this repository.

## Required sequence
1. Read the author source and A6 handoff from this branch.
2. Validate source attribution, editorial translation labels, privacy, rights, and visual review status.
3. Prepare an outbound payload for the connected Instagram account @metanoda.ai.
4. Send the payload only through an explicitly configured and authorized publishing adapter.
5. Verify the provider response and record its post ID/permalink.
6. Return a receipt to operations/ without storing credentials or private personal data.

## Current content candidate
- Draft: operations/A6_POST_DRAFT_001_DEVELOPMENT_RU_EN.md
- Visual asset: generated externally in Runway; available for manual review through the previously returned signed asset URL.
- Publication authorization: NOT GRANTED. Do not publish until the visual is reviewed and explicitly approved.
- Do not regenerate, duplicate, schedule, or publish this candidate automatically.

## Adapter requirements
- No credentials in repository files, commit messages, logs, or chat.
- External publishing adapter must use protected runtime secrets or an already authorized secure integration.
- If credentials/adapter are absent, emit an explicit machine-readable BLOCKED status and preserve the queue item.
- Never mark this request COMPLETE without an external provider receipt and a verified return record in GitHub.

## Expected runner output
- source_validation
- outbound_adapter_status
- provider_receipt_status
- return_record_status
