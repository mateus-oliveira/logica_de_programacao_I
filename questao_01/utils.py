from os import system
from random import choice
from constants import ERRORS


def clear():
    system('clear')


def get_some_word() -> str:
    words_file = open('words.txt', 'r')
    words = words_file.read().split('\n')
    words_file.close()
    return choice(words)


def return_errors_draw(errors) -> None:
    return ERRORS[errors]


def save_result_on_file(name, words, points):
    scores_file = open('scores.txt', 'a')
    comma_separated_words = ', '.join(words)
    if comma_separated_words:
        scores_file.write(f'{name}; {comma_separated_words}; {points}\n')
    else:
        scores_file.write(f'{name}; {points}\n')
    scores_file.close()


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