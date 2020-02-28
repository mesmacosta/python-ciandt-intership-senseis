"""
Hangman API methods

1) newGame => UUID onLoad/Reset
2) startGame => passa o id do Game… retorna palavra
3) handleGuess => passa a letra e id do game… retorna erro/acerto e armazena no sllite
4) Reset => finaliza o estado do id do game

Extra:
Validações
"""
import uuid


def new():
    """Endpoint to create new game"""
    return uuid.uuid1(), 200
