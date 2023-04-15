import sys
import csv
from tabulate import tabulate

def main():
    filename = get_csv_filename_from_args(sys.argv)
    print(return_grid_from_csv(filename))

# получаем корректное имя файла и нужное количество аргументов ком. стр
def get_csv_filename_from_args(argv):
    if len(argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        filename = argv[1].lower().lstrip()
        if not filename.endswith(".csv"):
            print("Expected a CSV file")
            sys.exit(1)
        else:
            return filename

# читаем csv и возвращаем строки данных
def return_grid_from_csv(filename):
    list_if_all_rows = []
    with open(filename, "r", newline = "") as file:
        reader = csv.reader(file, delimiter =',')
        for row in reader:
            list_if_all_rows.append(row)
    if not list_if_all_rows:
        return "CSV file is empty"
    else:
        # удаляем первую строку из списка и сохраняем ее в table_headers
        table_headers = list_if_all_rows.pop(0)
        # передаем table_headers в качестве заголовков таблицы
        return tabulate(list_if_all_rows, headers = table_headers, tablefmt = "grid")


if __name__ == "__main__":
    main()