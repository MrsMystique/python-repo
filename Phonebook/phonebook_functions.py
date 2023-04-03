import csv
import pandas as pd
from reportlab.pdfgen import canvas
import qrcode


# Функция выбора опций
# Основная функция для работы с телефонным справочником
def choose_option():
    # Открыть файл с телефонным справочником
    with open('phonebook.csv', 'a+') as file:
        # Предложить пользователю выбрать действие
        while True:
            print('Выберите действие:')
            print('1. Добавить контакт')
            print('2. Удалить контакт')
            print('3. Изменить контакт')
            print('4. Найти контакт')
            print('5. Экспорт карточки контакта')
            print('6. Экспорт всего содержимого справочника')
            print('7. Выйти из программы')
            choice = input('Введите номер действия: ')

            # Выполнить выбранное действие
            if choice == '1':
                add_contact()
            elif choice == '2':
                delete_contact()
            elif choice == '3':
                edit_contact()
            elif choice == '4':
                search_contacts()
            elif choice == '5':
                export_contact_found_to_pdf()
            elif choice == '6':
                export_all_contacts_to_pdf()
            elif choice == '7':
                break
            else:
                print('Нет такой опции')


# Функция для добавления контакта
def add_contact():
    with open("phonebook.csv", "a") as file:
        columnnames = ["Name", "Lastname", "Phone", "Email", "Telegram", "Organization name"]
        name = input("Введите имя: ").strip().title()
        lastname = input("Введите Фамилию: ").strip().title()
        phone_number = input("Введите номер телефона: ").strip()
        email = input("Введите email: ")
        telegram_id = input("Введите telegram_id: ").strip()
        Organization = input("Введите имя организации: ").strip().title()
        writer = csv.DictWriter(file, columnnames)
        writer.writerow({"Name": name, "Lastname": lastname, "Phone": phone_number, "Email": email, "Telegram": telegram_id,"Organization name": Organization})
    print('Контакт добавлен!')


# Функция для поиска контакта (визитка)
def search_contacts():
    # считываем данные из CSV файла в DataFrame
    df = pd.read_csv('phonebook.csv')
    # запрашиваем у пользователя строку для поиска
    search_term = input("Поиск контакта: ")
    # фильтруем DataFrame по запросу пользователя
    filtered_df = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().str.cat(sep=' '), axis=1)]
    # выводим найденные данные в форме визитной карточки
    for index, row in filtered_df.iterrows():
        print('===============================')
        print('Name:', row['Name'])
        print('Lastname:', row['Lastname'])
        print('Phone:', row['Phone'])
        print("Email:", row["Email"])
        print("Telegram:", row["Telegram"])
        print("Organization name:", row["Organization name"])
        print('===============================')


# требует pip install qrcode
# требует pip install reportlab
def export_contact_found_to_pdf():
    # считываем данные из CSV файла в DataFrame
    df = pd.read_csv('phonebook.csv')

    # запрашиваем у пользователя строку для поиска
    search_term = input("Search: ")

    # фильтруем DataFrame по запросу пользователя
    filtered_df = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().str.cat(sep=' '), axis=1)]

    # создаем PDF-файл
    pdf_file = canvas.Canvas("Visit Card.pdf")
    y = 750  # начальная координата для вывода информации

    # выводим найденные данные в форме визитной карточки и добавляем QR-код с телеграм ай ди
    for index, row in filtered_df.iterrows():
        pdf_file.drawString(100, y, 'Name: ' + str(row['Name']))
        pdf_file.drawString(100, y-20, 'Lastname: ' + str(row['Lastname']))
        pdf_file.drawString(100, y-40, 'Phone: ' + str(row['Phone']))
        pdf_file.drawString(100, y-60, 'Email: ' + str(row['Email']))
        pdf_file.drawString(100, y-80, 'Telegram: ' + str(row['Telegram']))
        pdf_file.drawString(100, y-100, 'Organization name: ' + str(row['Organization name']))
# генерируем QR-код с телеграммом
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data('telegram.me/' + row['Telegram'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qrcode.png')

        # добавляем QR-код в PDF
        pdf_file.drawImage('qrcode.png', 400, y-60, width=100, height=100)

        y -= 150  # смещаем координату по y для следующего контакта

    pdf_file.save()


# требует pip install qrcode
# требует pip install reportlab
# требует pip install qrcode
# требует pip install reportlab
def export_all_contacts_to_pdf():
    # считываем данные из CSV файла в DataFrame
    df = pd.read_csv('phonebook.csv')

    # создаем PDF-файл
    pdf_file = canvas.Canvas("all_contacts.pdf")
    y = 750  # начальная координата для вывода информации

    # выводим данные в форме визитной карточки и добавляем QR-код с телеграмм
    for index, row in df.iterrows():
        pdf_file.drawString(100, y, 'Name: ' + str(row['Name']))
        pdf_file.drawString(100, y-20, 'Lastname: ' + str(row['Lastname']))
        pdf_file.drawString(100, y-40, 'Phone: ' + str(row['Phone']))
        pdf_file.drawString(100, y-60, 'Email: ' + str(row['Email']))
        pdf_file.drawString(100, y-80, 'Telegram: ' + str(row['Telegram']))
        pdf_file.drawString(100, y-100, 'Organization name: ' + str(row['Organization name']))
        y -= 150  # смещаем координату по y для следующего контакта

    pdf_file.save()


# Функция удаления контакта
def delete_contact():
    search_term = input("Поиск контакта: ")
    search = []
    with open("phonebook.csv", "r", newline ='') as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            search.append({"Name": row["Name"], "Lastname": row["Lastname"], "Phone": row["Phone"], "Email": row["Email"], "Telegram": row["Telegram"], "Organization name": row["Organization name"]})
        matching_contacts = []
        for person in search:
            if any(search_term.lower() in value.lower() for value in person.values()):
                matching_contacts.append(person)
        if len(matching_contacts) == 0:
            print("Контактов с такими данными не найдено.")
            return
        print("Совпадающие контакты:")
        for i, contact in enumerate(matching_contacts):
            print(f"{i}: {contact['Name']} {contact['Lastname']}, {contact['Phone']}, {contact['Email']}, {contact['Telegram']}, {contact['Organization name']}")
        index = int(input("Введите порядковый номер контакта для удаления: "))
        fieldnames = ["Name", "Lastname", "Phone", "Email", "Telegram", "Organization name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for person in search:
            if person not in matching_contacts or person != matching_contacts[index]:
                writer.writerow(person)
    print("Контакт удален.")

# Функция изменения контакта
def edit_contact():
    search_term = input("Поиск контакта: ")
    search_result = []
    with open("phonebook.csv", "r", newline ='') as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            search_result.append({"Name": row["Name"], "Lastname": row["Lastname"], "Phone": row["Phone"], "Email": row["Email"], "Telegram": row["Telegram"], "Organization name": row["Organization name"]})
        matching_contacts = []
        for contact in search_result:
            if any(search_term.lower() in value.lower() for value in contact.values()):
                matching_contacts.append(contact)
        if len(matching_contacts) == 0:
            print("Контактов с такими данными не найдено.")
            return
        print("Совпадающие контакты:")
        for i, contact in enumerate(matching_contacts):
            print(f"{i}: {contact['Name']} {contact['Lastname']}, {contact['Phone']}, {contact['Email']}, {contact['Telegram']}, {contact['Organization name']}")
        index = int(input("Введите порядковый номер контакта для изменения: "))
        print(f"{matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}")
        print(f"Изменение {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}...")
        print("Выберите поле, которое вы хотите отредактировать:")
        print("1. Номер телефона")
        print("2. Email")
        print("3. Telegram ID")
        print("4. Название организации")
        field_choice = input("Введите номер поля: ")
        if field_choice == "1":
            new_phone_number = input(f"Введите новый номер для {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}: ").strip()
            matching_contacts[index]["Phone"] = new_phone_number
        elif field_choice == "2":
            new_email = input(f"Введите новый email для {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}: ").strip()
            matching_contacts[index]["Email"] = new_email
        elif field_choice == "3":
            new_telegram_id = input(f"Введите новый telegram id для {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}: ").strip()
            matching_contacts[index]["Telegram"] = new_telegram_id
        elif field_choice == "4":
            new_organization = input(f"Введите наименование организации {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']}: ").strip()
            matching_contacts[index]["Organization name"] = new_organization
        else:
            print("Некорректный выбор.")
            return
        with open("phonebook.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Lastname", "Phone", "Email", "Telegram", "Organization name"])
            writer.writeheader()
            for contact in search_result:
                if contact in matching_contacts:
                    writer.writerow(contact)
                else:
                    writer.writerow(contact)
            print(f"Контакт {matching_contacts[index]['Name']} {matching_contacts[index]['Lastname']} обновлен.")


choose_option()
