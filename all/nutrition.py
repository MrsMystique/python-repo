
# запрошу наименование фрукта. буду игнорировать регистр
Fruit = input("Enter the fruit: ").lower()

# создам словарь, где ключи это фруукты, значения это каллории
dictFruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
# игнорировать любые данные которые не входят в словарь
# по тз не надо заводить циклл для повторного запроса. просто программа завершается

if Fruit in dictFruits:
        print(f"Calories: {dictFruits[Fruit]}")
