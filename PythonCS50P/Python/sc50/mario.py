def main():
    heigth = get_heigth()

    for i in range(heigth):
        print("#"*3)


def get_heigth(n):
    while True:
        n = int(input("Heigth: "))
        if n > 0:
            return n


main()
