import inflect

p = inflect.engine()

names = []

while True:
    try:
        s = str(input("Name: "))
        names.append(s)
    except EOFError:
        print()
        print("Adieu, adieu, to "+ p.join(names))
        break

