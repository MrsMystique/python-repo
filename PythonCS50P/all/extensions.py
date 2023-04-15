# запросить имя файла с расширением
# если файл имеет определенной расширение, распечатать определенную инфу
filename = input("Input filename with extention: ").lower().strip()
# будем первращать все в л кейс, убирать пробелы вначале и в конце строки.
# и используем функцию endswith(),
# для того чтобы только при окончании строки на эти символы что то выводилось
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".jpg") and "zipper" not in filename and "happy" not in filename:
    print("image/jpg")
elif filename.endswith(".jpeg") or "zipper" in filename or "happy" in filename:
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".zip"):
    print("application/zip")
elif filename.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
