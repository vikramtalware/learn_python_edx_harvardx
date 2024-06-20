import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    try:
        matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+).([0-9]+)$", ip, re.IGNORECASE)
        nums = matches.groups()
        for i in nums:
            if int(i) > 255 or int(i) < 0:
                return False
        return True
    except(AttributeError):
        return False

if __name__ == "__main__":
    main()
