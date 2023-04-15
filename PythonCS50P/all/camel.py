# запросить наименование переменной в camelCase
# если есть буква в верхнем регистре (нужна функция определения регистра),
# то _ между словами (инсерт на индекс -1 и преобразовать в нижний текуший)
# if element.isupper()

camelCaseName = input("Input variable name in camelCase: ")
snake_case = []

for element in range(len(camelCaseName)):

    if camelCaseName[element].isupper():
        snake_case.append("_")

    snake_case.append(camelCaseName[element].lower())

print("".join(snake_case))
