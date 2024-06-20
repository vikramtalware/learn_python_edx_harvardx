from datetime import date
import inflect
import sys

def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
        result = age_min(birth_date, date.today())
        p = inflect.engine()
        print(f"{p.number_to_words(result, andword='').capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid date")

def age_min(birth_date, today):
    age_num = (today - birth_date).days * 24 * 60
    return age_num

if __name__ == "__main__":
    main()
