from datetime import datetime
from dateutil.parser import parse


try:
    date_string = input("Date: ").strip()
    date = datetime.strptime(date_string, "%B %d, %Y")
    date = parse(date_string, dayfirst=False)
    formatted_date = date.strftime("%Y-%m-%d")
    print(formatted_date)

except ValueError:
    try:
        date = datetime.strptime(date_string, "%m/%d/%Y")
        date = parse(date_string, dayfirst=False)
        formatted_date = date.strftime("%Y-%m-%d")
        print(formatted_date)

    except ValueError:
        date_string = input("Date: ").strip()
        try:
            date = datetime.strptime(date_string, "%B %d, %Y")
            date = parse(date_string, dayfirst=False)
            formatted_date = date.strftime("%Y-%m-%d")
            print(formatted_date)
        except ValueError:
            try:
                date = datetime.strptime(date_string, "%m/%d/%Y")
                date = parse(date_string, dayfirst=False)
                formatted_date = date.strftime("%Y-%m-%d")
                print(formatted_date)
            except ValueError:
                exit()

