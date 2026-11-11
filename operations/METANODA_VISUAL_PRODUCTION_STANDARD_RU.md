# METANODA — Visual Production Standard v1.0
**Date:** 11 November 2026  
**Owner role:** A5 Visual & Multimedia  
**Consumer role:** A6 Media Channel Editor  
**Status:** operating standard added; end-to-end visual quality test pending.

## 1. Problem statement

The previous visual process was too generic and fragile:
- A5 had only a broad role description, without an executable art-direction or quality-control pipeline.
- A6 required visual assets from A5 but did not define how to reject generic, repetitive or semantically weak visuals.
- Existing saved uploads included duplicates and at least one upload_ref that Instagram rejected as missing/0 bytes.
- The recent content flow reused a single luminous geometric threshold image, which risks turning the METANODA visual identity into one repeated AI-generated motif.
- Technical upload validation was treated too much like proof that the visual was ready. It is not.

This standard adds a repeatable production and quality gate. It does not assert that an autonomous A5 service is deployed.

## 2. Visual purpose

A visual must perform at least one clear job:
1. **Stop:** create a distinctive first-frame / cover that is legible on a phone.
2. **Explain:** make one source-grounded idea easier to understand.
3. **Demonstrate:** show an observable process, spatial relation or transformation.
4. **Orient:** establish a recognizable METANODA editorial identity without replacing the content with branding.
5. **Invite:** make the next action or question obvious.

A beautiful image that does none of these is decoration, not a finished content asset.

## 3. Source and meaning custody

For each visual, A5 receives:
- task object and audience;
- exact author source and locator;
- source proposition and allowed claims;
- text/caption and hook;
- format, platform, language and CTA;
- rights, consent and privacy restrictions.

Separate four visual categories:
- **Author source material:** original diagrams, photos, drawings or images supplied by the author; do not alter meaning.
- **Documentary material:** actual observed processes or environments; preserve time/context and consent.
- **Explanatory graphic:** diagrams, typography, sequences and charts built from verified source information.
- **Conceptual visual metaphor:** AI-generated or artist-created interpretation; label internally as a metaphor, never as a factual illustration of the author's system.

Do not depict a concept as a literal structure of METANODA unless the source or author explicitly supports that representation. Never use a generic neural-network node diagram, glowing portal, galaxy/star field or abstract gold geometry as a default substitute for the actual idea.

## 4. Art direction — coherent identity, varied visual language

Keep a restrained editorial identity as a family resemblance, not a template that makes every post look the same:
- Core palette may include midnight navy, warm ivory, stone, graphite and restrained champagne-gold.
- Typography: high legibility, disciplined hierarchy, generous negative space; avoid tiny text and decorative type.
- Composition: one focal point, clear scale, visible contrast, purposeful negative space, phone-first readability.
- Texture/materials may vary: architectural photography, paper, physical objects, spatial installations, translucent materials, clean diagrams, documentary frames, kinetic typography.
- Do not force every asset into a portal, glowing passage, sphere, gold line or floating-node aesthetic.
- Use the author's actual diagrams/media only with provenance and permission.
- Visual identity is not a claim about the author's method; style choices are editorial design.

## 5. Format selection — choose by the content, not by habit

### Instagram feed image / cover
- Preferred working canvas: 1080 × 1350 (4:5).
- One dominant focal point, safe margins, readable title if text is necessary.
- No long paragraphs embedded in the image. Caption carries explanation.

### Carousel
- 4–6 slides, consistent 4:5 canvas.
- Slide 1: concrete question/problem and visual hook.
- Slides 2–4: one idea per slide, clear progression; use diagrams only when relations are grounded.
- Final slide: concise synthesis + one CTA.
- Keep typography, spacing and grid consistent; do not use a quote style for an editorial adaptation.
- Check all slides together as one sequence, not as isolated exports.

### Reel / short explainer
- Working canvas: 1080 × 1920 (9:16).
- First frame must communicate the tension or question immediately.
- Visual change or meaningful movement every 1–3 seconds; avoid meaningless zooms and random transitions.
- Use motion to explain a relationship or transformation, not as decoration.
- Subtitles must be accurate, high contrast and safely inside platform UI margins.
- Produce a strong static cover separately; don't rely on an arbitrary video frame.

### Stories
- 1080 × 1920; one action or question per frame.
- Use for interaction, follow-up and traffic to a feed post; don't stretch one feed design into unreadable story format.

## 6. Creative route — mandatory sequence

1. **Brief:** A5 writes a one-sentence visual task: “Show/explain/demonstrate X for audience Y so they understand/do Z.”
2. **Meaning map:** identify what must be shown, what may be metaphorical, and what must not be implied.
3. **Three distinct concepts:** produce three genuinely different compositions or visual mechanisms, not three color variations of one prompt:
   - documentary/process-led;
   - explanatory/editorial graphic;
   - conceptual/art-directed metaphor.
   Select only the routes that fit the source and available rights.
4. **Rough preview:** generate or assemble the concepts before final production. For AI images on Instagram, use Supermetrics Creative Picker and let the user review the visual before any publish action unless the user explicitly waives review.
5. **Phone test:** preview at small mobile size; inspect focal point, contrast, crop, legibility and whether the idea is understood within 1–2 seconds.
6. **Source-fidelity test:** compare every visual claim and symbol against the source-to-post card. Remove any misleading implication.
7. **Production:** export correct dimensions, quality, format, subtitle/alt-text and a stable version label.
8. **Upload integrity:** use a fresh, confirmed upload_ref. Check that the reference resolves to a real non-zero asset and correct content type. Never assume an old upload_ref remains valid just because it appears in a saved asset list.
9. **Final preview:** review the exact asset selected for the post, not merely the prompt or a prior draft.
10. **Handoff:** deliver final asset/ref, preview, dimensions, source locator, rights, design rationale, alt-text, limitations and pass/fail gates to A6.

## 7. Quality scorecard — minimum release standard

Score each dimension 0–2:
- **Meaning fidelity:** 0 distorted / 1 ambiguous / 2 source-faithful.
- **Distinctiveness:** 0 generic stock/AI cliché / 1 somewhat distinctive / 2 recognizable original art direction.
- **Instant comprehension:** 0 unclear / 1 needs caption / 2 core visual idea reads in 1–2 seconds.
- **Composition:** 0 cluttered / 1 acceptable / 2 clear hierarchy and focal point.
- **Mobile legibility:** 0 fails / 1 marginal / 2 clear at phone size.
- **Format fit:** 0 wrong crop/ratio / 1 workable / 2 native to intended placement.
- **Craft/consistency:** 0 visibly rough / 1 adequate / 2 polished and consistent.
- **Rights/provenance:** 0 unknown / 1 incomplete / 2 confirmed.

Minimum: 13/16, with no zero in meaning fidelity, mobile legibility, format fit or rights/provenance. A5 records the score and evidence; it must not inflate scores to pass.

## 8. Variation and anti-repetition control

Maintain a rolling visual register of the last 12 assets:
- subject/concept;
- visual mechanism;
- composition;
- palette;
- format;
- source type;
- prompt / production method;
- asset ref and final URL;
- score and reviewer notes.

Do not use the same central metaphor or near-identical composition in consecutive feed posts. Across a 6-post run, use at least three visual mechanisms and two format families. A brand palette may recur; the same image grammar should not dominate.

## 9. Failure handling

- Missing/0-byte upload_ref: reject it, generate a fresh upload, verify again. Do not ask the user to manually upload unless the picker explicitly requires user input.
- Creative Picker has opened but no generated/uploaded asset is returned: status is “preview pending”, not “asset created”.
- Prompt is strong but output is generic: revise art direction and generate again; don't publish the prompt.
- Visual is beautiful but not source-grounded: reject.
- Visual is accurate but unreadable at phone size: redesign.
- Rights or provenance uncertain: block.
- User review is required by the connected publishing workflow: wait for the review; do not bypass it.

## 10. Handoff contract

A5 → A6 package:
- visual_task_id;
- source file + exact locator;
- one-sentence visual objective;
- concept selected and two rejected concepts with reasons;
- source facts represented vs metaphorical additions;
- final asset preview + upload_ref;
- dimensions, aspect ratio, file type and byte-size/validity result;
- alt text;
- rights/consent/provenance;
- quality scorecard;
- revision history;
- explicit status: draft / preview pending / reviewed / upload verified / approved for publication.

## 11. First repair test — monograph opening “Что есть развитие?”

Source-grounded proposition in the current draft:
“Развитие — это способ существования человека. Развитие — это способ существования Космоса.”

The visual must not pretend to show a literal cosmic structure or a proven mechanism. It may explore three editorial routes:
1. A human-scale point embedded in an evolving architectural/spatial environment.
2. A typographic/explanatory composition showing the contrast between “development as a finite destination” and “development as a mode of being”, explicitly labelled as an editorial interpretation.
3. A documentary or physical-material sequence showing continuous transformation, only if the material is original and rights-cleared.

The currently open Creative Picker contains three proposed prompt directions for high-quality 4:5 images. Status is **preview pending** until a concrete image and upload_ref are returned and reviewed. Do not publish automatically.

## 12. Success criteria

Visual production is repaired only after:
- A5 instruction is updated and linked from A6;
- at least one real asset is generated/uploaded and visually reviewed;
- its upload_ref passes technical validation with non-zero media;
- the visual scorecard passes;
- A6 receives a complete handoff;
- no post is published without the separate user authorization/release condition.

A written standard alone is not proof of improved visual quality or deployed agent capability.
