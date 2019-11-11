class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.currentStatus = ['_' for _ in range(len(self.secretWord))]
        self.numTries = 0

        pass


    def display(self):
        for c in self.currentStatus:
            print(c, end="")
        print()
        print('Tries: %d'% self.numTries)
        pass


    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus[i] = character
        else:
            self.numTries += 1
        self.check = ''
        for c in self.currentStatus:
            self.check += c
        if self.check == self.secretWord:
            return True
        pass
