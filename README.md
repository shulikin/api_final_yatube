# Проект «API для Yatube»
API инструмент расширяющий возможности социальной сети «Yatube».  
Авторизованные пользователи могут создавать посты, комментировать весь контент и подписываться на других пользователей.  
В иных случаях доступ предоставляется только для чтения.  
## Технологии
![api_yatube](https://shulikin.com/images/py.png) ![api_yatube](https://shulikin.com/images/django.png) ![api_yatube](https://shulikin.com/images/jwt.png) ![api_yatube](https://shulikin.com/images/rest.png)
## Установка и запуск:
1.Клонировать репозиторий и перейти к проекту:
```
git clone https://github.com/shulikin/api_yatube.git && cd api_yatube
```
```
cd yatube_api
```
2.В корневой директории проекта создайте виртуальное окружение, используя команду:
- Если у вас windows
```
python -m venv venv
```
  или
```
py -3 -m venv venv
```
- Если у вас Linux/macOS
```
python3 -m venv venv.
```
3.Активируйте виртуальное окружение командой:
- Если у вас windows
```
source venv/Scripts/activate
```
- Если у вас Linux/macOS
```
source venv/bin/activate
```
4.Обновите менеджер пакетов:
```
python -m pip install --upgrade pip
```
5.Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
6.Выполнить миграции:
```
python manage.py migrate
```
7.Запустить проект:
```
python manage.py runserver
```

## ![api_yatube](https://shulikin.com/images/aend.png)  
Задача API — обеспечить доступ к информации.  
  
### Любой пользователь:  
- получить список всех публикаций
- при указании параметров limit и offset выдача должна работать с пагинацией
```
GET /api/v1/posts/
```
- получение публикации по id
``` 
GET /api/v1/posts/{id}/ 
```
- получение списка доступных сообществ
```
GET /api/v1/groups/
```
- получение информации о сообществе по id
```
GET /api/v1/groups/{id}/
```
- получение всех комментариев к публикации
```
GET /api/v1/{post_id}/comments/ 
```
- получение комментария к публикации по id
```
GET /api/v1/{post_id}/comments/{id}/ 
```
### Аутентифицированный пользователь:  
- публикации
```
POST /api/v1/posts/
PUT /api/v1/posts/{id}/ 
PATCH /api/v1/posts/{id}/  
DEL /api/v1/posts/{id}/  
```
- комментарии
```
POST /api/v1/posts/{post_id}/comments/)  
PUT /api/v1/posts/{post_id}/comments/{id}/)  
PATCH /api/v1/posts/{post_id}/comments/{id}/)  
DEL /api/v1/posts/{post_id}/comments/{id}/)
```
- подписки пользователя, сделавшего запрос
```
GET /api/v1/follow/  
```
- подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса
```
POST /api/v1/follow/  
```
- получение токена  
```
POST /api/v1/jwt/create/  
```
- обнорвление токена  
```
POST /api/v1/jwt/refresh/  
```
- проверка токена  
```
POST /api/v1/jwt/verify/  
```
## Несколько примеров API запроса:
- создание публикации
```
POST /api/v1/posts/ 
в body { "text": "string", "image": "string", "group": 0 }
```
- обновление публикации
```
PUT /api/v1/posts/{id}/ 
в body { "text": "string", "image": "string", "group": 0 }
```
- частичное обновление публикации
```
PATCH /api/v1/posts/{id}/ 
в body { "text": "string", "image": "string", "group": 0 }
```
- удаление публикации
```
DEL /api/v1/posts/{id}/ 
```
- получение токена
```
POST /api/v1/jwt/create/ 
в body { "username": "string", "password": "string" }
```
- обнорвление токена  
```
POST /api/v1/jwt/refresh/  
в body { "refresh": "string" }  
```
- проверка токена  
```
POST /api/v1/jwt/verify/  
в body { "token": "string" }  
```