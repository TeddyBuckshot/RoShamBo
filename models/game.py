class Game():
    def __init__(self, p1_name, p2_name, p1_choice, p2_choice):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_choice = p1_choice
        self.p2_choice = p2_choice

def play_game(name1, name2, choice1, choice2):
    winner = name2
    if choice1 == choice2:
        winner = "tie"
    if choice1 == "rock" and choice2 == "scissors":
        winner = name1
    if choice1 == "scissors" and choice2 == "paper":
        winner = name1
    if choice1 == "paper" and choice2 == "rock":
        winner = name1
    return winner
