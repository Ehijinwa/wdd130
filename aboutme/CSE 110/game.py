print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. ")
action = input("what  do you do?").lower()

if action == "match":
    print("you pick the match and you die!")
elif action == "flashlight":
    print("you see the flashlight and get into another dimension")

    player = input("choose your player! SAMURAI JACK or NARUTO ").lower()
    if player == "samurai jack":
        print("you just bought a sword")
    elif player == "naruto":
        print("you just unlocked a new jutsu")
else: 
    print("please type match or flashlight!") 

