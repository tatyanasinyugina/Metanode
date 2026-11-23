# Project Change Control and Preservation Rules

**Purpose:** make the repository's existing preservation rules easy to find. This file is a navigation aid and a concise operational reminder; it does not replace or supersede the original protocols.

## Canonical rules already present in the project

The following documents were written for this repository before the current documentation task. They remain the governing references:

1. [Git workflow and source-tree model](https://github.com/tatyanasinyugina/Metanode/blob/agents/first-contour-instructions/process-log/GIT_WORKFLOW_AND_SOURCE_TREE_RU.md) — defines the authorial trunk, derivative work branches, provenance, verification, and controlled return of results.
2. [Process-log rules](https://github.com/tatyanasinyugina/Metanode/blob/agents/first-contour-instructions/process-log/README.md) — requires every record to state what was taken from sources, added, changed, left untouched, checked, not checked, and what comes next.
3. [Universal exchange protocol](https://github.com/tatyanasinyugina/Metanode/blob/agents/first-contour-instructions/process-log/UNIVERSAL_EXCHANGE_PROTOCOL_RU.md) — establishes the mandatory cycle **TAKE → PROCESS → RETURN** and says a return never automatically changes the authorial trunk.
4. [Chronological process changelog](https://github.com/tatyanasinyugina/Metanode/blob/process-log/metanoda-ai-ecosystem/process-log/CHANGELOG.md) — append-only history; old entries are not rewritten.

## Non-negotiable preservation rules

- The author's original texts, definitions, methods, technologies, and source files are the **authorial trunk**. Preserve their wording, structure, filenames, versions, and history.
- Never rewrite, reorganize, shorten, rename, replace, or delete an original source to fit a temporary task, a new audience, a public figure, a product, or a research direction.
- Work derived from a source belongs in a separate, clearly named working branch and/or separate file. Every derivative identifies the exact source and version used.
- A correction to an original source is a new proposed version, never an overwrite. It requires the author's explicit approval.
- Keep source statements, verbatim extracts, editorial restructuring, AI interpretation, hypotheses, observations, and verified results visibly distinct.
- Preserve prior files, commits, and decisions. Add a new version or an append-only log entry; do not silently erase history.
- A Git commit or merge is a technical event, not proof that a result has been accepted into the author's system.
- Do not merge work into `main` or return it to the authorial trunk without the relevant review and explicit approval.
- Do not claim that a workflow, agent, integration, publication, or contact is operational without evidence of a real test or event.

## Required record for every substantial task

Use the project's existing process-log template and record:

1. source materials and exact versions/locators;
2. files or artifacts added;
3. any changes made, with before/after and reason;
4. materials explicitly left untouched;
5. checks performed and results;
6. limitations and items not checked;
7. next steps, dependencies, and responsible person;
8. commit and pull-request identifiers.

## Applying the rules to this documentation work

- The monograph and original authorial materials in `main` are not edited by this task.
- The existing root `README.md` is restored byte-for-byte to the current `main` version in the documentation branch; the previous proposed replacement is withdrawn.
- The library index and structure guide are additional navigation documents, not replacements for the author's structure.
- The Elon Musk reader path is maintained in its own communication branch and is not part of the authorial trunk.
- No changes are merged into `main` by this work.

**Operating principle:** preserve the source; develop connections around it; return only verified, attributed, approved results; keep the history intact.
