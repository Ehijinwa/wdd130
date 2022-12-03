guess = ""
print("Welcome to the word guessing game!")

word = "window"
counts = 0


while word  != guess:
    guess = input("What is your guess?")
    counts = counts + 1

print(f"It took you {counts} guesses")
print("Congratulations! You guessed it!")

    