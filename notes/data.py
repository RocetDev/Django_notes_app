import uuid

NOTES = [
    {"id": str(uuid.uuid4()), "title": "Идея проекта", "text": "Сделать сайт заметок на Django", "tag": "работа"},
    {"id": str(uuid.uuid4()), "title": "Список покупок", "text": "Хлеб, молоко, яйца", "tag": "личное"},
    {"id": str(uuid.uuid4()), "title": "Книги на лето", "text": "Достоевский, Толстой, Чехов", "tag": "хобби"},
]

TAGS = ["работа", "личное", "хобби", "учёба"]

THEMES = {
    "light": {"name": "Светлая", "bg": "#ffffff", "fg": "#222222"},
    "dark":  {"name": "Тёмная",  "bg": "#1e1e1e", "fg": "#f0f0f0"},
    "sepia": {"name": "Сепия",   "bg": "#f4ecd8", "fg": "#5b4636"},
}

FONTS = [14, 16, 18, 20, 22]