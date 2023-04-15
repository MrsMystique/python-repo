answer = input("What is your name, beautifull lady: ")

# первый способ совмещения аргумента и текста. Конкатенация
# print ("Hello, "+ answer +" ,i love you!")
# второй способ совмещения аргумента и текста. через разделение аргументов запятой
# print ("Hello,", answer,",i love you!")
# третий способ совмещения аргумента и текста. Интерполирование
# print (f"Hello, {answer} ,i love you!")

""" В технической документации к функции print() разработчики пишут такую характеристику
print (*objects, sep=' ', end = '\n', file = sys.stdout, flush = false)
sep = разделитель между аргументами, end = как (чем) заканчивается исполнение функции. 
в данном случае по окончании строки будет переход на новую строку. 
Эти параменты можно менять"""

# изменение значения функции, которые заложены в нее по умолчанию (например окончание строки)
# print("hello, ",end = "")
# print(answer) 

# обработка исключений со строками

# удалить случайно введенные пробелы(если это нужно, например при введении каких то данных)
# answer = answer.strip()

# заменить lowercase на uppercase в начале слова и если я написала oLGa - поставит в нужный case
# answer = answer.capitalize()

# каждое слово будет написано с заглавной буквы  olga zorina - Olga Zorina
# answer = answer.title()

# для того чтобы связать несколько вышестоящих функций в одну строку кода я могу сделать следующее
answer = answer.title().strip()
# print("hello,", answer)

# все вышестоящие функции можно применить сразу на строку ввода
# answer = input ("What is your name, beautifull lady: ").strip().title()

# МЕТОД СПЛИТ - разделение срок (What is your name, beautifull lady: olga zoryna - Hello, Olga)
firstName, lastName = answer.split(" ")
print("hello,", firstName)
