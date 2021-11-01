from flask import render_template, request
from app import app
from models import player
from models.player import Player
from models import game


@app.route('/home')
def index():
    return render_template('index.html', title='Rock Paper Scissors!')

@app.route('/start')
def start():
    return render_template('start.html', title='Start Game')

@app.route('/result', methods=['POST'])
def get_result():
    print(request.form)
    player_one_name = request.form['name1']
    player_one_choice = request.form['choice1']
    new_player1 = Player(player_one_name, player_one_choice)
    player_two_name = request.form['name2']
    player_two_choice = request.form['choice2']
    new_player2 = Player(player_two_name, player_two_choice)
    winner = game.play_game(new_player1.choice, new_player2.choice)

    return render_template('result.html', player_name_1=new_player1.name, player_name_2=new_player2.name, player_one=player_one_choice, player_two=player_two_choice, winner=winner)