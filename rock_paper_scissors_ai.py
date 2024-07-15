import random

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    ai = "rock"
elif rand_num == 1:
    ai = "paper"
else:
    ai = "scissors"
print(f"AI plays {ai}")


if player == ai:
    print("It's a tie!")
elif player == "rock":
    if ai == "scissors":
        print("Player wins!")
    elif ai == "paper":
        print("AI wins!")
elif player == "paper":
    if ai == "rock":
        print("Player wins!")
    elif ai == "scissors":
        print("AI wins!")
elif player == "scissors":
    if ai == "paper":
        print("Player wins!")
    elif ai == "rock":
        print("AI wins!")
else:
    print("Something went wrong. Please type: rock, paper or scissors.")
