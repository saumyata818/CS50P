import inflect
from typing import Optional
from datetime import datetime, date, timedelta


def days_diff(start: date, end: date) -> int:
    return int((end - start) / timedelta(minutes=1))


def validate_date(date: str) -> Optional[date|bool]:
    try:
        return datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return False


def number_to_word(days: int) -> str:
    inf = inflect.engine()
    return inf.number_to_words(days, andword="")


def main() -> None:
    today = date.today()
    if date_of_birth := validate_date(input("Date of Birth: ")):
        print(f"{number_to_word(days_diff(date_of_birth, today)).capitalize()} minutes")
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()

