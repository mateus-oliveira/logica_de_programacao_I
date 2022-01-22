from utils import return_errors_draw, save_result_on_file


class Player:
    def __init__(self) -> None:
        self._errors = 0
        self._points = 0
        self._name = 'UNKNOW'
        self._words = []

    @property
    def name(self):
        return self._name

    @property
    def errors(self):
        return self._errors

    @property
    def points(self):
        return self._points

    def set_name(self, name):
        self._name = name.upper()

    def save_result(self):
        save_result_on_file(self.name, self._words, self.points)
    
    def print_errors_draw(self):
        errors_list = return_errors_draw(self._errors)
        for error in errors_list:
            print(error)

    def set_new_error(self):
        self._errors += 1
        self._points -= 1

    def set_points(self, word, letter):
        repetitions = len([char for char in word if letter == char])
        self._points += 1 * repetitions

    def reset(self):
        self._errors = 0
    
    def save_word(self, word):
        self._words.append(word)
