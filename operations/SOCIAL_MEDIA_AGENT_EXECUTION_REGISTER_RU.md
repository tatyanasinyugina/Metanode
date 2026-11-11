# METANODA — реестр исполнения медиа-агентов

**Рабочая ветка:** `agents/social-media-execution`  
**База:** `ops/metanoda-media-operations`  
**Дата начала:** 11 ноября 2026  
**Статус:** ролевой контур исполняется оркестратором через доступные интеграции; автономные фоновые агенты не развёрнуты.

## 1. Задача
Запустить последовательное исполнение медиа-функций METANODA на действующих социальных каналах с обязательной регистрацией входа, обработки, передачи и внешнего результата.

## 2. Маршрут агентов
| Роль | Функция в задаче | Выход |
|---|---|---|
| A0 | Оркестрация, задача и контроль передачи | Единый отчёт и статусы |
| A1 | Источник, авторство, права, версия | Карточка источника |
| A2 | Смысловая точность и границы интерпретации | Смысловая карта |
| A4 | Проверка формулировок и доказательности | Результат верификации |
| A5 | Визуалы и мультимедиа | Готовый визуал/видео и alt-текст |
| A9 | Перевод и терминология | Сверенная языковая версия |
| A6 | Редакция каналов, публикация и аналитика | Адаптация и подтверждённая запись |

## 3. Подключения, подтверждённые на 11.11.2026
- Instagram Insights/Publishing: источник `IGI`; аккаунт `@metanoda.ai`; account_id `17841470456952988`; авторизация и право публикации проверены через API.
- Instagram publishing quota на момент проверки: 4/100 за скользящие 24 часа; остаток 96 (верхняя граница платформы).
- LinkedIn Company Pages (`LIP`): источник обнаружен, но `NOT_AUTHENTICATED`; публикации не запускать до авторизации владельцем.
- Facebook organic insights (`FB`) доступен как аналитический источник, но текущий `manage_social_media` не предоставляет публикацию Facebook Page.
- Telegram/YouTube: подключённая публикационная интеграция в текущем контуре не подтверждена.
- Основная публичная точка входа: https://tatyana-open-dialogue.gv966ysyr2.chatgpt.site/

## 4. Выполненное действие
- Обнаружена ранее созданная запись Instagram scheduled_id `7844`, account_id `17841470456952988`.
- Запись перенесена с 12.11.2026 09:00 на 11.11.2026 08:10, часовой пояс Asia/Omsk.
- API вернул `success: true`, `status: scheduled`, publish_at_local `2026-11-11T08:10:00+06:00`.
- На момент фиксации это **запланированная**, а не опубликованная запись. После времени публикации A6 обязан проверить фактический статус и сохранить permalink/media_id, если платформа его вернёт.
- Существующая первая публикация не дублируется: https://www.instagram.com/p/DfkiUxZDies/

## 5. Рабочие ограничения
- Не менять авторские оригиналы и `main`.
- Не считать проектные инструкции автономными агентами.
- Не объявлять LinkedIn, Facebook, Telegram или YouTube активными публикационными каналами без фактической авторизации и теста.
- AI-визуалы проходят предусмотренный процесс предварительного просмотра; существующие визуалы используются только после проверки источника и прав.
- Публичные тексты сохраняют различие между авторским фрагментом, редакционной адаптацией и аналитикой ИИ.
- Каждая внешняя публикация требует явного поручения/утверждения и проверки результата.

## 6. Операционный цикл
1. Проверить реестр и не дублировать публикации.
2. Зарегистрировать задачу A0.
3. A1 фиксирует источник, права и версию.
4. A2/A4 проверяют содержание и границы утверждений.
5. A5 готовит медиа; A9 проверяет языковую версию.
6. A6 готовит отдельные platform-native адаптации.
7. Проверить доступы, тип публикации, расписание и квоты.
8. Выполнить validate_only, если поддерживается.
9. Опубликовать или запланировать по прямому поручению.
10. Проверить статус и вернуть результат A0.
11. Зафиксировать URL/ID/время/метрики и следующий шаг.

## 7. Статусы
- `designed` — роль/процесс описан;
- `connected` — интеграция авторизована;
- `validated` — параметры прошли техническую проверку;
- `scheduled` — платформа приняла запись в расписание;
- `published` — платформа подтвердила публикацию;
- `blocked` — зафиксирован конкретный блокер;
- `measured` — получены и записаны метрики.

**Не смешивать эти статусы.** Наличие инструкции не означает deployment; scheduled не означает published.


## 8. Первый аналитический снимок Instagram — 11.11.2026, 08:01 Asia/Omsk

Источник: Supermetrics `IGI`, аккаунт `17841470456952988`, report type `AccountMedia`, диапазон `last_7_days_inc`; запрос завершён, cache_used=false.

В выборке возвращено 5 опубликованных материалов:
- Reel `18138104302642770`: reach 67, likes 0, comments 3, saves 0, shares 0; permalink https://www.instagram.com/reel/DfkoS8DhuNe/
- IMAGE `18132109735827225`: reach 0, likes 1, comments 1; permalink https://www.instagram.com/p/DfkiUxZDies/
- IMAGE `17991938421081819`: reach 0, likes 0, comments 0; permalink https://www.instagram.com/p/Dfkl-JvOoq5/
- VIDEO `17992386372118777`: reach 0, likes 0, comments 0; caption begins “Imaginary conversation of Tatyana Sinyugina and Elon Musk...”
- VIDEO `18122211415978141`: reach 0, likes 0, comments 0; permalink https://www.instagram.com/reel/DflRLjVsfhE/

Нулевые значения метрик у четырёх материалов фиксируются как возвращённые API на момент запроса; они не трактуются как окончательная оценка качества или доказательство отсутствия просмотров.

### Комментарии
Для Reel `18138104302642770` вызван `list_comments`: возвращены 3 комментария, все от собственного аккаунта `metanoda.ai` (`from_account=true`); внешние комментарии в этой выдаче не обнаружены. Ответы не отправлялись.

### Редакционный контроль
- Обнаружен опубликованный ролик с подписью “Imaginary conversation of Tatyana Sinyugina and Elon Musk...”. Это требует отдельной проверки маркировки художественной/AI-реконструкции и прав на изображение/голос до дальнейшего продвижения. Никакие изменения или удаления не выполнялись.
- Подготовленный пятислайдовый carousel проверен визуально: вертикальный формат, единая визуальная система. Слайды 2–4 содержат формулировки, совпадающие с начальным фрагментом монографии; формулировки на слайдах 1 и 5 являются редакционными адаптациями, а не дословными цитатами. Не маркировать их как прямую цитату без уточнения.
- Carousel не загружался и не публиковался в рамках этой операции.

## 9. Текущее состояние публикации
- Scheduled post `7844` подтверждён статусом `scheduled`; назначен на 11.11.2026 08:10 Asia/Omsk.
- Публикация ещё не подтверждена; после времени запуска требуется отдельный `status(scheduled_id=7844)` и фиксация конечного статуса/URL.
- Повторные публикации не создавать, пока не завершена проверка этой записи и не оценена плотность публикаций аккаунта.


## 10. Проверка оптимального часа публикации
- Запрошен отчёт `OnlineFollowers` за последние 30 дней, часовой пояс `Asia/Omsk`.
- API вернул пустой набор `[]`; данные активности подписчиков по часам для этого аккаунта сейчас недоступны в Supermetrics.
- Поэтому время 08:10 назначено как технически допустимое ближайшее окно по прямому поручению, а не как статистически подтверждённый пик аудитории.
- Повторить проверку после накопления достаточного объёма данных и доступности метрики.


## 11. Перезапуск A6 — контроль аудитории и контента, 11.11.2026

**Решение:** прежний контентный подход признан не прошедшим тест на привлечение аудитории. Массовое продолжение публикаций по прежней логике остановлено; опубликованные материалы не изменялись.

### Конфигурация
- A6 обновлён в ветке `agents/social-media-execution`; commit: `888bab72f6dc6361806d82b0c14d8d8eabd56f06`.
- Новый обязательный режим: сегмент аудитории → конкретный вопрос/пример → hook первых 1–3 секунд → одна ценность → один CTA → метрика/окно проверки.
- Введён research gate: минимум 5 смежных публичных аккаунтов/форматов на цикл; фиксировать конкретные URL, примеры публикаций, hook, структуру и наблюдаемое вовлечение; не заявлять исследование без просмотра материалов.
- Введён editorial kill gate: абстрактный hook, непонятная аудитория, повтор общей декларации, отсутствие CTA, неясное авторство/права/согласие или вводящее в заблуждение изображение публичного лица блокируют публикацию.
- Воронка измерения: non-follower reach → watch time/retention → shares/saves → profile visits → attributable follows/link clicks.
- Первые тестовые сегменты — гипотезы: Human–AI/AI builders; systems/cognition/complexity; education/human development. Детская/аутизм-тематика не является единственным позиционированием.
- Правила сохранены в Supermetrics business context для IGI account 17841470456952988; context id 24706.
- Платная реклама не включается без отдельного разрешения и бюджета. Не использовать накрутку, follow/unfollow и спам.

### Аналитика аккаунта: новый снимок
Источник: Supermetrics IGI, account 17841470456952988, запрошено 11.11.2026 около 08:14 Asia/Omsk.
- AccountInsightsDaily за 12.10–10.11: API вернул нули за 29 дней и 10.11: reach 67, accounts_engaged 1, profile_views 68. Примечание: поле profile_views в этой интеграции описано как account-wide content views, а не посещения страницы профиля; не использовать его как profile page visits.
- Follower growth (follower_count) за последние 30 дней: пустой массив [] — значение unavailable, не 0.
- followers_count: API вернул 0; требуется перепроверка через нативный Instagram Insights прежде чем считать это фактическим размером аудитории.
- Audience country и age/gender breakdown: пустые массивы [] — unavailable.
- AccountMedia за last_30_days: 4 материала. Reel 18138104302642770 (https://www.instagram.com/reel/DfkoS8DhuNe/) reach 67, comments 3, likes/saves/shares 0; три остальных материала на момент запроса вернули reach 0. Для media 17992386372118777 caption “Imaginary conversation of Tatyana Sinyugina and Elon Musk...” — редакционный/правовой стоп-фактор до проверки маркировки AI-реконструкции и прав.
- Ни один из этих результатов не подтверждает устойчивый прирост подписчиков или эффективную конверсию в подписку.

### Внешний первичный обзор форматов
11.11.2026 выполнен поисковый обзор открытых источников. Найдены смежные ориентиры:
- @cleoabram — научно-технологические видео-объяснения через наглядный сюжет; источник: https://it-klett.de/en/ai-media-tips-ai-sources/
- @cahdoria — короткие материалы по AI literacy/этике ИИ; тот же источник.
- @hubermanlab — нейронаучное объяснение через регулярный видеосериал; сторонний публичный обзор: https://igdatahub.com/blog/hubermanlab-instagram-profile-stats/
- @philosophyofexistence — философия, соединённая с психологией, литературой и общественными вопросами; сторонний профильный обзор: https://creatordb.app/creatorstats/philosophyofexistence/
- @sternstoic — короткая практическая философия с широким повседневным framing; разбор: https://www.oleg.ae/creators/sternstoic

Это shortlist для последующего просмотра, а не завершённый сравнительный аудит отдельных Reels: свежие публикации каждого аккаунта и их метрики ещё не проверены. Источники о механике Instagram указывают на важность watch time, shares/sends и оригинального контента; это ориентир для тестов, не гарантия результата: https://blog.hootsuite.com/instagram-algorithm/ ; https://buffer.com/resources/instagram-algorithms/ ; https://www.socialmediatoday.com/news/instagram-reels-recommendations-tips/741030/

### Следующий допуск
До нового серийного выпуска: провести ручную проверку профиля и последних публикаций shortlist, подготовить 3 сегментных концепции с 2 hook-вариантами каждая, проверить авторство/визуалы, затем выпустить ограниченный тестовый пакет и измерять 24–48 часов и 7 дней. Никакой массовой публикации по старому плану.


## 12. Запуск первого теста аудитории — 11.11.2026

**Публикация подтверждена Instagram:**
- Аккаунт: @metanoda.ai (IGI, account_id 17841470456952988)
- Формат: IMAGE, публикация немедленно.
- media_id: 18094224926280271
- permalink: https://www.instagram.com/p/DflZDLwjJzI/
- upload_ref: upl_CXIhCd7nZNAGTm8LaMMr3g (ранее сохранённый AI-визуал luminous geometric passage threshold)
- Квота после публикации: 94 поста в 24-часовом окне.
- Dry-run прошёл: parameters valid, media reachable over HTTPS, write access confirmed, quota passed.
- Публикация прошла со статусом applied; Instagram permalink получен.

### Гипотеза первого теста
- Сегмент: Human–AI / AI builders.
- Hook: “Can an AI continue a line of thought when the next step has not yet been formulated?”
- Содержание опирается на исследовательский вопрос, изложенный в книге Татьяны Синюгиной: удержание новой системы определений, отказ от автоматического возврата к наиболее вероятной известной модели, продолжение к ещё не сформулированному знанию.
- В тексте явно обозначено: это исследовательский вопрос, не утверждение о сознании ИИ и не заявление о доказанном механизме.
- RU + EN caption; CTA — вопрос о том, что проверять первым.
- Метрика: reach/non-follower reach, shares, saves, comments, profile visits и follows, если соответствующие показатели будут доступны.
- Оценка: ранний сигнал через 24–48 часов, повторная оценка через 7 дней. Не объявлять тест успешным только по факту публикации.

### Ограничение
Публикация изображения — первый входной тест, не полноценная Reels-кампания. Следующий материал не выпускать автоматически до проверки первых сигналов и подготовки второго формата (короткий explainer Reel с тем же смысловым ядром, но другим hook).


## 13. A6 content-agent training and failure transfer — 11.11.2026

**User instruction:** train the content agent on Tatyana Sinyugina's materials in the repository; transfer all tasks, remarks, analysis and results from this conversation; prepare a new result and check Instagram after five minutes.

### Repository handoff
- Added `operations/A6_CONTENT_AGENT_TRAINING_HANDOFF_RU.md` (commit `4fc2e5c38aaef8d75ea675073e0adfe55f48776c`).
- Updated `agents/A6_MEDIA_CHANNEL_EDITOR_RU.md` with mandatory source corpus, task-identity gate, source-to-post trace, editorial release gates and explicit limitations of technical validation.
- The primary source is `Метанода_Татьяны_Синюгиной_RU_EN 2.md`; the GPT adaptation and technical method references are listed separately. Application analyses are not to be misattributed to the monograph.
- Source corpus and conversation handoff are now present in the working branch; no changes to `main`.

### Newly documented failures
1. `18094224926280271` / https://www.instagram.com/p/DflZDLwjJzI/ — the assistant generated an interpretation about AI holding a new system of definitions and attributed it to the author's book without verifying the exact passage. Rejected as unsupported attribution.
2. `17995943901056987` / https://www.instagram.com/p/DflZni7jMeQ/ — the assistant changed the subject to its own execution process when the user asked to restart the METANODA post. Rejected as task-object substitution.

Both records remain published and untouched. Neither is accepted as a corrected author-based post. Technical `validate_only` checks were successful, but they did not verify meaning or task identity; the gate design was insufficient in execution.

### User instructions transferred
- Manage the connected Instagram channel; avoid asking the user to repeat established details.
- Keep RU and EN versions, make the entry simple and inviting without distorting the author's meaning.
- Do not rewrite Tatyana Sinyugina's original text or attribute AI adaptations to her.
- Do not default every post to children/autism; do not use vulnerable participants as marketing hooks.
- Research audience formats honestly; record actual sources and distinguish observations from hypotheses.
- Aim for relevant audience acquisition and meaningful conversion, not posting volume.
- No paid promotion or spending without explicit permission; no fabricated celebrity conversations or unsupported claims.

### New execution status
- A6 handoff and source references are recorded in the branch.
- “Training” here means source corpus + operational instructions + negative examples; no model fine-tuning or autonomous deployment is claimed.
- Publishing remains paused until a draft passes the new source-to-post readiness test. The five-minute Instagram check is a separate verification task; it must report the actual latest media and not assume a new post exists.


## 14. A6 source-to-post validation draft — 11.11.2026

- Added `operations/A6_POST_DRAFT_001_DEVELOPMENT_RU_EN.md` (commit `af9c8b42c660bb3663f44487f2809284cd32474d`).
- Task identity: public METANODA post grounded in T. I. Sinyugina's monograph, not AI self-analysis.
- Exact source checked in the monograph opening: “Что есть развитие?”; “Развитие — это способ существования человека.”; “Развитие — это способ существования Космоса.”; and the sentence defining development as a fundamental mode of existence of the human being and the Cosmos.
- Draft caption prepared in RU/EN. English quote is labelled as an editorial translation, not as a separately verified original English quote. Hook is labelled as editorial adaptation.
- A6 source fidelity, attribution and task-identity gates passed on the draft.
- Media gate blocked: existing slide 2 upload_ref `upl_UgaGZFG7URpqQVYNHYtI2A` was rejected by Instagram publishing API as missing/0 bytes. No post was scheduled or published; no media_id/permalink exists for this draft.
- Creative Picker is already open for preview/upload. Required next technical action is a fresh upload there and use of the returned upload_ref. Do not call Creative Picker again until the user responds with the uploaded asset.
- A6 end-to-end readiness remains pending; no claim of completed training/deployment.
