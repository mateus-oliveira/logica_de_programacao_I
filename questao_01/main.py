from tabulate import tabulate

from classes.word import Word
from classes.player import Player
from constants import BYE
from utils import clear, print_game_board, get_table_to_list


def new_game(same_player=None):
    if same_player:
        same_player.reset()

    player = same_player or Player()
    word = Word()

    running = True

    while running:
        clear()
        print_game_board(word, player)
        letter = input().upper()
        if word.is_letter_on_word(letter):
            player.set_points(word.word, letter)
        else:
            player.set_new_error()

        running = player.errors < 6 and '_' in word.hidden_word
        
        if not running:
            clear()
            print_game_board(word, player)
            if '_' not in word.hidden_word:
                print(f'\nParabéns, você descobriu a palavra!')
                player.save_word(word.word)

                play_again = input("\n'S' - Sim\n'N' - Não\nDeseja jogar novamente? ").upper()

                if play_again == 'S':
                    new_game(player)
                else:
                    name = input('Informe seu nome para salvar o resultado: ')
                    player.set_name(name)
                    player.save_result()
                    print(BYE)
            else:
                print(f'\nVocê perdeu! A palavra era {word.word}.')
                name = input('Informe seu nome para salvar o resultado: ')
                player.set_name(name)
                player.save_result()
                print(BYE)


def list_scores():
    clear()
    table = get_table_to_list()
    print(tabulate(table, headers=['NOME','PALAVRAS', 'PONTOS']))
    print()


def main():
    option = 0

    while option not in (1, 2, 3):
        clear()
        option = int(input('1 - Novo jogo\n2 - Ver scores\n3 - Sair\nSelecione uma opção: '))
    
    selected = {1: new_game, 2: list_scores, 3: print(BYE)}
    selected[option]()


if __name__ == '__main__':
    try:
        main()
    except:
        pass