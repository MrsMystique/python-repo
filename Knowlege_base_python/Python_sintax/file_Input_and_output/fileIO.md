# конспект  с кейсам по работе с данными файлов csv на python

---


Конспект по работе с данными файлов csv на Python:

1. Импортирование модуля csv:

import csv

2. Открытие файла csv:

with open('file.csv') as csvfile:

3. Создание объекта-читателя:

reader = csv.reader(csvfile)

4. Чтение данных из файла:

for row in reader:
   print(row)

5. Получение списка значений из ячейки:

data = row[0]

6. Запись данных в файл:

with open('file.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Column 1', 'Column 2', 'Column 3'])
    writer.writerow(['Value 1', 'Value 2', 'Value 3'])

7. Использование разделителей:

with open('file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['Column 1', 'Column 2', 'Column 3'])
    writer.writerow(['Value 1', 'Value 2', 'Value 3'])

8. Использование словаря для записи данных:

with open('file.csv', 'w', newline='') as csvfile:
    fieldnames = ['Column 1', 'Column 2', 'Column 3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Column 1': 'Value 1', 'Column 2': 'Value 2', 'Column 3': 'Value 3'})

9. Чтение данных из файла с помощью pandas:

import pandas as pd

df = pd.read_csv('file.csv')
print(df)

10. Запись данных в файл с помощью pandas:

import pandas as pd

df = pd.DataFrame({'Column 1': ['Value 1'], 'Column 2': ['Value 2'], 'Column 3': ['Value 3']})
df.to_csv('file.csv', index=False)

# Кейсы работы с данными файлов csv на Python:

1. Вычисление среднего значения числовых данных в файле csv

import csv

with open('file.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(float(row[0]))
    average = sum(data) / len(data)
    print("Average is:", average)

2. Фильтрация данных в файле csv по условию

import csv

with open('file.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        if float(row[0]) > 5:
            data.append(row)
    print("Filtered data is:", data)

3. Объединение данных из двух файлов csv

import csv

with open('file1.csv') as csvfile1:
    reader1 = csv.reader(csvfile1)
    with open('file2.csv') as csvfile2:
        reader2 = csv.reader(csvfile2)
        data = []
        for row1, row2 in zip(reader1, reader2):
            data.append(row1 + row2)
        print("Merged data is:", data)

4. Вычисление суммы данных из нескольких файлов csv

import csv

data = []
for i in range(1, 4):
    with open(f'file{i}.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(float(row[0]))
sum_data = sum(data)
print("Sum is:", sum_data)

5. Запись данных в файл csv с использованием словаря

import csv

data = {'Column 1': ['Value 1'], 'Column 2': ['Value 2'], 'Column 3': ['Value 3']}
with open('file.csv', 'w', newline='') as csvfile:
    fieldnames = ['Column 1', 'Column 2', 'Column 3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)

---