# api_final
## Проект по реализации API

Создано с помощью Django REST Framework

### Описание:
реализация API для социальной сети (сайт, на котором можно создать свою страницу, посмотреть все записи автора, подписаться на авторов и комментировать их записи).

### Установка:
Для установки ПО необходимо установить зависимости

*pip install -r requirement.txt*

### Доступные методы:
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


### Примеры:

    import requests

    api = 'http://localhost:8000/api/v1/posts/'
    headers - {'Authorization': 'Bearer <токен>'}
    request = requests.get(api,headers=headers)

