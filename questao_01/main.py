from utils import clear, print_game_board

from classes.word import Word
from classes.player import Player


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
            else:
                print(f'\nVocê perdeu a palavra era {word.word}!')
                name = input('Informe seu nome para salvar o resultado: ')
                player.set_name(name)
                player.save_result()


def list_scores():
    pass


def main():
    option = 0

    while option not in [1, 2]:
        clear()
        option = int(input('1 - Novo jogo\n2 - Ver scores\nSelecione uma opção: '))
    
    selected = {1: new_game, 2: list_scores}

    selected[option]()

if __name__ == '__main__':
    main()