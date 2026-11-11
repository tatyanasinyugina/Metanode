# Внешний исполнительный контур METANODA
**Версия:** 1.0  
**Дата:** 11.11.2026  
**Статус:** operational contract for scheduled ChatGPT automation; not a standalone always-on server.

## 1. Роли слоёв
1. **GitHub — control plane / source of truth.** Хранит авторские материалы, технологию, правила, версии, handoff, реестр внешних действий и результаты. Рабочая ветка: `agents/social-media-execution`. Не изменять первоисточники и `main`.
2. **Scheduled automation — dispatcher.** Существующая задача ChatGPT Automations «Ежедневное продвижение METANODA» запускает рабочий цикл по расписанию и получает этот контракт и A6 handoff из GitHub. Она не является постоянно работающим процессом между запусками.
3. **Execution tools — external network adapters.** Использовать только реально подключённые действия в текущем запуске: GitHub, Supermetrics/Instagram, vidIQ/YouTube, web research и доступные media tools. Не считать найденный инструмент авторизованным, пока безопасная read-only проверка не подтверждает доступ.
4. **Role stages — A0/A1/A2/A4/A5/A6/A9.** Это последовательные функции внутри dispatcher run, а не отдельные независимые модели/процессы. Каждый этап должен оставить проверяемый результат.
5. **Event log — return path.** После каждого внешнего действия сохранить receipt (provider, account/channel, action, timestamp, status, platform ID, permalink, source refs, limitations) в operations register. Не записывать секреты, tokens, персональные данные или закрытые детские материалы.

## 2. Единый цикл каждого запуска
A. READ: открыть этот контракт, `operations/A6_CONTENT_AGENT_TRAINING_HANDOFF_RU.md`, `operations/SOCIAL_MEDIA_AGENT_EXECUTION_REGISTER_RU.md`, `agents/A6_MEDIA_CHANNEL_EDITOR_RU.md` и первичный авторский источник. Проверить branch/version/SHA.  
B. LOAD: извлечь задачу, ограничения, текущие статусы, публикации, расписания и последние результаты. Не полагаться только на память предыдущего запуска.  
C. RESEARCH: изучить актуальные доступные данные платформ и реальные публичные форматы; фиксировать URLs, даты и ограничения. Не выдавать предположения за измерения.  
D. PRODUCE: подготовить platform-native контент RU/EN, source-to-claim mapping, locator, audience hypothesis, CTA, visual provenance.  
E. QA: пройти task identity, source fidelity, authorship, rights/privacy, RU/EN, visual and technical gates. Любой FAIL блокирует публикацию.  
F. EXECUTE: выполнять только разрешённые действия через внешние официальные интеграции. Не использовать paid ads, покупки, массовые сообщения, накрутку, follow/unfollow или спам. Не публиковать неподтверждённые авторские утверждения, синтетический образ/голос Татьяны или AI-визуалы, для которых требуется review.  
G. VERIFY: повторно запросить статус у платформы. Считать действие завершённым только при подтверждённом provider status; сохранить permalink/ID. Draft, scheduled, approval-required и published — разные статусы.  
H. RETURN: обновить operations register и добавить отчёт запуска в GitHub. Отдельно записать blockers и следующий исполнимый шаг.  
I. REPORT: коротко сообщить пользователю о конкретных изменениях и подтверждениях; если действий не было, указать причину. Не засчитывать исторические публикации как результат нового запуска.

## 3. Подключения и ограничения
- Instagram: `@metanoda.ai`, Supermetrics `ds_id=IGI`, `account_id=17841470456952988`. Перед действиями проверять статус, квоту и отсутствие дублей.
- YouTube: METANODA `@metanoda`, channel ID `UCgcXPGT0dWvqjbdE3wtNAHQ`. Перед действием проверять текущий OAuth account и channel ID через подключённый vidIQ tool. Не утверждать, что подключение/публикация работает, пока конкретный read-only check и publish receipt это не подтверждают.
- Другие каналы: не активны до read-only auth check и успешного внешнего теста.
- GitHub Actions: только детерминированные runner tasks, пока не настроены безопасные model/API credentials. Не считать GitHub Actions LLM-agent runtime.
- Секреты и API keys: не запрашивать в чате, не коммитить в репозиторий, не выводить в логи. Использовать только поддерживаемое защищённое подключение.

## 4. Авторские и редакционные границы
METANODA — авторская система и термин Татьяны Синюгиной. Не приписывать ей AI-интерпретации и редакционные hooks. Цитаты должны быть точными и сопровождаться source locator. Перевод, адаптация, гипотеза и AI interpretation маркируются отдельно. Не переписывать оригиналы и не изменять историю. Не использовать детей/семьи как маркетинговый материал без отдельного согласия. Не клонировать лицо/голос/мимику Татьяны.

## 5. Definition of done
Цикл считается сквозным только если в одном запуске подтверждены:
- GitHub source read + версия/SHA;
- external tool read/write action (не просто перечисление инструмента);
- внешний provider receipt/status;
- сохранённый обратно в GitHub event record;
- проверяемая ссылка на результат.
Если любой пункт отсутствует — статус `PARTIAL` или `BLOCKED`, не `COMPLETE`.

## 6. Честный статус runtime
Этот контракт связывает repository instructions с существующей scheduled ChatGPT automation и подключёнными внешними tools. Он не создаёт отдельные независимые AI-модели, не обеспечивает непрерывное выполнение между запусками и не превращает GitHub Actions в LLM runtime. Для этого потребуется отдельный постоянно работающий orchestration service и защищённый model endpoint. До его появления единственный поддерживаемый автономный режим — запуски существующей scheduled automation с проверкой фактических действий и receipts.
