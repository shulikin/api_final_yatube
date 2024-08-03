![api_yatube](https://shulikin.com/images/Api.png)
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
![api_yatube](https://shulikin.com/images/ok.png)  

## API endpoint:
# Любой пользователь:  
- получить список всех публикаций
- при указании параметров limit и offset выдача должна работать с пагинацией
```
GET api/v1/posts/
```
- получение публикации по id
``` 
GET api/v1/posts/{id}/ 
```
- получение списка доступных сообществ
```
GET api/v1/groups/
```
- получение информации о сообществе по id
```
GET api/v1/groups/{id}/
```
- получение всех комментариев к публикации
```
GET api/v1/{post_id}/comments/ 
```
- получение комментария к публикации по id
```
GET api/v1/{post_id}/comments/{id}/ 
```



За исключением эндпоинта follow, доступен только авторизованных пользователей.
```
api/v1/follow/ - получение подписок текущего пользователя
api/v1/follow/{id}/ - получение одной подписки
```
Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
```
POST /api/v1/posts/ - создание публикации
в body { "text": "string", "image": "string", "group": 0 }

PUT /api/v1/posts/{id}/ - обновление публикации
в body { "text": "string", "image": "string", "group": 0 }

PATCH /api/v1/posts/{id}/ - частичное обновление публикации
в body { "text": "string", "image": "string", "group": 0 }

DEL /api/v1/posts/{id}/ - удаление публикации
```
## Добавить группу в проект нужно через админ панель Django:
```
admin/ - после авторизации, переходим в раздел Groups и создаем группы
```
Доступ авторизованным пользователем доступен по JWT-токену
```
POST /api/v1/jwt/create/ - получение токена

{
"username": "string",
"password": "string"
}

POST /api/v1/jwt/refresh/ - обнорвление токена
POST /api/v1/jwt/verify/ - проверка токена
```

Также в проекте реализована пагинация(LimitOffsetPagination).
