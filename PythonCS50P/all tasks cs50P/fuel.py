def main():
    percentfuel = convert(input("введите дробь в формате x/y: ").strip().lower())
    print(gauge(percentfuel))
# должна получить корректную дробь

def convert(user_input):
    try:
        x, y = user_input.split("/")
        if int(x) <= int(y) and int(y) != 0:
            percentfuel = int(round(int(x) / int(y) * 100))
            return percentfuel
    except (ValueError, ZeroDivisionError):
        pass



def gauge(percentfuel):
    # если процент = 99 - бак полон
    if percentfuel in [99, 100]:
        return ("F")
    # бак 1 - бак пуст
    elif percentfuel in [0, 1]:
        return ("E")
    else:
        return f"{percentfuel}%"


if __name__ == "__main__":
    main()

