def main():
    greeting = input("Please, say hello to Newman : ").strip()
    print(value(greeting))

def value(greeting):

    if greeting == "Hello" or "hello" in greeting.lower():
        return 0
    elif greeting[0].lower() == "h":
        return 20
    else:
        return 100

if __name__=="__main__":
    main()