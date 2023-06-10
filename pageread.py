import pyttsx3
from pathlib import Path
from PyPDF2 import PdfReader

# создаем объект для чтения PDF-файла
pdf_file = Path('first head of python.pdf')
pdf_reader = PdfReader(str(pdf_file))

# получаем количество страниц в документе
num_pages = len(pdf_reader.pages)

# создаем объект для озвучивания текста
engine = pyttsx3.init()

# устанавливаем параметры озвучивания
engine.setProperty('rate', 150) # скорость озвучивания
engine.setProperty('volume', 1.0) # громкость озвучивания

# выбираем голос для озвучивания (в данном случае, русский язык)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # выбор первого голоса

# задаем номер страницы, с которой нужно начать чтение
start_page = 3

# проходим по всем страницам документа, начиная с заданной страницы, и озвучиваем их содержимое
for page_num in range(start_page - 1, num_pages):
    # получаем текст на текущей странице
    page = pdf_reader.pages[page_num]
    text = page.text

    # озвучиваем текст
    engine.say(text)

# сохраняем изменения
engine.runAndWait()