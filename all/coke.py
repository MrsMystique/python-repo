

# цена 50 центов - константа
# номинал 25, 10, 5 - константы
# игнорирует все что не равно номиналу
# сколько осталось внести
# когда сумма = 50 - вывести сдачу
current_sum = 0

while current_sum < 50:
    if 50-current_sum >= 0:
        print(f"Amount Due: {50-current_sum}")
    else:
        print(f"Change Owed: {(50-current_sum)*(-1)}")
    coin_nominal = int(input("Insert Coin: "))

    if coin_nominal in [5, 10, 25]:
        current_sum += coin_nominal
print(f"Change Owed: {(50-current_sum)*(-1)}")
