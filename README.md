
# 📚 Library API — FastAPI + JWT + Alembic

RESTful API для управления библиотечным каталогом: книги, читатели, выдача и возврат.  
Проект выполнен по техническому заданию для стажера Python-разработчика.

---

## 🚀 Запуск проекта

```bash
# Установка
git clone https://github.com/MadiKaliyev/library.git
cd library
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Запуск приложения
uvicorn app.main:app --reload
```

По умолчанию используется SQLite (файл `library.db` создается автоматически).

---

## 👤 Регистрация первого библиотекаря

1. Перейти в Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Вызвать `POST /auth/register`:
```json
{
  "email": "admin@example.com",
  "password": "123456"
}
```
3. Затем `POST /auth/login` и вставить `access_token` через кнопку **Authorize**.

---

## 📂 Структура проекта

```
app/
├── api/         # Маршруты (auth, books, readers, borrowed)
├── crud/        # CRUD-логика
├── models/      # SQLAlchemy модели
├── schemas/     # Pydantic-схемы
├── core/        # Настройки, безопасность
├── database/    # Подключение к базе данных
├── main.py      # Точка входа
alembic/         # Миграции Alembic
.env             # Переменные окружения
```

---

## 🧱 Принятая структура базы данных

- `users`: библиотекари, авторизуются по email/password
- `books`: книга с полями title, author, year, isbn, count, description
- `readers`: читатели библиотеки, управляются библиотекарями
- `borrowed_books`: связи книг и читателей с датами выдачи и возврата

---

## 🔐 Аутентификация

Используется OAuth2 + JWT:
- `python-jose` для токенов
- `passlib[bcrypt]` для хеширования паролей
- Все `CRUD`-эндпоинты защищены `Depends(get_current_user)`
- Только `/auth/register` и `/auth/login` — публичные

---

## 🔄 Миграции Alembic

1. Первая миграция — `create initial tables`
2. Вторая миграция — `add description to books`

```bash
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head

alembic revision --autogenerate -m "add description to books"
alembic upgrade head
```

---

## 📊 Реализация бизнес-логики

**4.1. Выдача книги (`/borrowed/borrow`)**
- Проверяется, что `book.count > 0`
- У читателя не должно быть более 3 книг

**4.2. Возврат книги (`/borrowed/return`)**
- Нельзя вернуть книгу дважды
- Кол-во экземпляров увеличивается
- Устанавливается `return_date`

**4.3. Получение всех книг читателя (`/borrowed/reader/{reader_id}`)**
- Возвращаются книги без `return_date`

**Сложности:** реализовать проверку количества активных книг у читателя, логика вложена в `crud/borrowed.py`.

---

## ✅ Пример защищённого эндпоинта

```bash
POST /books/
Authorization: Bearer <ваш токен>
Content-Type: application/json

{
  "title": "Капитанская дочка",
  "author": "Александр Пушкин"
}
```

---

## ✅ Комментарии по PEP8 и архитектуре

- Все модули разделены по назначению (CRUD, модели, схемы, API)
- Типизация и `from_attributes = True` для Pydantic v2
- Использован `.env` для переменных
- Все команды протестированы в Swagger UI

---

## ✅ Осмысленные коммиты

- `🎉 Initial commit`
- `🔐 Add auth and user creation`
- `📚 Add book model and logic`
- `🛠️ Alembic initial migration`
- `✨ Add description field to books`

---

## ✨ Дополнительная фича (идея)

**Автооповещение о просроченных книгах:**  
Добавить `due_date` + фоновый скрипт, который проверяет непросроченные книги и ставит флаг `overdue = True`. Это можно расширить до уведомлений по email.

---

## 🧪 Тестирование (Pytest)

Добавить файл `tests/test_logic.py`:
- попытка взять 4 книги
- выдача книги с `count = 0`
- возврат книги дважды

📌 Тесты можно запускать так:

```bash
pytest
```

---

## 🧾 Лицензия

MIT License — свободно использовать, дорабатывать, показывать на собеседованиях.  
Дата завершения: **2025-05-18**
