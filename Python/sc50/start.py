
answer = input("what is your name?  ") # присваивание переменной значения (ответа на вопрос )
print("hello, " + answer + "!") # конкатенация
print(f"hello, {answer}!") # интерполяция

x = 5
y = 2
if x < y:   
    print("Горила")
else:
    print("Обезяна")