*# API_FINAL*
---
### Описание:
API для социальной сети Yatube: cайт со статьями авторов по интересам.
С помощью Api для Yatube возможно:
* Создавать пост
* Запросить все записи автора
* Подписаться на автора
* Комментировать записи автора
---
### Установка:

1. Создать виртуальное окружение

*python -m venv venv*

2. Активировать виртуальное окружение

*source venv/scripts/activate*

3. Установить зависимости

*pip install -r requirement.txt*

---
### Доступные методы API запросов:
метод                                            | GET | POST | PUT | PATCH | DEL |
-------------------------------------------------|-----|------|-----|-------|-----|
/api/v1/token/ | - | V | - | - | - |
/api/v1/token/refresh/ | - | V | - | - | - |
/api/v1/posts/  | V | V | - | - | - |
/api/v1/posts/{id}/ | V | - | V | V | V |
/api/v1/posts/{post_id}/comments/ | V | V | - | - | - |
/api/v1/posts/{post_id}/comments/{comment_id}/ | V | - | V | V | V |
/api/v1/follow/ | V | V | - | - | - |
/api/v1/group/ | V | V | - | - | - |

---

