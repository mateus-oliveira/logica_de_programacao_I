from utils import clear, print_game_board

from classes.word import Word
from classes.player import Player



def new_game():
    player = Player()
    word = Word()

    while player.errors < 6 or '_' not in word.hidden_word:
        clear()
        print(word.word)
        print_game_board(word, player)
        letter = input().upper()
        if word.is_letter_on_word(letter):
            player.set_points(word.word, letter)
        else:
            player.set_new_error()



def list_scores():
    pass


def main():
    option = 0

    while option not in [1, 2]:
        option = int(input('1 - Novo jogo\n2 - Ver scores\nSelecione uma opção: '))
        clear()
    
    selected = {
        1: new_game, 2: list_scores,
    }

    selected[option]()

if __name__ == '__main__':
    main()