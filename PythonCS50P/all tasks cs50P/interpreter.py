# запрашивает у пользователя арифметическое выражение
# Предположим, что пользовательский ввод будет отформатирован как x y z с
# одним пробелом между x и y и одним пробелом между y и z, где: x- int/
# y знак  +, -, * или /, z int
# Предположим, что если y это /, то z не будет 0.
# вычисляет и выводит результат в виде значения с плавающей запятой,
# отформатированного до одного десятичного знака {,f1}
expression = input("Enter math expression: ").lower().strip()

x, y, z = expression.split()

if y == "+":
    math = float(int(x) + int(z))
elif y == "-":
    math = float(int(x) - int(z))
elif y == "*":
    math = float(int(x) * int(z))
elif y == "/":
    if z != 0:
        math = float(int(x) / int(z))
    else:
        print("ZeroDivisionError: division by zero")
print(f"{math:.1f}")
