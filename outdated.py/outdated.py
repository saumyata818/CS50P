def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    reverse(months)

def reverse(months):
    while True:
        try:
            date = input("Date: ").strip()
            if ',' in date:
                date = date.capitalize()
                month, day, year = date.split()
                day = day.split(',')
                day = int(day[0])
                if month in months and day >= 1 and day <= 31:
                    return print(f"{year}-{months.index(month)+1:02}-{day:02}")

            elif '/' in date:
                month, day, year = date.split('/')
                year = int(year)
                day = int(day)
                month = int(month) - 1
                if month in range(len(months)) and day >= 1 and day <= 31:
                    return print(f"{year}-{month+1:02}-{day:02}")
        except ValueError:
            pass

main()
