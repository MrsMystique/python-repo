import pyttsx3

# создаем объект для озвучивания текста
engine = pyttsx3.init()

# получаем список всех доступных голосов
voices = engine.getProperty('voices')

# выбираем голос на русском языке
for voice in voices:
    if voice.languages[0] == 'ru':
        engine.setProperty('voice', voice.id)
        break