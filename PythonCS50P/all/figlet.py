from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if len(sys.argv) > 1:
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")


user_input = input("Enter text: ")


if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))
    print("Random Font:\n" + figlet.renderText(user_input))# 0 аргументов командной строки

elif len(sys.argv) == 3:
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(user_input))
else:
    sys.exit("Invalid usage")


