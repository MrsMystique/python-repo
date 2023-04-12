# комп загадывает число. рандом
from random import *
def guesing_int(number, user_input):
    while user_input != number:
        if user_input < number:
            print("Too small!")
        elif user_input > number:
            print("Too large!")
        user_input = int(input("Guess "))
    print ("Just right!")
# генерируем число до ста


number = randint(1,100)


Level = input("Level: ")

if not Level.isnumeric():
    while Level[0] == "-":
        Level = input("Level: ")

    while Level.isalpha():
        Level = input("Level: ")
else:
    Level = int(Level)
    print(type(Level))


try:
    user_input = int(input("Guess: "))
    guesing_int(number, user_input)

except ValueError:
    try:
        user_input = int(input("Guess: "))
        guesing_int(number, user_input)
    except ValueError:
        user_input = int(input("Guess: "))
        guesing_int(number, user_input)