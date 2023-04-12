def main():
    string = input("Input text: ")
    print(shorten(string))

def shorten(string):
    new_string = []
    for letter in string:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_string.append(letter)
    return (''.join(new_string))

if __name__ == "__main__":
    main()

