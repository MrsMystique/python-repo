# Вариант первый. обозначение типа в строке для решения. так как любое введенное число воспримется как текст
x = input("Введите х = ")
y = input("Введите y = ")
z = int(x) + int(y)
print(z)
# Вариант второй. не вводить доп. переменные, если ее используют один раз и принять значения, конвертировав в целые числа
# сразу в строке запроса на ввод
x = int(input("Введите х = "))
y = int(input("Введите y = "))
print(x + y)
# Вариант третий. записать код без переменных, одной строкой, если в дальнейшем они использоваться не будут
print(int(input("Введите х = ")) + int(input("Введите y = ")))

# установлю разделитель (,) -->> 1,000-->>>1,000,000
print(f"{z:,}")