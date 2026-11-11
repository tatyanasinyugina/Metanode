# Live audit: METANODA Instagram / YouTube visual and publishing results

**Date:** 11 November 2026  
**Scope:** Current Instagram and YouTube connections, recent publishing history, actual visual assets and available performance data.  
**Important:** Read-only audit plus creation of a visual-review prompt in the Instagram creative picker. No post was created or published during this audit.

## 1. Connected accounts

- Instagram via Supermetrics IGI: `metanoda.ai`, account ID `17841470456952988`; publishing and insights scopes are active.
- Instagram via vidIQ: `metanoda.ai`, platform account ID `29113336628328872`; connection active, `canPublish=true`.
- YouTube via vidIQ: `METANODA`, handle `@metanoda`, channel ID `UCgcXPGT0dWvqjbdE3wtNAHQ`; connection active, `canPublish=true`.
- vidIQ authorized account: `ls.sharoian@gmail.com`.
- No claim is made that YouTube publishing is available through Supermetrics; the verified YouTube publishing route is vidIQ.

## 2. Instagram — actual posts and performance snapshot

Recent Instagram media returned by IGI AccountMedia query (30-day inclusive window; data queried live, not cached):

| Media ID | Link | Type | Current snapshot |
|---|---|---|---|
| `18132109735827225` | https://www.instagram.com/p/DfkiUxZDies/ | Feed image | 1 like, 1 comment; reach 0 in returned row |
| `17991938421081819` | https://www.instagram.com/p/Dfkl-JvOoq5/ | Feed image | 0 likes/comments/reach |
| `17992386372118777` | https://www.instagram.com/reel/Dfkm4J9uO5i/ | Reel | Caption claims an imaginary conversation between Tatyana Sinyugina and Elon Musk; this is a representation/endorsement risk and is not to be reused |
| `18138104302642770` | https://www.instagram.com/reel/DfkoS8DhuNe/ | Reel | 67 reach, 68 views, 3 comments; 0 saves/shares at snapshot |
| `18077227664766700` | https://www.instagram.com/p/DflYJ6tDD21/ | Bilingual feed image | 0 likes/comments/reach at snapshot |
| `18094224926280271` | https://www.instagram.com/p/DflZDLwjJzI/ | Feed image | Previously flagged for unsupported authorial attribution; do not reuse without source revalidation |
| `18132658087748911` | https://www.instagram.com/p/DflbCvzDQia/ | 5-slide carousel | 0 likes/comments/reach at snapshot |

Performance values are an early snapshot, not a mature 7-day result. Zero in a returned metric is the platform's returned value at query time; it does not establish long-term failure. The Reel with 67 reach/68 views/3 comments is the only item with a non-zero reach signal in this snapshot.

## 3. Visual inspection — actual assets

### Negative Example 002 — generic corridor Reel cover
- Asset: `18138104302642770`, Reel `DfkoS8DhuNe`.
- Cover: dark architectural corridor with light at the far end.
- Issue: generic "passage/unknown" metaphor; does not show the specific source proposition or a verifiable relation to the spatial methods described in the monograph.
- Metrics snapshot: 67 reach, 68 views, 3 comments; this is an early distribution signal, not proof of visual relevance.
- Decision: do not use as the reference style for the next content cycle.

### Negative Example 003 — carousel with child/cosmos default and text collision
- Asset: `18132658087748911`, carousel `DflbCvzDQia`, 5 slides.
- Slide 1: child + Earth/cosmic network imagery; the subject shifts the brand toward child/cosmos imagery instead of the selected source idea.
- Slide 3: children silhouettes and luminous interface; again defaults to children as the central visual motif.
- Slide 4: generic glowing wireframe/cube and child reaching upward; does not show the concrete floor → wall → volume transition.
- Slide 5: the source-text block is visibly obscured by a large dialogue overlay; text layers collide and the original copy becomes unreadable.
- Decision: reject as a visual reference. Do not edit or delete the already-published post without a separate instruction. The slide-5 overlap is a critical legibility defect.

### Existing Reel caption risk
- Asset `17992386372118777`, Reel `Dfkm4J9uO5i`, caption: “Imaginary conversation of Tatyana Sinyugina and Elon Musk…”.
- This implies a fabricated conversation with a real public figure. It must not be reused or represented as a real exchange/endorsement. Existing post is left untouched.

## 4. YouTube — actual publishing state

- Video: **METANODA — The Unknown Begins When We Change Our Point of Observation**
- URL: https://www.youtube.com/watch?v=TtJEDT-mChs
- Video ID: `TtJEDT-mChs`
- Type: Short, duration 16 seconds.
- vidIQ social publication: `completed`; one destination; no platform failure.
- YouTube video metadata: `privacyStatus=private`; `scheduledPublishAt=2026-11-12T12:00:00Z`; 2 views, 0 likes, 0 comments at snapshot.
- vidIQ status explicitly says a video given a publish time stays private until that time. Therefore the upload is complete, but it is **not public yet**; it is scheduled to become public at the recorded time if YouTube honours the scheduled publication.
- YouTube thumbnail was unavailable while private, so its visual content could not be independently inspected from the thumbnail.
- Do not upload a duplicate. Recheck after the scheduled publication time and verify the public URL/visibility.

## 5. Source-grounded correction for the next visual

Primary source: Tatyana Sinyugina, *Метанода Татьяны Синюгиной*, 2026, in the repository source file `Метанода_Татьяны_Синюгиной_RU_EN 2.md`.

Exact source locations:
- `Обращение к будущему читателю`: the author describes years of observation and asks why a change in spatial organization changes the character of thinking, and why horizontal, then vertical, then volumetric space is associated with changes in perception.
- §2.4, “Нейросеть на полу и нейросеть на стене: рождение развивающей реальности”: the floor system organizes movement; the wall system changes perception; the environment changes with the learner's activity.
- §11.1–11.3: floor architecture, wall architecture, and volumetric developing reality.

The next visual must show the specific progression **horizontal interactive floor → vertical interactive wall → connected volumetric spatial environment**. It must not use a generic corridor, portal, cosmic background, abstract sculpture, or child portrait as a substitute. A schematic image must be labelled in the caption as an illustration, not documentary evidence of an actual installation. Do not depict children by default.

## 6. Current action / blockers

- A source-grounded prompt was submitted to the Instagram creative picker for a 1080×1350 (4:5) schematic of the floor → wall → volume transition, with no people/children, no cosmic motifs, no text, and explicit rejection of generic architectural metaphors.
- The creative picker opened for visual review; its response did not contain a new generated asset or a fresh `upload_ref`. The prompt is staged for review/generation; it is **not** a completed visual.
- No new Instagram or YouTube post was created or published during this audit.
- For AI imagery, the user must review the generated visual before it can be used in a post. For vidIQ social publishing, the user must see and approve the exact draft before publish. YouTube privacy must be explicitly chosen; the existing video is private until its scheduled time.
- Next operational step: complete the picker generation/review, then build one exact draft for Instagram and YouTube from the approved asset; validate platform rules; show the draft and publish only after approval. Do not duplicate existing media.

## 7. Readiness verdict

**A5 visual readiness: FAIL / repair required.** Existing outputs include a generic corridor metaphor, default child/cosmos imagery, and a carousel text collision. The new source-grounded asset has not yet been generated and passed review.

**A6 publishing readiness: PARTIAL.** Instagram and YouTube accounts are connected. Instagram has recent live posts; YouTube upload is completed but still private until its scheduled publish time. There is no verified new cross-platform publication from this audit.

**Agent training status:** instructions and negative examples are documented. This audit does not prove model fine-tuning or autonomous operation. A full end-to-end pass requires a new approved asset, valid platform drafts, and verified publication links.
