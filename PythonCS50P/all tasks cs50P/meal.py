
# запрашивает у пользователя время
# Предположим, что пользовательский ввод будет отформатирован в 24-часовом формате как #:##или ##:##
# breakfast time с 7:00 до 8:00, lunch time с 12:00 до 13:00, или dinner time 18:00 до 19:00
# будь то 7:00, 7:01, 7:59, 8:00 или любое другое время между ними, пора завтракать (between)
# Если не время для еды, вообще ничего не выводите
# добавьте поддержку 12-часового времени, что позволит пользователю вводить время и в этих форматах:
# convert есть функция (которую можно вызвать main),
# которая преобразует time а str в 24-часовом формате в
# соответствующее количество часов в виде float
# например, учитывая time "7:30"(т. е. 7 часов 30 минут),
# convert должен вернуться 7.5(т. е. 7,5 часов)

def main():
    time = convert(input("What time is it? ").strip())

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

    else:
        print()


def convert(time):

    if time.endswith("a.m"):
        global hours, minutes
        hours, minutes = time.replace("a.m", "").split(":")
        hours = int(hours)
        minutes = int(minutes)
        time = round((hours + (minutes/60)), 2)

    elif time.endswith("p.m"):
        hours, minutes = time.replace("p.m", "").split(":")
        hours = int(hours)
        minutes = int(minutes)
        time = round((hours + (minutes/60)), 2)

        if time <= 11:
            time = round((time + 12), 2)

    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        time = round((hours + (minutes/60)), 2)

    return time


if __name__ == "__main__":
    main()
