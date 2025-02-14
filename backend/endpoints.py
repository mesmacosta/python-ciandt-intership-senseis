"""
Hangman API methods
"""
import uuid
from services import start_game, gess_word, reset_game, new_id


def new():
    """Endpoint to create new game id"""
    return {'game_id': new_id()}, 200

def start(game_id: str):
    """Endpoint to create new game record"""
    return {'game_id': game_id, 'data': start_game(game_id)}, 200

def handle_guess(game_id: str, gess: str):
    """Endpoint handle the guess"""
    return {'game_id': game_id, 'data': gess_word(game_id, gess)}, 200

def reset(game_id: str):
    return {'game_id': game_id, 'data': reset_game(game_id)}, 200

