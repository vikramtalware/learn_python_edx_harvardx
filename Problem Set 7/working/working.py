import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r"^([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM) to ([0-1]?[0-9])(\:[0-5][0-9])? (AM|PM)", s):
        from_time  = hour_24(int(time.group(1)), time.group(2), time.group(3))
        end_time = hour_24(int(time.group(4)), time.group(5), time.group(6))
        return f"{from_time} to {end_time}"
    else:
        raise ValueError

def hour_24(hour, min, period):
    if hour == 12:
        if period == 'AM':
            hour = 0
        else:
            hour = 12
    elif period == 'PM':
        if hour != 12:
            hour += 12

    if min == None:
        min = ":00"

    return f"{hour:02d}{min}"

if __name__ == "__main__":
    main()
