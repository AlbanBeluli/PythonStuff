from random import randint

player_wins = 0
ai_wins = 0
winning_score = 3

while player_wins < winning_score and ai_wins < winning_score:
    print(f"Player Score: {player_wins} AI Score: {ai_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Player, make your move: ").lower()
    rand_num = randint(0,2)
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
            player_wins += 1
        else:
            print("AI wins!")
            ai_wins += 1
    elif player == "paper":
        if ai == "rock":
            print("Player wins!")
            player_wins += 1
        else:
            print("AI wins!")
            ai_wins += 1
    elif player == "scissors":
        if ai == "paper":
            print("Player wins!")
            player_wins += 1
        else:
            print("AI wins!")
            ai_wins += 1
    else:
        print("Something went wrong. Please type: rock, paper or scissors.")
if player_wins > ai_wins:
    print("Congrats you won the game!")
elif player_wins == ai_wins:
    print("It's a tie.")
else:
    print("AI won the game.")
print(f"FINAL SCORES... Player Score: {player_wins} AI Score: {ai_wins}")
