# Онлайн-магазин наушников

В проекте пока реализована не полностью бэкенд авторизации /register, /login. И немного Frontend

## Технический стэк

## Backend
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Alembic**
- **authx**
- **Pydantic**

## Frontend
- **HTML + CSS**
- **JavaScript**

## Как запустить 
В проекте используется пакетный менеджер `uv`, но можно использовать и `pip`.
Перед тем как запустить проект нужно создать какую-нибудь бд, после создать в главной директории проекта файл ENV и заполнить его примерно в таком виде, что ниже, но со своими данными:
```
USER='postgres'
HOST='localhost'
PASSWORD='postgres'
DATABASE='database'
PORT=5432
```

### Если использовать uv
```bash 
pip install uv # если не установлен
uv sync
```

## Если pip
```bash
python -m venv .venv
.venv/Scripts/activate
pip install -requirements.txt
```

## После нужно запустить файл products.py чтобы главная страница работала корректно
```
python products.py
```

## Запуск Backend
```bash
uvicorn main:app
```

## Запуск Frontend
Зайти в папку templates и оттуда с помощью расширения `Open with Live Server` запустить(можно по-другому, но я делал так)

## Над проектом работают:
- Рахманов Русиф
- Чиковани Андрей

# Артем Вадимович, простите что мы так мало чего реализовали🙏🙏🙏, но мы старались 






