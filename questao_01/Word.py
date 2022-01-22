class Word:
    def __init__(self, word) -> None:
        self._word = word
        self._hidden_word = self.__get_hidden_word(word)
    
    def __get_hidden_word(self, word=None) -> list:
        if not word:
            return []

        return ['_' for _ in word]

    @property
    def word(self):
        return self._word

    @property
    def hidden_word(self):
        return ' '.join(self._hidden_word)
