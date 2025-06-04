import random as rand

def go():
# picks a random num between 1 and 100
    num = rand.randint(1, 100)
# set guesses left
    gleft = 8
    print("im thinking of a number between 1 and 100.")
# higher or lower logic
    while gleft > 0:
        guess = int(input(f"you've got {gleft} guesses.    "))
# too low guess
        if guess < num:
                print("too low.")
# too high guess
        if guess > num:
                print("too high.")
# nvm ur right
        if guess == num:
            print(f"Congratulations! You guessed the number {num} in {7 - gleft + 1} tries.")
            return

        gleft -= 1
# loser
    print(f"too late. number was {num}")

go()