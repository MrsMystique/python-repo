# принять от пользователя ответ на вопрос в л кейсе
# (заюзан многострочный ввод. так как строка слишком длинная)
answer = input("""What is the answer to the Great Question of Life,
               the Universe and Everything? """).lower()
# сделать ветвление
if "42" in answer or "forty-two" in answer or "forty two" in answer:
    print("Yes")
else:
    print("No")
