import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if output := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w*)"', s):
        return f"https://youtu.be/{output.group(1)}"

if __name__ == "__main__":
    main()
