def main():
    meal_time = convert(input("What time is it? "))
    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        hour_12, period = time.split(" ")
        hours, minutes = hour_12.split(":")
        hours = float(hours)
        minutes = float(minutes)
        if period == 'p.m.' and hours != 12:
            hours = hours + 12
        elif period == 'a.m.' and hours == 12:
            hours = 0
        else:
            hours = hours
    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)

    return hours + (minutes/60)

if __name__ == "__main__":
    main()
