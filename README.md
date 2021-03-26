# frtest
```sh
$ git clone https://github.com/drrros/frtest.git
$ cd frtest
$ mkdir env && mkdir db && mkdir static && chmod -R 777 static
$ cat <<EOF >> env/env.env
DJANGO_SECRET_KEY='(z@hn##5($123456w56xs$2abmz*rag(pyvo7u23a#i2uer1l'
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=*
DJANGO_LOG_LEVEL=INFO
POSTGRES_DB=frtest
POSTGRES_USER=postgres
POSTGRES_PASSWORD=SuperPassword123
DJANGO_SQL_ENGINE=django.db.backends.postgresql
DJANGO_SQL_DATABASE=frtest
DJANGO_SQL_USER=postgres
DJANGO_SQL_PASSWORD=SuperPassword123
DJANGO_SQL_HOST=db
DJANGO_SQL_PORT=5432
EOF
$ docker-compose up
```

После этого API становится доступно на порту 1354 хоста на котором запускался docker-compose

Документация.




Эндпоинт **/api/token/**

Эндпоинт для получения JWT токена аутентификации

Метод: POST

Параметры:
```json
{
    "username": str,
    "password": str
}
```

В случае успеха:

Код ответа: 200

Параметры ответа:

```json
{
    "refresh": str,
    "access": str
}
```

Для аутентификации необходимо добавлять в хедеры запроса параметр:

```json
Authorization: Bearer {access_token}
```



Эндпоинт **/api/token/refresh/**

Эндпоинт для обновления JWT токена аутентификации

Метод: POST

Параметры:
```json
{
    "refresh": str, - токен рефреш
}
```

В случае успеха:

Код ответа: 200

Параметры ответа:

```json
{
    "refresh": str,
    "access": str
}
```



Эндпоинт **/api/poll_list/**

Служит для получения активных опросов (опросов для которых установлены даты начала и окончания и текущее время попадает в этот интервал)

Метод: GET

Параметры: Нет

В случае успеха:

Код ответа: 200

Содержимое ответа:  
```json
[
  {
    "id": int,
    "title": str,
    "description": str,
    "date_start": str (datetime),
    "date_end": str (datetime),
    "questions": [
      {
          "id": int,
          "text": str,
          "type": str
      }
    ]
  }
]
```  
В случае ошибки:

Код ответа: 404


Эндпоинт **/api/answer/**

Служит для отправки ответа на опросы

Метод: POST

Параметры: 
```json
{
    "question": int с id вопроса,
    "userid": int id пользователя,
    "value": str
}
```

В случае успеха:

Код ответа: 201

Содержимое ответа:  
```json
{
    "question": int с id вопроса,
    "userid": int id пользователя,
    "value": str
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:  
Объект с полями с ошибками, например:
```json
{
    "question": [
        "This field may not be null."
    ],
    "userid": [
        "This field may not be null."
    ],
    "value": [
        "This field may not be blank."
    ]
}
```


Эндпоинт **/api/get_answers/_userid_/**

Служит для просмотра ответов на вопросы по заданному ID пользователя

Метод: GET

Параметры: 
userid - ID пользователя

В случае успеха:

Код ответа: 200

Содержимое ответа:  
```json
[
    {
        "question": int,
        "userid": int,
        "value": str
    }
]
```  
В случае ошибки:

Код ответа: 404




Эндпоинт **/api/admin/create_poll/** *

Служит для создания опросов

Метод: POST

Параметры: 
```json
{
    "title": str,
    "description": str,
    "date_start": str, - не обязательный
    "date_end": str - не обязательный
}
```
В случае успеха:

Код ответа: 201

Содержимое ответа:  
```json
{
    "id": int,
    "title": str,
    "description": str,
    "date_start": str,
    "date_end": str,
    "questions": []
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "title": [
        "This field may not be blank."
    ],
    "description": [
        "This field may not be blank."
    ]
}
```




Эндпоинт **admin/change_poll/_pk_/** *

Служит для изменения опросов

Методы: GET, PUT, PATCH, DELETE

Параметры: 
```json
{
    "title": str,
    "description": str,
    "date_start": str, - не обязательный
    "date_end": str - не обязательный
}
```
В случае успеха:

Код ответа: 200

Содержимое ответа:  
```json
{
    "id": int,
    "title": str,
    "description": str,
    "date_start": str,
    "date_end": str,
    "questions": []
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "title": [
        "This field may not be blank."
    ],
    "description": [
        "This field may not be blank."
    ]
}
```



Эндпоинт **/api/admin/create_question/** *

Служит для создания вопросов

Метод: POST

Параметры: 
```json
{
    "text": str,
    "type": str,
    "polls": [int] - id опросов
}
```
В случае успеха:

Код ответа: 201

Содержимое ответа:  
```json
{
    "id": int,
    "text": str,
    "type": str,
    "polls": [int] - id опросов
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "text": [
        "This field may not be blank."
    ],
    "type": [
        "This field may not be null."
    ]
}
```




Эндпоинт **admin/change_question/_pk_/** *

Служит для изменения опросов

Методы: GET, PUT, PATCH, DELETE

Параметры: 
```json
{
    "id": int,
    "text": str,
    "type": str,
    "polls": [int] - не обязательный
}
```
В случае успеха:

Код ответа: 200

Содержимое ответа:  
```json
{
    "id": int,
    "text": str,
    "type": str,
    "polls": [int]
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "error": "Как минимум один из опросов заблокирован для изменений"
}
```




Эндпоинт **/api/admin/create_question_choice/** *

Служит для создания вариантов ответа

Метод: POST

Параметры: 
```json
{
    "text": str,
    "question": int - id вопроса
}
```
В случае успеха:

Код ответа: 201

Содержимое ответа:  
```json
{
    "text": str,
    "question": int
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "text": [
        "This field may not be blank."
    ],
    "question": [
        "This field may not be null."
    ]
}
```




Эндпоинт **admin/change_question_choice/_pk_/** *

Служит для изменения опросов

Методы: GET, PUT, PATCH, DELETE

Параметры: 
```json
{
    "id": 1,
    "text": str,
    "question": int - id вопроса
}
```
В случае успеха:

Код ответа: 200

Содержимое ответа:  
```json
{
    "id": 1,
    "text": str,
    "question": int
}
```  
В случае ошибки:

Код ответа: 400

Содержимое ответа:
Объект с полями с ошибками, например:
```json
{
    "text": [
        "This field may not be null."
    ],
    "question": [
        "This field may not be null."
    ]
}
```

* - Эндпоинты требующие аутентификации
    
