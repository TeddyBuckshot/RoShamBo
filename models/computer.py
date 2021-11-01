import random

class Cmptr():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return choices[random.randint(0,2)]