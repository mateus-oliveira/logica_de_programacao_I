from utils import get_some_word


class Word:
    def __init__(self) -> None:
        word = get_some_word()
        self._word = word
        self._hidden_word = self.__get_hidden_word(word)

    @property
    def word(self) -> str:
        return self._word

    @property
    def hidden_word(self) -> str:
        return ' '.join(self._hidden_word)
    
    def __get_hidden_word(self, word=None) -> list:
        if not word:
            return []
        return ['_' for _ in word]
    
    def __find_indexes(self, string, char) -> list: 
        return [i for i, ltr in enumerate(string) if ltr == char]

    def is_letter_on_word(self, letter) -> bool:
        if letter.upper() in self._word:
            indexes = self.__find_indexes(self._word, letter)
            for i in indexes:
                self._hidden_word[i] = letter
            return True
        return False
