import pyttsx3
import PyPDF2

# имя PDF файла
file_name = "first head of python.pdf"

# номер страницы с которой начнется чтение
start_page = 2

# инициализация движка TTS
engine = pyttsx3.init()

# установка голоса с русской локализацией
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# открытие PDF файла
with open(file_name, 'rb') as pdf_file:
    # чтение PDF файла
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # ограничение чтения до указанной страницы
    pdf_reader.numPages = start_page + 1

    # чтение каждой страницы
    for i in range(start_page, pdf_reader.numPages):
        # извлечение текста страницы
        page = pdf_reader.getPage(i)
        text = page.extractText()

        # произношение текста
        engine.say(text)

# ожидание завершения произношения
engine.runAndWait()