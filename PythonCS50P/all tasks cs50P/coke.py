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
