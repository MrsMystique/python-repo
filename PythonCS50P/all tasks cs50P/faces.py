def main():
    str = input()
    print(convert(str))


def convert(str):
    if ":)" and ":(" in str:
        newstr = str.replace(":)", "\U0001F642").replace(":(", "\U0001F641")
        return newstr
    elif ":)" in str:
        newstr = str.replace(":)", "\U0001F642")
        return newstr
    elif ":(" in str:
        newstr = str.replace(":(", "\U0001F641")
        return newstr


main()
