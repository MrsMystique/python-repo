
def get_correct_input(user_input):
    try:
        x, y = user_input.split("/")
        if int(x) <= int(y) and int(y) != 0:
            percentage = int(round(int(x) / int(y) * 100))
            return percentage
    except (ZeroDivisionError, ValueError):
            pass



print(get_correct_input("1/100"))
