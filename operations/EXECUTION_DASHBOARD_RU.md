# METANODA — панель контроля исполнения

Рабочая ветка: `agents/social-media-execution`

## Исполнительная схема

- **GitHub / A0** — источник заданий, проверка, маршрутизация и журнал receipts.
- **Supermetrics** — прямой исполнитель разрешённых операций в подключённых социальных каналах.
- **TinyFish** — прямой исполнитель отдельных браузерных задач по конкретному запросу.
- **Runway** — создание и обработка медиа; не исполнитель публикаций.
- **Lovable** — ИСКЛЮЧЁН из рабочей цепочки: в текущем workspace исчерпаны кредиты; не использовать как обязательную зависимость и не закладывать расходы.
- Постоянный универсальный внешний executor endpoint пока НЕ РАЗВЁРНУТ. Не считать доступные инструменты автономными агентами или объединённой системой до появления проверенного межсервисного запуска.

## Как проверять каждый цикл

1. Открыть [GitHub Actions — METANODA A0 Runtime](https://github.com/tatyanasinyugina/Metanode/actions/workflows/metanoda-a0-runtime.yml).
2. Проверить оба задания: **Validate source and handoff package** — проверка исходников; **Deliver queued task to external executor** — сейчас заблокирован, пока не настроен внешний endpoint.
3. Открыть receipt по тому же `github_run_id` в `operations/receipts/`.
4. Сверить статусы и внешнее доказательство. Успешный GitHub run сам по себе не означает исполнения.

## Текущий цикл: METANODA-OUTBOUND-2026-11-11-01

- [GitHub Actions run #10](https://github.com/tatyanasinyugina/Metanode/actions/runs/43044285780)
- [Задание](https://github.com/tatyanasinyugina/Metanode/blob/agents/social-media-execution/operations/OUTBOUND_EXECUTION_REQUEST_2026-11-11_01.md)
- [Receipt](https://github.com/tatyanasinyugina/Metanode/blob/agents/social-media-execution/operations/receipts/43044285780_outbound.json)

| Этап | Подтверждённый статус |
|---|---|
| Задание в GitHub | QUEUED |
| Проверка исходников A0 | PASS |
| Универсальный внешний endpoint | NOT DEPLOYED |
| Конфигурация endpoint в GitHub Secrets | BLOCKED — METANODA_EXECUTOR_URL / METANODA_EXECUTOR_TOKEN отсутствуют |
| Отправка внешнему исполнителю | SKIPPED — запрос не отправлялся |
| Receipt возвращён в GitHub | YES |
| Подтверждение внешнего сервиса | NOT_RECEIVED |
| Публикация | NOT_AUTHORIZED |

## Критерий завершения

Цикл считается **VERIFIED** только если имеются: подтверждение принятия задания внешним исполнителем; подтверждение фактического действия целевого сервиса; независимая проверка результата; receipt в этом репозитории, связанный с исходным request ID.

`PASS` у GitHub Actions, `ACCEPTED` у исполнителя и `VERIFIED` результата — разные статусы.

## Безопасность

Не хранить токены, ключи, персональные данные или приватные материалы в журнале. Секреты — только в защищённых хранилищах. Не публиковать материалы без отдельного разрешения на конкретную публикацию.