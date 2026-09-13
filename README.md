# Django Notes web-app

Это приложение повзоляет создавать, читать и удалять заметки, а еще размечать их по тегам. Также возможно изменить тему самого приложения и размер шрифта.

## Установка и запуск приложения

Создайте директорию в который вы хотите установить приложение. Затем, через команду git clone скопируйте данный репозиторий и дальше просто запускаете через manage.py фаил.

Последовальность комманд для запуска:
```
mkdir notes_app
cd notes_app

git clone https://github.com/RocetDev/Django_notes_app.git
cd Django_notes_app

# Если у вас просто Python
pip install -r requirements.txt
python manage.py runserver

# Если у вас стоит uv (Рекомендуется)
uv sync
uv run mangage.py runserver
```
