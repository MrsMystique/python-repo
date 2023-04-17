## конспект на тему dictionarys по книге byte of python с кодом




Dictionarys в Python

- Dictionarys (словари) в Python - это изменяемые объекты, которые используются для хранения данных в формате ключ-значение.
- Ключи должны быть уникальными, а значения могут быть любыми типами данных - числами, строками, списками, другими словарями и т.д.
- Создание пустого словаря:

```
my_dict = {}
```

- Создание словаря с определенными ключами и значениями:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

- Доступ к значениям словаря осуществляется по ключу:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict['key1']) # выведет 'value1'
```

- Добавление новых значений в словарь:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict['key4'] = 'value4'
print(my_dict) # выведет {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```

- Итерирование по словарю:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key in my_dict:
    print(key, my_dict[key])
```

- Получение всех ключей и значений словаря:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
keys = my_dict.keys()
values = my_dict.values()
print(keys) # выведет dict_keys(['key1', 'key2', 'key3'])
print(values) # выведет dict_values(['value1', 'value2', 'value3'])
```

- Проверка наличия ключа в словаре:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
if 'key1' in my_dict:
    print('key1 exists')
```

- Удаление элемента из словаря:

```
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del my_dict['key1']
print(my_dict) # выведет {'key2': 'value2', 'key3': 'value3'}
```

- Комбинирование двух словарей:

```
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key3': 'value3', 'key4': 'value4'}
dict1.update(dict2)
print(dict1) # выведет {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```


 list compression на python



1. Задание списка: создайте список, который Вы хотите сжать с помощью лист-компрессии.

2. Синтаксис лист-компрессии: используйте следующий синтаксис для лист-компрессии: [выражение for элемент in список if условие], где:
- выражение - это операция (или последовательность операций), которая будет применена к каждому элементу списка.
- элемент - это текущий элемент списка.
- список - это список, который нужно сжать.
- условие - это дополнительное условие, которое выбирает элементы списка.

3. Примеры выражений:
- удвоить все элементы списка: [element*2 for element in original_list]
- отфильтровать все четные числа: [element for element in original_list if element % 2 == 0]
- объединить строки в одну: [letter for word in original_list for letter in word]

4. Применение лист-компрессии: примените синтаксис лист-компрессии к Вашему списку.

5. Результат: результатом лист-компрессии будет новый сжатый список, содержащий результаты выражения.

6. Использование результата: используйте новый сжатый список так, как Вам нужно в конечной программе.

Например, получив список имен файлов, можно легко сжать его с помощью лист-компрессии и вернуть только те имена файлов, которые заканчиваются на расширение ".txt":

original_list = ["file1.txt", "file2.png", "file3.doc", "file4.txt"]
filtered_list = [file_name for file_name in original_list if file_name.endswith(".txt")]
print(filtered_list)
# Output: ["file1.txt", "file4.txt"]