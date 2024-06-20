def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check length of the string
    if len(s) > 6 or len(s) < 2:
        return False
    elif len(s) == 2 and s[0:2].isalpha():
        return True

    # check if first two characters are letters
    if s[0:2].isalpha():
        # check if remaining characters are alphanumeric and last two characters are digits, because letters can't be the last two characters (Ex. CS50P2).
        # also checks if the remaining characters do not have periods, spaces, or punctuation.
        if s[2:].isalnum() and s[-2:].isdigit():
            # check if numbers are starting from 0
            for i in range(len(s)):
                if s[i].isdigit():
                     if s[i].startswith("0"):
                          return False
                     else:
                          return True
        # check if whole string is just letter
        elif s[2:].isalpha():
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
