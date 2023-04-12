import sys
import requests
import json

# Получаем количество биткойнов, которые пользователь хочет купить
try:
    bitcoins = float(sys.argv[1])
except (IndexError, ValueError):
    print("Command-line argument is not a number")
    sys.exit(1)

# Запрашиваем данные от API CoinDesk
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException:
    print("Не удалось получить данные от API CoinDesk.")
    sys.exit(1)

# Получаем текущую цену биткойна из ответа JSON
data = json.loads(response.text)
price = data["bpi"]["USD"]["rate_float"]

# Вычисляем стоимость покупки биткойнов
cost = bitcoins * (price)

# Выводим результат с точностью до четырех знаков после запятой
print(f"${cost:,.4f}")







