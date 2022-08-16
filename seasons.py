import datetime
import sys
import inflect
p = inflect.engine()


def main():
    # Prompt user for date of birth in YYYY-MM-DD
    birthdate = input("Date of Birth: ")

    # Exit via sys.exit if the user does not input a date in YYYY-MM-DD format
    try:
        validate_date(birthdate)
    except ValueError:
        sys.exit("Invalid date")

    print(format_date(birthdate), "minutes")


def validate_date(birthdate):
    if not datetime.datetime.strptime(birthdate, "%Y-%m-%d"):
        raise ValueError


def format_date(birthdate):
        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        today = datetime.date.today()
        result = today - birthdate
        amount_days = int(result.days)
        minutes = p.number_to_words(amount_days * 1440, andword="").capitalize()
        return minutes


if __name__ == "__main__":
    main()