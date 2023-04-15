from random import *


def main():
    try:
        level = get_level()
        min, max = different_levels(level)
        score = generate_integer(min, max)
        print(score)
    except ValueError:
        raise ValueError("Not a number")


# Запрашивает у пользователя уровень, Если пользователь не вводит 1, 2 или 3, программа должна снова запросить.
def get_level():
    try:
        level = int(input("Level: "))
        if level not in [1, 2, 3]:
            print("Error: level must be 1, 2 or 3")
            return get_level()
        return level
    except ValueError:
        print("Error: level must be a number")
        return get_level()


def different_levels(level):
    min = 0
    max = 0
    if level == 1:
        min = 0
        max = 10
    elif level == 2:
        min = 10
        max = 100
    else:
        min = 100
        max = 1000
    return min, max


def generate_integer(min, max):
    score = 0
    try:
        for _ in range(9):
            problem = randint(min, max), randint(min, max)
            print(f"{problem[0]} + {problem[1]} =", end=" ")
            answer = input()

            if not answer.isdigit() or int(answer) != problem[0] + problem[1]:
                for attemp in range(2):

                    print("EEE")
                    print(f"{problem[0]} + {problem[1]} =", end=" ")
                    answer = input()

                    if attemp == 1:
                        print(problem[0] + problem[1])
                        break
                    elif answer.isalpha():
                        continue
                    elif int(answer) == problem[0] + problem[1]:
                        score = score + 1
                        break
                    elif attemp == 1:
                        print(problem[0] + problem[1])

            score = score + 1
    except ValueError:
        pass
    return score


if __name__ == "__main__":
    main()
