from flask import Flask, jsonify

from five_in_a_row import FiveInARow
from player import Player

app = Flask(__name__)
# when server starts, game starts and players can connect
# Not the most scalable solution but I think its alright rather than over complicating whats in the brief
# could save games into an array if we wanted to handle multiple games
game = FiveInARow()

@app.route('/')
def index():
    return 'Welcome to my awesome connect 5 game \n please use \'/join\' to enter the game'

@app.route('/join/<string:name>', methods=['POST'])
def join_game(name):
    if game.num_players < 2:
        game.add_player(name)
        player = Player(name, game.num_players)
        response = jsonify(
                data=player.__dict__,
                status=200
            )
        return response
    error_response = jsonify(
                data={'message': 'Sorry 2 players already participating'},
                status=401
            )
    return error_response

@app.route('/print', methods=['GET'])
def display():
    return jsonify(game.print_board())

@app.route('/status', methods=['GET'])
def is_game_over():
    return jsonify(game.is_over())

@app.route('/started', methods=['GET'])
def is_game_started():
    return jsonify(game.is_started())

@app.route('/turn', methods=['GET'])
def get_turn():
    return jsonify(game.turn)

@app.route('/winner', methods=['GET'])
def winner():
    return jsonify(game.winner)

@app.route('/change_turn', methods=['PUT'])
def change_turn():
    game.change_turn()
    return jsonify(200)

@app.route('/change_token/<int:token>', methods=['PUT'])
def change_token(token):
    game.setP1Token(token)
    return jsonify(200)

@app.route('/move/<int:column>', methods=['PUT'])
def move(column):
    game.takeTurn(column)
    if game.is_over():
        return f'Game over, winner is {game.winner}'
    return jsonify(200)



@app.route('/disconnected/<int:playerNum>', methods=['PUT'])
def ending(playerNum):
    # passing the number of the player who remained in the game
    output = game.setWinner(playerNum)
    return(jsonify(output))

if __name__ == '__main__':
    app.run()
