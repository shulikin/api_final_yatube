![api_yatube](https://shulikin.com/images/Api.png)
# Проект «API для Yatube»
API для сервиса yatube. Позволяет запрашивать данные о постах, группах и комментариях в социальной сети Yatube, а также управлять ими.
## Технологии
![api_yatube](https://shulikin.com/images/py.png) ![api_yatube](https://shulikin.com/images/django.png) ![api_yatube](https://shulikin.com/images/jwt.png) ![api_yatube](https://shulikin.com/images/rest.png)
## Как запустить
1. Клонируем репозиторий и переходим в него в командной строке
# Проект «API для Yatube»
### API для Yatube представляет собой проект социальной сети, в котором реализованы возможности публиковать записи, комментировать записи, а также подписываться или отписываться от авторов.

## Технологии
Python, Django, DRF, JWT + Djoser

## Установка и запуск::
Клонировать репозиторий и перейти к проекту:
```
git clone https://github.com/shulikin/api_yatube.git && cd api_yatube
```
```
cd yatube_api
```
В корневой директории проекта создайте виртуальное окружение, используя команду:
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

- 3.Активируйте виртуальное окружение командой:
- Если у вас windows
```
source venv/Scripts/activate
```
- Если у вас Linux/macOS
```
source venv/bin/activate
```

```
python3 -m venv venv
```
- Если у вас Linux/macOS

```
source venv/bin/activate
```


```
python -m pip install --upgrade pip
```



Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python manage.py migrate
```
Запустить проект:

```
python manage.py runserver
```
![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
По умолчанию для неавторизованных пользователей проект доступен только для чтения.
```
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
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
