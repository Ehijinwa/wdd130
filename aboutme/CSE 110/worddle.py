guess = ""
print("Welcome to the word guessing game!")

word = "window"
counts = 0


while word  != guess:
    guess = input("\nWhat is your guess?")
    if len(word) != len(guess):

        print("Sorry, the guess must have the same number of letters as the secret word")
    else :
        counts = counts + 1
        for i in range(len(word)):
            if word[i] == guess[i]:
                print(guess[i].upper(), end="")
            elif guess[i] in word:
                print(guess[i].lower(), end="")
            else: 
                print("_", end="")

print(f"It took you {counts} guesses")
print("Congratulations! You guessed it!")

    