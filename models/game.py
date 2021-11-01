def play_game(choice1, choice2):
    winner = "player_two"
    if choice1 == choice2:
        winner = "tie"
    if choice1 == "rock" and choice2 == "scissors":
        winner = "player_one"
    if choice1 == "scissors" and choice2 == "paper":
        winner = "player_one"
    if choice1 == "paper" and choice2 == "rock":
        winner = "player_one"
    
    return winner
