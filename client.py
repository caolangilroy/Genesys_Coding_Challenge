import requests
from time import sleep
import http.client
import json

HEADERS = {'Content-type': 'application/json'}
SERVER_URL = 'http://127.0.0.1:5000/'

def take_turn():
    turn = requests.get(f'{SERVER_URL}turn').json()
    print(f'Turn belongs to player {turn}')

    if game_player['number'] == turn:
        board = requests.get(f'{SERVER_URL}print')
        print(board.json())
        column = input('Input column to drop: ')
        requests.put(f'{SERVER_URL}move/{column}')
        board = requests.get(f'{SERVER_URL}print')
        print(board.json())
        requests.put(f'{SERVER_URL}change_turn')
        check_is_game_over()
    else:
        while turn != game_player['number']:
            playerDisconnected = requests.get(f'{SERVER_URL}status').json()
            if playerDisconnected:
                print(f"CONGRATULATIONS {name} YOU WIN ")
                print("Game Over, closing in 10 seconds")
                sleep(10)
                break
            sleep(3)
            turn = requests.get(f'{SERVER_URL}turn').json()
        print('next turn')
        check_is_game_over()


def check_is_game_over():
    is_game_over = requests.get(f'{SERVER_URL}status').json()
    if not is_game_over:
        take_turn()
    else:
        winner = requests.get(f'{SERVER_URL}winner')
        print(f'WINNER IS PLAYER {winner.json()}')
        sleep(5)


def play():
    print('PLAY')
    is_game_started = requests.get(f'{SERVER_URL}started').json()
    if not bool(is_game_started):
        print('Waiting for another player to join...')
    while not is_game_started:
        sleep(3)
        print('/started')
        is_game_started = requests.get(f'{SERVER_URL}started').json()
    take_turn()

def start_server():
    global name
    name = input('Your name: ')
    conn.request('POST', f'/join/{name}', headers=HEADERS)
    game_response = conn.getresponse()
    game_player_json = json.loads(game_response.read())


    global game_player
    game_player = game_player_json['data']
    print(f"Game_player: {game_player}")
    if game_player_json['status'] == 401:
        print(game_player['message'])
    else:
        if game_player["number"] == 1:
            tokenChoice =  input('Choose your token, Press 1 for (X) or Press 2 for (O): ')
            requests.put(f'{SERVER_URL}change_token/{tokenChoice}')
        print(game_player['message'])
        play()



if __name__ == '__main__':
    try:
        global conn
        conn = http.client.HTTPConnection("localhost", 5000)
        conn.request('GET', '/status', headers=HEADERS)
        resp = conn.getresponse().read()
        is_game_over = json.loads(resp)
        start_server()
    finally:
        gameIsOver = requests.get(f'{SERVER_URL}status').json()
        if not gameIsOver:
            player_disconnected = game_player["number"]
            winner = None
            if player_disconnected == 1:
                winner = 2
            else:
                winner = 1
            conn.request('PUT', f'/disconnected/{winner}', headers=HEADERS)
            winner = json.loads(conn.getresponse().read())

        conn.close()