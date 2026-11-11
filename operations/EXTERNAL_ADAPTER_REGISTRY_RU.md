# Реестр внешних адаптеров METANODA
**Проверка:** 11.11.2026  
**Ветка:** agents/social-media-execution  
**Назначение:** фиксировать только реально обнаруженные подключения. Наличие инструмента не означает разрешение на публикацию.

## Подтверждённые read-only подключения

| Адаптер | Проверка | Результат | Граница |
|---|---|---|---|
| Supermetrics / Instagram Insights (IGI) | data source discovery | AUTHENTICATED | Доступ к данным Instagram; аккаунт сверяется через accounts discovery |
| Supermetrics / Instagram | accounts discovery | FOUND: metanoda.ai, account ID 17841470456952988 | Не считать проверкой публикации |
| vidIQ / YouTube | user channels | FOUND: @metanoda, channel ID UCgcXPGT0dWvqjbdE3wtNAHQ | Read-only проверка канала |
| vidIQ / Social accounts | social account list | Instagram и YouTube: active; canPublish=true | Подготовка черновика и публикация — разные операции; публикация только после отдельного разрешения |
| Runway | whoami | AUTHENTICATED; workspace найден | Доступные image models перечислены провайдером; video models в проверке не возвращены |
| HeyGen | get current user | Подключение отвечает | Функциональные права на создание/публикацию отдельно не подтверждены |
| Higgsfield | get profile + models_list(type=video) | AUTHENTICATED; Seedance 1.5 Pro, Seedance 2.0, Seedance 2.0 Mini и Seedance 2.5 доступны в каталоге | Генерация видео расходует ресурсы/кредиты; отдельная генерация не запускалась |
| ByteDance Seedance via Higgsfield | model catalog | Seedance 2.5 подтверждён; режимы t2v, omni_reference, video_edit, video_extension; 4–30 сек; 480p/720p/1080p | Вызывается через подключённый Higgsfield generate_video; перед каждой платной генерацией требуется оценка стоимости и отдельное подтверждение пользователя |
| ByteDance Seedance via vidIQ | tool schema | Seedance 2 и Seedance 2 Fast доступны как модели vidiq_generate_video | Асинхронная генерация платная по кредитам; использовать только после предварительного показа цены и явного подтверждения |
| Lovable | get me | Подключение отвечает; 1 workspace | Не включать как обязательную зависимость; учитывать ранее зафиксированное ограничение по кредитам до повторной проверки |

## Не подтверждено в этой проверке

- Универсальный постоянно работающий внешний executor endpoint.
- Прямой LinkedIn publishing adapter: найден только поиск людей LinkedIn.
- Автоматическое выполнение GitHub Actions внешних вызовов Supermetrics/vidIQ: GitHub runner не имеет прямого доступа к этим ChatGPT connector tools.
- Автономная работа между запусками без существующей ChatGPT Automation.

## Правила диспетчеризации

1. Агент может подготовить execution ticket, но не может сам считать его разрешением на публикацию.
2. Для Instagram учитывать Supermetrics IGI и точный account ID из реестра.
3. Для YouTube/Instagram через vidIQ передавать только точный platformAccountId, полученный из свежего vidiq_social_account_list; username не подставлять вместо ID.
4. Перед публикацией — отдельное явное разрешение пользователя на конкретный материал, канал и действие.
5. После внешнего действия — запросить provider status, сохранить platform ID/permalink и receipt в GitHub.
6. Если адаптер не подтверждён или инструмент недоступен — BLOCKED, без имитации исполнения.

## Авторство и конфиденциальность

METANODA — авторская система и термин Татьяны Синюгиной. Не отправлять внешним сервисам закрытые авторские материалы, частные исследовательские данные, сведения о детях/семьях, персональные данные или секреты без отдельного явного разрешения.
