# METANODA Analytics and Provenance Plan

**Status:** plan documented. This file does not enable a new analytics integration.

## 1. GitHub repository analytics

Use GitHub **Insights → Traffic** where repository access permits. Aggregate indicators include views, unique visitors, clones, unique cloners, referrers, and popular content paths.

GitHub's traffic dashboard exposes a rolling 14-day window. It does not identify individual visitors. A clone is not proof that the repository was read, used, or adopted.

Official documentation:
- https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository
- https://docs.github.com/en/rest/metrics/traffic

## 2. Historical retention

If the repository owner approves, a scheduled GitHub Action may periodically retrieve aggregate traffic metrics and store dated snapshots. Before enabling it:
1. obtain repository-owner approval;
2. use least-privilege permissions;
3. keep secrets in GitHub Actions secrets, never in repository files or chat;
4. document frequency and retention;
5. store aggregate metrics only;
6. test the workflow and verify real API responses.

No token or workflow has been configured by this documentation change.

## 3. Author's website

Author's website: https://tatiana-siniugina.gv966ysyr2.chatgpt.site/

The project currently has **no administrative access**. No analytics code has been installed and no website visitor data is available to this repository workflow. If the owner later grants access, review existing analytics and privacy requirements before making changes. Do not introduce covert individual tracking.

## 4. Publication metrics

For each public release, record canonical URL/platform, publication date/time and time zone, content format/source, transparent referral tags if used, platform-reported metrics, collection date/window, provider, and metric caveats.

Do not treat unavailable values as zero. Do not equate reach, views, clicks, clones, citations, adoption, or impact.

## 5. Provenance and privacy

Record exact title, contributor roles, version/date, file path, source relationship, and Git commit/blob SHA where available. Preserve originals and distinguish AI-assisted transformations. Use aggregate statistics in public reporting; never publish access tokens, private user data, or confidential correspondence.
