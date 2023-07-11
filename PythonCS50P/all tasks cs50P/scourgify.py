import sys
import csv

def main():
    check_command_line_arguments()
    try:
        with open(sys.argv[2], "r") as check_file:
            check_reader = csv.reader(check_file)
            for row in check_reader:
                pass
    except FileNotFoundError:
        try:
            with open(sys.argv[2], "a") as new_file:
                header = True
                with open(sys.argv[1]) as before_csv_file:
                    before_csv_file = csv.DictReader(before_csv_file)
                    for row in before_csv_file:
                        # удаляем пробел (Hannah,Abbott)
                        name = row["name"].replace(" ", "")
                        house = row["house"]
                        # сплитуем по запятой (Hannah Abbott)
                        last, first = name.split(",")
                        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
                        if header == True:
                            writer.writeheader()
                            header = False
                        writer.writerow({"first": first, "last": last, "house": house})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def check_command_line_arguments():
    if len(sys.argv) < 3:
        sys.exit("To few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("To many command-line arguments")
    if not sys.argv[2].endswith(".csv"):
        sys.exit("The new file is not a CSV file")


if __name__ == "__main__":
    main()
