I. Введение: 

Библиотека requests – это библиотека Python для работы с HTTP-запросами. Requests позволяет легко отправлять HTTP/1.1 запросы и получать ответы, представленные в виде объектов Python.

II. Установка библиотеки requests: 

Чтобы начать работать с библиотекой requests, ее нужно установить. Это можно сделать с помощью команды pip. 

```
pip install requests
```

III. Основы работы с библиотекой requests: 

1. GET-запрос: 

GET-запрос используется для получения данных с сервера. 

Пример:

```
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.status_code)
print(response.json())
```

2. POST-запрос: 

POST-запрос используется для отправки данных на сервер. 

Пример:

```
import requests

data = {'name': 'John', 'email': 'john@example.com'}
response = requests.post('https://jsonplaceholder.typicode.com/users', data=data)

print(response.status_code)
print(response.json())
```

3. PUT-запрос: 

PUT-запрос используется для обновления существующих данных на сервере. 

Пример: 

```
import requests

data = {'name': 'John', 'email': 'john@example.com'}
response = requests.put('https://jsonplaceholder.typicode.com/users/1', data=data)

print(response.status_code)
print(response.json())
```

4. DELETE-запрос: 

DELETE-запрос используется для удаления данных с сервера. 

Пример: 

```
import requests

response = requests.delete('https://jsonplaceholder.typicode.com/users/1')

print(response.status_code)
print(response.json())
```

IV. Использование параметров запроса: 

Для добавления параметров в запрос, нужно использовать параметр params. 

Пример: 

```
import requests

params = {'q': 'python'}
response = requests.get('https://google.com/search', params=params)

print(response.url)
print(response.status_code)
```

V. Заголовки запросов: 

Для добавления заголовков в запрос, нужно использовать параметр headers. 

Пример: 

```
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://google.com', headers=headers)

print(response.status_code)
```

VI. Обработка ошибок: 

Чтобы обработать ошибку запроса, можно использовать статус-коды. 

Пример: 

```
import requests

response = requests.get('https://google.com/404')

if response.status_code == 404:
    print('Page not found')
else:
    print(response.status_code)
```

VII. Загрузка файлов: 

Чтобы загрузить файл на сервер, нужно использовать параметр files. 

Пример: 

```
import requests

files = {'file': open('/path/to/file.txt', 'rb')}
response = requests.post('https://jsonplaceholder.typicode.com/users', files=files)

print(response.status_code)
print(response.json())
```

VIII. Сессии: 

Сессии позволяют сохранять параметры авторизации и другие настройки между запросами. 

Пример: 

```
import requests

session = requests.Session()

session.auth = ('user', 'password')
session.headers.update({'x-test': 'true'})

response = session.get('https://jsonplaceholder.typicode.com/users/1')

print(response.status_code)
print(response.json())
```

IX. Заключение: 

Библиотека requests позволяет легко работать с HTTP-запросами. В этом конспекте были рассмотрены основные методы работы с библиотекой, а также способы настройки запросов.