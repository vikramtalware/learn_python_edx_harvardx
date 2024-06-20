from random import randrange

while True:
    try:
        user = int(input("Level: "))
        computer = randrange(1, user+1)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < computer:
                    print("Too small!")
                elif guess > computer:
                    print("Too large!")
                elif guess == computer:
                    print("Just right!")
                    break
            except ValueError:
                pass
        break
    except ValueError:
        pass
