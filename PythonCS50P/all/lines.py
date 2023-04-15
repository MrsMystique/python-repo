import sys

def main():
    print(search_file_in_dir())

def search_file_in_dir():
    try:
        filename = get_correct_filename(sys.argv)
        return read_file(filename)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        code_lines = 0
        for line in lines:
            if line.strip() and not line.strip().startswith('#'):
                code_lines += 1
    return code_lines


def get_correct_filename(argv):
    if len(argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        filename = argv[1].lower().lstrip()
        if not filename.endswith(".py"):
            print("Not a python file")
            sys.exit(1)
        else:
            return filename

if __name__ == "__main__":
    main()
