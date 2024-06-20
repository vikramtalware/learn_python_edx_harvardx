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
            print("Hello")
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


# :) input of CS50 yields output of Valid
# :) input of ECTO88 yields output of Valid
# :) input of NRVOUS yields output of Valid
# :) input of CS05 yields output of Invalid
# :) input of 50 yields output of Invalid
# :) input of CS50P2 yields output of Invalid
# :) input of PI3.14 yields output of Invalid
# :) input of H yields output of Invalid
# :) input of OUTATIME yields output of Invalid
