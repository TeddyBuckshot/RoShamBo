from flask import render_template, request
from app import app
from models.player import Player
from models import game

@app.route('/home')
def index():
    return render_template('index.html', title='Rock Paper Scissors!')

@app.route('/home/<choice1>/<choice2>')
def results(choice1, choice2):
    player_one_choice = choice1.lower()
    player_two_choice = choice2.lower()
    winner = game.play_game(choice1, choice2)

    return render_template('result.html', player_one=player_one_choice, player_two=player_two_choice, winner=winner)
    
