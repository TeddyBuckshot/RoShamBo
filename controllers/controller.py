from flask import render_template, request
from app import app
from models import computer
from models.player import Player
from models import game
from models.computer import Cmptr
from models.game import Game

@app.route('/home/<choice1>/<choice2>')
def results(choice1, choice2):
    player_one_choice = choice1
    player_two_choice = choice2
    winner = game.play_url_game(choice1, choice2)
    return render_template('result.html', player_one=player_one_choice, player_two=player_two_choice, winner=winner)
    
@app.route('/home')
def index():
    return render_template('index.html', title='Rock Paper Scissors!')

@app.route('/start')
def start():
    return render_template('start.html', title='Start Game')

@app.route("/computer")
def play_computer():
    return render_template('computer.html', title='Play the Computer')

@app.route('/result1', methods=['POST'])
def get_result():
    print(request.form)
    player_one_name = request.form['name1']
    player_one_choice = request.form['choice1']
    new_player1 = Player(player_one_name, player_one_choice)
    player_two_name = request.form['name2']
    player_two_choice = request.form['choice2']
    new_player2 = Player(player_two_name, player_two_choice)
    winner = game.play_game(new_player1.name, new_player2.name, new_player1.choice, new_player2.choice)
    return render_template('result.html', player_name_1=new_player1.name, player_name_2=new_player2.name, player_one=player_one_choice, player_two=player_two_choice, winner=winner)

@app.route('/result2', methods=['POST'])
def get_comp_result():
    player_name = request.form['name1']
    player_choice = request.form['choice1']
    new_player1 = Player(player_name, player_choice)
    computer1 = Cmptr("Computer", computer.computer_choice())
    computer_name = computer1.name
    computer_choice = computer1.choice
    new_game = Game(new_player1.name, computer_name, new_player1.choice, computer_choice)
    winner = game.play_game(new_game.p1_name, new_game.p2_name, new_game.p1_choice, new_game.p2_choice)
    return render_template('result.html', player_name1=new_player1.name, player_name_2=computer_name, player_one=new_player1.choice, player_two=computer_choice, winner=winner)