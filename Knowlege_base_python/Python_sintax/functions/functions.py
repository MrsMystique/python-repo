# все строки кода которые будут с отступом под именем функции - будут считаться функцией
def sum():
    x = input("Введите х = ")
    y = input("Введите y = ")
    z = int(x) + int(y)
    print (z)

# параметр выбранный в качестве аргумента можно брать из головы, чтобы понятно было для чего использовать функцию
# в данном случае to выбран для того чтобы было ясно что нужно сказать привет TO OLGA
#def hello(to):
#    print ("Hello,",to)

# вместо параметра функции нужно положить переменную. создадим ее и примем в нее значение от пользователя
# name = input("Please enter your name: ").title().strip()
# вызовем функцию и положим туда введенное значение, присвоенное переменной name
#hello(name)

# функция со значением по умолчанию: hello() - вызов без аргументов вызовет значение по умолчанию hello, world
def hello(to="world"):
    print("hello,", to)

hello()
name = input("Please enter your name: ").title().strip()
hello(name)

# вернула значение
def main():
    x = int(input("Enter x: "))
    print("x квадрат равен:", square(x))

def square(n):
    return n*n
main()