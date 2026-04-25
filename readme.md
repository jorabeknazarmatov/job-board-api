# Job Board / Freelance Marketplace API
**Суть: платформа для публикации задач и откликов**

**Функционал**:

- JWT-аутентификация (access/refresh)
- Роли: заказчик / исполнитель
- CRUD вакансий и откликов
- Фильтрация, пагинация, поиск
- Система откликов + статус (accepted/rejected)

**Технологии:**

- FastAPI + PostgreSQL + SQLAlchemy
- Redis (кэш или rate limit)
- Alembic (миграции)

**Что делает проект сильным:**

- Чёткая бизнес-логика
- Работа с отношениями (User → Job → Application)
- Реальный use-case (можно показать на фрилансе)