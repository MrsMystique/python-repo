
import sys
from PIL import Image, ImageOps



#in sys.argv[1], имя (или путь) файла JPEG или PNG для чтения (т. е. открытия) в качестве входных данных.
# in sys.argv[2], имя (или путь) файла JPEG или PNG для записи (т. е. сохранения) в качестве вывода
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
        if not filename.endswith(".jpg"):
            print("Expected a jpg file")
            sys.exit(1)
        else:
            return filename


# Проверить достаточно ли аргументов в командной строке
if len(sys.argv) != 3:
    sys.exit("Error: Please provide exactly two command-line arguments.")

# Проверить, заканчиваются ли имена входных и выходных файлов на .jpg, .jpeg или .png (без учета регистра).
if not (sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')) and sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png'))):
    sys.exit("Error: Input and output file names must end in .jpg, .jpeg, or .png (case-insensitive).")

# Проверить, имеют ли имена входного и выходного файлов одинаковое расширение
if sys.argv[1].lower().split('.')[-1] != sys.argv[2].lower().split('.')[-1]:
    sys.exit("Error: Input and output file names must have the same extension.")

# проверка существует ли файл
# Блок пытается открыть файл в двоичном режиме ('rb') с помощью функции open().
try:
    with open(sys.argv[1], 'rb') as f:
        pass
# Если файл не найден, обрабатываем исключение FileNotFoundError.
except FileNotFoundError:
    sys.exit("Error: Input file does not exist.")

# Открыть картинку
input_image = Image.open(sys.argv[1])
# print(input_image.size)

# Измените размер и обрезать входное изображение, чтобы оно было такого же размера, как shirt.png
shirt_image = Image.open('shirt.png')

# входное изображение  -> изменяем размер функцией, принимающей 2 аргумента
# входное изображение () - которое необходимо изменить, и, в данном случае возвращаемый с помощью size
# размер накладываемой картинки
input_image = ImageOps.fit(input_image, shirt_image.size)

# Наложение файла shirt.png на входное изображение input_image с помощью paste
input_image.paste(shirt_image, (0, 0), shirt_image)


# Сохранение результата
input_image.save(sys.argv[2])