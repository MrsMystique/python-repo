menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order_list = []
cost = 0
try:

    for element in menu:
        order = input("Item: ").title()
        if order in menu:
            order_list.append(order)
            cost += float((menu[order]))
            print(f'\n${cost:.2f}')
# ПРОБЛЕМА.

# игнорируем любое несоответствие
        elif order not in menu:
            pass

# если вводим комбинацию ctrl+d - выводим результат
except EOFError:
        pass
print(f'\n${cost:.2f}')
