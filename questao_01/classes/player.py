from utils import return_errors_draw


class Player:
    def __init__(self) -> None:
        self._errors = 0
        self._points = 0

    @property
    def errors(self):
        return self._errors

    @property
    def points(self):
        return self._points
    
    def print_errors_draw(self):
        errors_list = return_errors_draw(self._errors)
        for error in errors_list:
            print(error)

    def set_new_error(self):
        self._errors += 1
        self._points -= 1

    def set_points(self, word, letter):
        self._points += 10
    
