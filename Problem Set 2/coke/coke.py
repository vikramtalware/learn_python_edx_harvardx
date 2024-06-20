amt = 50
coins = [5, 10, 25]

print("Amount Due:", amt)

while (amt > 0):
    due = int(input("Insert Coin: "))
    if due in coins:
        amt -= due
        if amt <= 0:
            print("Change Owed:", abs(amt))
        else:
            print("Amount Due:", amt)
    else:
        print("Amount Due:", amt)
