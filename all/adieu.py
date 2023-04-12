# `inflect` для склонения имен в правильном числе и падеже.
# создаем объект `p`, который мы будем использовать для форматирования и склонения слов.
import inflect
p = inflect.engine()
try:
    #Далее, мы создаем пустой список `names`, в который мы будем сохранять введенные с клавиатуры имена.
    names = []
    # используем вечный цикл, он прервется при нажании ctrl+d
    # внутри цикла мы принимаем имена и добавляем их в список
    while True:
        name = input(f"Введите имя: ").strip().title()
        names.append(name)


# ctrl+d вызовет исключение, и будет выполняться код внутри этого исключения
except EOFError:
    # используем наш обьект p для форматирования при обьединении списка в строку
    # удаляем финальный разделитель (это была бы запятая, установим..ничего)
    join_names = p.join(names)
    # выведем отформатированный текст
    print(f"Adieu, adieu, to {join_names} ")