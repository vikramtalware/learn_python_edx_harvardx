items = []

final_list = set()

while True:
    try:
        i = input().strip().upper()
        items.append(i)
    except EOFError:
        print()
        for j in sorted(items):
            if j not in final_list:
                print(items.count(j), j)
                final_list.add(j)
        break
