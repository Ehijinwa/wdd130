guess = ""
print("Welcome to the word guessing game!")

word = "window"
counts = 0


while word  != guess:
    guess = input("What is your guess?")
    if len(word) != len(guess):
        print("Sorry, the guess must have the same number of letters as the secret word")
    else :
        counts = counts + 1

print(f"It took you {counts} guesses")
print("Congratulations! You guessed it!")

    