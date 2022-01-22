from os import system
from random import choice
from constants import ERRORS

scores_file = open('scores.txt', 'w')
words_file = open('words.txt', 'r')

def clear():
    system('clear')


def get_some_word() -> str:
    words = words_file.read().split('\n')
    words_file.close()
    return choice(words)


def return_errors_draw(errors) -> None:
    return ERRORS[errors]


def print_game_board(word, player):
    '''
    Print terminal game board

    Args:
        word (Word): instance of Word class
        player (Player): instance of Player class
    
    Returns: None
    '''
    print(f'Pontos: {player.points}')
    player.print_errors_draw()
    print(word.hidden_word)