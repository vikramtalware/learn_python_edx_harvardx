import random

def main():
    score = 0
    problems = 10

    l = get_level()

    while problems != 0:
        x, y = generate_integer(l)
        print("Problem No:", problems)
        answer = x + y
        for i in range(3):
            try:
                question = int(input(f"{x} + {y} = "))
                if question == answer:
                    problems -= 1
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
            if i == 2:
                print(f"{x} + {y} = {answer}")
                problems -= 1

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

if __name__ == "__main__":
    main()
