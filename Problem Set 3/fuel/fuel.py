def main():
    x = fuel_capacity()
    print(x)

def fuel_capacity():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            if int(x) <= int(y):
                if int(x)/int(y) <= 0.01:
                    return("E")
                elif int(x)/int(y) >= 0.99:
                    return("F")
                else:
                    return (str(round(int(x)/int(y) * 100))+'%')
        except (ValueError, ZeroDivisionError):
            pass
main()
