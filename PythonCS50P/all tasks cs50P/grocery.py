element_list = []
counts = {}
try:
    while True:
        user_input = input()
        element_list.append(user_input)

# если вводим комбинацию ctrl+d - выводим результат
except EOFError:

    for element in sorted(element_list):
        if element in counts:
            counts[element] += 1
            # counts.update({counts[element]: counts[element] += 1})
        else:
            counts[element] = 1
    print()
    for element in counts:
        print(f'{counts[element]} {element.upper()}')
