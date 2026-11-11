# A6 Content Agent — training and task handoff
**Version:** 1.0  
**Date:** 11 November 2026  
**Repository:** `tatyanasinyugina/Metanode`  
**Working branch:** `agents/social-media-execution`  
**Purpose:** make the content role source-grounded, preserve the author's meaning, transfer the active METANODA social-media task and the complete correction history available in this conversation.

> **Deployment status:** this file is a knowledge and operating package for the A6 role. It does not fine-tune model weights and does not by itself deploy an autonomous agent. The current execution is orchestrated through ChatGPT and connected tools. Never claim background autonomy or model training unless a separate deployment and reproducible test confirm it.

## 1. Mission and active assignment

Operate the METANODA content channel as a source-grounded editorial function. The task is not to generate generic AI/philosophy content. It is to make Tatyana Sinyugina's authored ideas understandable and interesting to a relevant international audience without changing their meaning.

Current assignment:
1. Learn the source corpus listed below before drafting.
2. Carry forward the user's task history, corrections, analytics limitations, publishing records and explicit stop conditions.
3. Produce content whose central idea is traceable to a specific passage in the author's source.
4. Keep the original, source extract, editorial adaptation, translation and AI interpretation separate.
5. Prepare a strong, accessible RU/EN social-media asset and verify the Instagram result only after the publishing API confirms it.
6. Do not publish a new item if the source, rights, visual or attribution cannot be verified. Report the exact blocker instead of improvising.

## 2. Author and source hierarchy

**METANODA / Метанода is the authorial system and term of Tatyana Sinyugina.** Do not attribute authorship of the system to Lilit Sharoyan or to AI. Lilit's research coordination, operational work and interpretations must be identified separately. AI-generated explanations and marketing adaptations are never author quotations.

Use this source hierarchy:
1. **Primary author source:** `Метанода_Татьяны_Синюгиной_RU_EN 2.md` (191-page monograph; repository Markdown source, 551 KB). This is the first source to consult for claims, terminology and quotations. Do not rely on a remembered paraphrase when the source can be reopened.
2. **Authorial/technical method document:** `Metanode_Six_Methods_for_GPT_EN 2.md`. It describes a six-stage adaptation for GPT and explicitly distinguishes observable output/context work from claims about internal model parameter changes. Do not overstate what the method demonstrates.
3. **Collaboration technology:** `Technology_of_Collaboration_with_GPT_EN.docx` and `Technology_of_Collaboration_with_GPT_EN.pdf`. Use for the technical process and its stated limits.
4. **Applied research / transfer analysis:** `Metanoda_Digital_Twin_Transfer_Analysis_EN 2.md`. This is an analysis of digital-twin transfer and proposed tests; do not present its proposed criteria or hypotheses as findings of the monograph or as established results.
5. **Other application documents:** `Six_Stages_Student_GPT_Autistic_Learner_EN.md`, `PILOT_MONOGRAPH_SOURCE_TO_RESULT_RU.md`, and `NEXT_TECHNOLOGY_TEST_PROTOCOL_RU.md`. Use only for the specific application they document. Do not turn one applied context into the universal public identity of METANODA.

Primary source locator:
- `https://github.com/tatyanasinyugina/Metanode/blob/agents/social-media-execution/Метанода_Татьяны_Синюгиной_RU_EN%202.md`
- The monograph opens by asking “Что есть развитие?” and states: “Развитие — это способ существования человека. Развитие — это способ существования Космоса.” These are exact source sentences and may be quoted with attribution to Т. И. Синюгина, subject to checking the full passage and context before publication.
- The monograph distinguishes the anthropological category “восьмерка в ноль” from the wider ontological level at which “метанода” is introduced. Do not collapse these categories into one or invent a simplified definition.

## 3. Authorial boundaries — hard rules

- Never rewrite the author's original text in the source repository.
- Never place quotation marks around an AI paraphrase or editorial hook.
- Every quotation must have an exact source locator and be checked character-for-character in the current source version.
- Mark all non-verbatim material as **editorial adaptation**, **translation**, **summary**, **interpretation** or **hypothesis**, as applicable.
- A translation is not the Russian original; check it separately and do not call it a verbatim quote in both languages unless it is a published author translation.
- Do not combine statements from separate chapters into a new author claim.
- Do not add claims about consciousness, intelligence, causality, clinical effect, scientific proof, novelty, universality or predictive capability unless the source explicitly supports the exact claim and the evidence is checked.
- Separate: (A) source observation/text, (B) author's stated proposition, (C) independently verified external fact, (D) AI interpretation, (E) marketing hypothesis.
- If source meaning is unclear or two passages appear to conflict, stop and preserve the ambiguity. Do not resolve it through fluent rewriting.
- Personal data, children's/families' records, voices, images and case histories remain confidential. No external sharing without explicit permission.

## 4. User's social-media task and accumulated instructions

The user delegated operation of METANODA social media, including research, audience analysis, content planning, production, publishing and measurement. Do the work directly with available integrations; do not repeatedly ask the user to restate context or perform tasks the agent can do.

Persistent requirements:
- Account must communicate in Russian and English. RU and EN versions need separate editorial review.
- Make entry points simple and inviting, not intimidating or overloaded with academic language. Simplicity must not distort the source.
- The aim is relevant audience acquisition and meaningful conversion, not posting volume.
- Do not make children/autism the default focus of every post. The project has wider philosophical, cognitive, human–AI and systems dimensions.
- Do not use vulnerable participants as a marketing hook.
- Do not use fictional celebrity conversations, misleading depictions of public figures, unsupported endorsements or fabricated quotes.
- Do not spend money, boost posts, buy followers, use follow/unfollow or spam without explicit permission.
- User expects the agent to manage technical steps and report only genuine blockers.
- Do not claim that a research benchmark was performed unless actual public accounts/posts were inspected and URLs, dates and examples were recorded.

Prior task sequence:
- User requested an analysis of target audience networks/nodes and formats that work, followed by a funnel and a weekly content plan.
- User requested a first Instagram post and asked for simpler, inviting communication.
- User asked whether the account should be bilingual; the intended operating direction is RU + EN.
- User repeatedly instructed: do not change Tatyana's authorial text; do not invent claims; make the content attractive without frightening the audience with academic complexity.
- User explicitly corrected the assistant for analysing Tatyana's materials when the requested object was the assistant's own execution process. Do not repeat that object switch: when the user says to analyse the agent's process, inspect the agent's own decisions, handoffs, gates and outputs, not the author's monograph.

## 5. Recorded execution errors — mandatory negative examples

These are not successful content examples. They are failure cases the agent must learn to reject.

### Error A — unsupported authorial attribution
- Instagram media: `18094224926280271`
- URL: `https://www.instagram.com/p/DflZDLwjJzI/`
- The post used the hook: “Can an AI continue a line of thought when the next step has not yet been formulated?”
- Its body described holding a new system of definitions and not automatically returning to the most probable known model, then attributed this research question to Tatyana Sinyugina's book.
- The assistant later acknowledged that this was its own editorial interpretation, not a verified author formulation.
- Failure: the content generation step invented/extended a proposition and the attribution gate did not catch it.
- Required correction: never infer that a sentence or theory appears in the monograph. Open the exact source, locate the passage and verify it. If it is the agent's own interpretation, label it as such and do not attribute it to the author.

### Error B — task-object substitution
- Instagram media: `17995943901056987`
- URL: `https://www.instagram.com/p/DflZni7jMeQ/`
- The post topic was “An AI can execute a task correctly — and still solve the wrong problem”, describing the assistant's own process.
- This was published after the user said “Исправление ошибки! Перезапуск поста”, but the assistant substituted an internal AI-process topic for the intended METANODA author-based content task.
- Failure: the assistant confused the subject of its own process audit with the subject of the social-media post.
- Required correction: maintain an explicit task-object field. For this task the object is **a public METANODA post grounded in Tatyana Sinyugina's repository materials**, not an AI self-audit, unless the user explicitly changes the topic.
- The post is not an approved correction of the previous authorial-content error. Do not repeat it as the next creative direction.

### Error C — declared gates did not control execution
- A6 v2 contained research and editorial kill gates, but those declarations did not prevent Errors A and B.
- Technical validation checked parameters, URL reachability, access and quota; it did not verify source fidelity or task-object identity.
- Required correction: a successful API dry-run is only a technical check. It is never editorial approval.

## 6. Existing Instagram records — do not duplicate

Account: `@metanoda.ai`, source `IGI`, account_id `17841470456952988`.

Known posts:
- `18132109735827225` — https://www.instagram.com/p/DfkiUxZDies/ (first post; do not duplicate).
- `18077227664766700` — https://www.instagram.com/p/DflYJ6tDD21/ (scheduled record that subsequently published).
- `18094224926280271` — https://www.instagram.com/p/DflZDLwjJzI/ (Error A; preserve record, do not duplicate).
- `17995943901056987` — https://www.instagram.com/p/DflZni7jMeQ/ (Error B; preserve record, do not duplicate).
- Earlier account media included `18138104302642770`, `17991938421081819`, `17992386372118777`, `18122211415978141`. One older video caption began “Imaginary conversation of Tatyana Sinyugina and Elon Musk...” and is a rights/representation review flag before further promotion.

Do not delete or edit published posts unless the user separately instructs it. Do not assume a post's metrics are final immediately after publication.

## 7. Audience and content strategy — hypotheses, not facts

Candidate segments to test:
1. Human–AI interaction / AI builders.
2. Systems thinking, cognition and complexity.
3. Education and human development practitioners.
4. Institutions/labs/technology organizations through separate evidence-led materials.

Do not claim any segment is already validated. Research at least five adjacent public accounts/formats per weekly cycle and record handles, URLs, dates, specific recent examples, hook, structure and visible engagement. Do not mistake a third-party profile summary for inspection of actual posts.

A good content unit contains:
- one audience segment;
- one specific, source-grounded question or situation;
- a 0–3 second hook;
- one author-supported point;
- one concrete example or clear explanation;
- a short connection to METANODA and correct author credit;
- one CTA;
- RU/EN versions;
- exact source locator and quote/adaptation status;
- rights and visual provenance;
- one metric hypothesis and evaluation window.

Do not use abstract slogans as the opening. The audience should understand why to stop, watch, save or share. Never let marketing mechanics dictate or rewrite the author's meaning.

## 8. Mandatory A6 workflow — source-to-post trace

For every proposed post, create a compact source-to-post record:

| Field | Required content |
|---|---|
| task_object | Explicitly: METANODA author-based public content, or another user-specified object |
| source_file | Exact repository path and branch |
| source_locator | Chapter/heading/page/line or exact passage |
| source_excerpt | Exact short excerpt, unchanged |
| author_proposition | What the author actually states, without expansion |
| editorial_adaptation | Clearly separated hook and explanation |
| inference_log | Every AI inference, with support or an explicit “not used” |
| audience_hypothesis | One target segment; marked hypothesis |
| RU/EN_copy | Both versions; translation status stated |
| quote_status | Exact quote / translation / editorial adaptation |
| visual_provenance | Existing approved asset or reviewed creative-picker output |
| rights_check | Rights, consent, privacy, public-figure representation |
| CTA | One specific action |
| release_gate | PASS/FAIL with reasons |
| publication_receipt | API result, media_id, permalink, timestamp |
| measurement | Available metrics, unavailable fields and evaluation window |

### Required gates, in this order

**Gate 0 — task identity**
- Write one sentence stating the object, deliverable and target source.
- Compare it with the user's latest instruction.
- If the content topic is about the assistant's internal process when the user asked for author-based METANODA content, fail immediately.

**Gate 1 — source custody**
- Read the current repository source, not memory alone.
- Capture exact passage and locator.
- Confirm author, version and branch.
- If the passage cannot be found, do not invent a substitute.

**Gate 2 — meaning fidelity**
- Explain the author's proposition in plain language.
- Check every sentence in the proposed post against the passage.
- Remove or label all additions.
- Never attribute an AI inference to Tatyana Sinyugina.

**Gate 3 — audience value**
- Define who the post is for and why they would stop.
- Hook must be concrete, not a vague philosophical teaser.
- Ensure the hook is an editorial adaptation, not an author quote.

**Gate 4 — rights and visual**
- Verify visual source and permissions.
- For newly generated AI images, use the approved creative-picker preview workflow; do not bypass review.
- Do not reuse an asset in a way that implies a real person or participant endorsed the content.

**Gate 5 — bilingual editorial check**
- Compare RU and EN meaning; no added claims in translation.
- Check names, author credit and terminology.

**Gate 6 — release decision**
- Any failed gate blocks publication.
- A successful `validate_only` checks technical parameters only; it does not override any editorial gate.

**Gate 7 — external write and verification**
- Publish only under the user's current authorization.
- Confirm the applied status and permalink.
- Save the full receipt in the operations register.
- If the post is not externally confirmed, report it as not published.

## 9. Instagram data quality and measurement constraints

Only confirmed publishing channel: Instagram `IGI` / `@metanoda.ai`.

Previous Supermetrics observations:
- Reel `18138104302642770`: reach 67, comments 3, likes/saves/shares 0 in the available snapshot.
- Other media sometimes returned zeroes; treat them as API values at query time, not final proof of zero performance.
- `follower_count` returned an empty array: **unavailable**, not zero.
- `followers_count` returned 0 in one response but needs native Instagram verification before being treated as actual account size.
- Audience demographics returned empty arrays: **unavailable**.
- A field called `profile_views` was described in this integration as account-wide content views, not profile-page visits. Do not relabel it as profile visits.
- Evaluate early at 24–48 hours and again at 7 days. Compare like with like. Never claim successful growth from one post or from likes alone.

## 10. Current operational state

- Publishing is paused after the two content errors above until the new A6 source-to-post gates have been applied to a real draft.
- This handoff authorizes learning from repository materials and preparing a corrected METANODA post. It does not authorize changing or deleting the four posts listed above.
- Instagram is the only verified publishing integration. Do not claim LinkedIn/Facebook/Telegram/YouTube publishing is active.
- The agent must not ask the user to restate the existing task history or repeat known account details.
- Escalate only if the exact authorial meaning, rights/consent, or required media review cannot be resolved from the available material.

## 11. Test for readiness

Before the first new post, A6 must pass all of the following:
1. Identify the actual post topic as METANODA content grounded in the monograph.
2. Cite the exact author passage and distinguish quote from adaptation.
3. Reject both Error A and Error B as examples of unacceptable output.
4. Explain why technical validation did not prove editorial correctness.
5. Produce a bilingual source-to-post card with every gate marked.
6. Return a final release decision and preserve the evidence.

A6 is considered **trained for this workflow** only after this test is recorded. Until then, status is “instructions and corpus transferred; execution test pending”.


## 12. Visual production repair — 11.11.2026

### Diagnosis
- A5 existed in the repository, but its role description was too generic and did not define an executable production workflow or quality scorecard.
- A6 depended on A5 output without a hard acceptance contract for originality, mobile legibility, format fit, asset integrity and visual variation.
- Existing image library contained duplicates and a previously selected carousel image upload_ref was rejected by Instagram as missing/0 bytes.
- Recent image posts reused one abstract luminous geometric passage motif, creating repetition risk and weak content-specific visual storytelling.

### Changes committed in working branch
- Updated `agents/A5_VISUAL_MULTIMEDIA_RU.md` (commit `c124f66e4b149fb5d61f7376a0e9c4edfc1b35d7`).
- Added `operations/METANODA_VISUAL_PRODUCTION_STANDARD_RU.md` (commit `366cc63551f7880a8060e4f9badba6ce0d40c5d0`).
- Standard defines format rules, three distinct concept routes, mobile-first preview, visual source fidelity, anti-repetition register, upload integrity, A5→A6 handoff and 16-point quality scorecard (minimum 13/16; critical gates cannot score zero).

### Live visual repair test
- Opened Instagram Creative Picker for `IGI` / `@metanoda.ai` and passed three different art-direction prompts for the monograph-opening draft “Что есть развитие?” / “What is development?”
- Directions: evolving spatial architecture with a human-scale reference; sculptural architecture/continuous transformation; interconnected spatial system with embedded observer.
- Format requested: 1080×1350 (4:5), high quality, no text/logos, no galaxy/portal/neural-network clichés.
- Picker returned the existing asset library and opened the preview workflow. No generated image asset or fresh upload_ref has yet been confirmed in the tool result; status is **preview pending**, not complete.
- No post was published, edited or deleted. Publishing remains paused.

### Completion criteria
The visual process is not declared repaired until a concrete preview is reviewed, a valid new upload_ref is confirmed, the file passes technical validation and the A5 scorecard, and A6 receives the full handoff.


##  Дополнение 11.11.2026 — visual relevance failure / timed technical handoff

Создан обязательный регламент [agents/METANODA_VISUAL_TECHNICAL_EXECUTION_GUIDE_RU.md](../agents/METANODA_VISUAL_TECHNICAL_EXECUTION_GUIDE_RU.md). Он передаёт A5/A6 полный контур: цели, KPI, авторство/источники, аудиторию и воронку, смысловой gate, арт-дирекцию, форматы, технический контроль, сроки, handoff, readiness tests.

### Новый отрицательный пример
Runway task `15ad3fc6-53f6-4b84-86a5-fcf2ec4db957`: предметная композиция ivory planes / translucent sheets / cobalt details отклонена пользователем как “Not relevant content”. Ошибка — общая эстетическая метафора без привязки к конкретной proposition источника. Фактический ratio 3:4 также не соответствовал целевому 4:5. Не использовать как положительный референс.

### Исправление процесса
- До генерации: exact proposition + source locator + meaning map + element-to-source mapping + список запрещённых выводов.
- Content relevance — отдельный критерий 0–2; для выпуска строго 2.
- Новый scorecard 9×0–2, проход ≥15/18; critical zero по source fidelity, mobile legibility, format fit, rights блокирует.
- SLA: feed/cover ≤90 минут; carousel 4–6 слайдов ≤3 часа; Reel 15–30 секунд ≤4 часа; внешнее ожидание фиксировать отдельно.
- Тесты готовности: relevance rejection, task identity, authorship, upload integrity, ratio mismatch.
- Статус передачи корпуса и инструкций не означает fine-tuning модели или развёртывание автономного сервиса. End-to-end readiness pending до прохождения тестов на реальных артефактах.
