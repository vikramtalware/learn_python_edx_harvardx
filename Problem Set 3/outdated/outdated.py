months =   ["January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]

while True:
    try:
        date = input("Date: ")

        if "," in date:
            m, d, y = date.lstrip().rstrip().replace(",","").split(" ")
            if m in months and int(d) <= 31:
                m = int(months.index(m))+1
                print(f"{int(y)}-{m:02}-{int(d):02}")
                break
        elif "/" in date:
            m, d, y = date.lstrip().rstrip().split("/")
            if int(m) <= 12 and int(d) <= 31:
                print(f"{int(y)}-{int(m):02}-{int(d):02}")
                break
    except:
        pass
