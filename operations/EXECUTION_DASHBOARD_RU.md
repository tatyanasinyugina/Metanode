# METANODA — панель контроля исполнения

Рабочая ветка: `agents/social-media-execution`

## Как проверять каждый цикл

1. Открыть [GitHub Actions — METANODA A0 Runtime](https://github.com/tatyanasinyugina/Metanode/actions/workflows/metanoda-a0-runtime.yml).
2. Выбрать конкретный запуск и проверить оба задания:
   - **Validate source and handoff package** — проверка исходников;
   - **Deliver queued task to external executor** — передача наружу и возврат receipt.
3. Открыть receipt по тому же `github_run_id` в `operations/receipts/`.
4. Сверить статусы и внешнее доказательство результата. Успешный GitHub run сам по себе не означает, что внешнее действие выполнено.

## Текущий цикл: METANODA-OUTBOUND-2026-11-11-01

- [GitHub Actions run #10](https://github.com/tatyanasinyugina/Metanode/actions/runs/43044285780)
- [Задание](https://github.com/tatyanasinyugina/Metanode/blob/agents/social-media-execution/operations/OUTBOUND_EXECUTION_REQUEST_2026-11-11_01.md)
- [Receipt](https://github.com/tatyanasinyugina/Metanode/blob/agents/social-media-execution/operations/receipts/43044285780_outbound.json)

| Этап | Подтверждённый статус |
|---|---|
| Задание в GitHub | QUEUED |
| Проверка исходников A0 | PASS |
| Конфигурация внешнего исполнителя | BLOCKED — секреты METANODA_EXECUTOR_URL / METANODA_EXECUTOR_TOKEN не настроены |
| Отправка внешнему исполнителю | SKIPPED — запрос не отправлялся |
| Receipt возвращён в GitHub | YES |
| Подтверждение внешнего сервиса | NOT_RECEIVED |
| Публикация | NOT_AUTHORIZED |

## Критерий завершения

Цикл считается **VERIFIED** только если одновременно имеются:
- подтверждение принятия задания внешним исполнителем;
- подтверждение фактического действия от целевого сервиса;
- независимая проверка результата (например, открывающаяся публичная ссылка публикации);
- receipt, возвращённый в этот репозиторий и связанный с исходным request ID.

Статусы `PASS` у GitHub Actions, `ACCEPTED` у исполнителя и `VERIFIED` у результата — разные вещи. Не объединять их в один общий статус.

## Безопасность

Не хранить токены, ключи, персональные данные или приватные материалы в этом журнале. Секреты задаются только в защищённых GitHub Actions Secrets. Не публиковать материалы до отдельного разрешения на конкретную публикацию.
