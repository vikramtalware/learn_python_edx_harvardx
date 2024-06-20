from validator_collection import validators, checkers, errors

def main():
    email = str(input("What's your email address? "))
    print(validate(email))

def validate(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
