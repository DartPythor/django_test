# django_test
## Запуск проекта

### env файл
Создайте .env файл по примеру из example.env
### Docker-compose
Для запуска проекта нужно в корневую папку проекта и запустить:
```commandline
docker-compose up
```

### Требования
Для корректной работы проекта необходимо установить зависимости:

1. Установить продакшн зависимости:
   ```commandline
   pip install -r requirements/prod.txt
   ```
2. Установить тестовые зависимости:
    ```commandline
    pip install -r requirements/test.txt
    ```
3. Установить зависимости для разработки:
    ```commandline
    pip install -r requirements/dev.txt
    ```
Если вы хотите установить все зависимости одной командой, просто используйте:
```commandline
pip install -r requirements/requirements.txt
```

## Контакты
Maxim - [Telegram](https://t.me/maximneverov) - perobyte@yandex.ru