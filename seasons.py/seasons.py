from datetime import date, timedelta
import inflect
import sys

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    minutes = sub_date(birthday)
    print(convert_totext(minutes))

def sub_date(birth):
    #take input date
        try:
            b = date.fromisoformat(birth)
        except ValueError:
            sys.exit("Invalid date type")
        else:
            #take current date
            today = date.today()
            #substract one from another
            sub = today - b
            total = sub.total_seconds() / 60

        return round(total)

def convert_totext(num):
    return f"{p.number_to_words(num, andword='')} minutes"


if __name__ == "__main__":
    main()
