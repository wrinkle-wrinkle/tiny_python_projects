#!/usr/bin/env python3

class Board:
    def __init__(self):
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.is_winner = False
        self.is_tied = False
        self.__ansi = {'X': '\u001b[31m','O': '\u001b[32m', 'Xw': '\u001b[41m','Ow': '\u001b[42m', 'reset': '\u001b[0m'}
        self.__player = 'X'
        self.player_form = f'{self.__ansi[self.__player]}{self.__player}{self.__ansi["reset"]}'

    def __str__(self):
        nl = '\n'
        hdr = '-------------'
        line1 = f'| {self.values[0]} | {self.values[1]} | {self.values[2]} |'
        line2 = f'| {self.values[3]} | {self.values[4]} | {self.values[5]} |'
        line3 = f'| {self.values[6]} | {self.values[7]} | {self.values[8]} |'
        return f'{hdr}{nl}{line1}{nl}{hdr}{nl}{line2}{nl}{hdr}{nl}{line3}{nl}{hdr}'

    def alternate_player(self):
        if self.__player == 'X':
            self.__player = 'O'
        else:
            self.__player = 'X'
        self.player_form = f'{self.__ansi[self.__player]}{self.__player}{self.__ansi["reset"]}'

    def get_valid(self):
        return [value for value in self.values if value != 'X' and value != 'O']

    def insert(self, move):
        self.values[move] = self.player_form
        self.winner()

    def winner(self):
        winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                   [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i, j, k in winning:
            combo = [self.values[i], self.values[j], self.values[k]]
            if combo == [self.player_form, self.player_form, self.player_form]:
                self.values[i] = f'{self.__ansi[self.__player + "w"]}{self.__player}{self.__ansi["reset"]}'
                self.values[j] = f'{self.__ansi[self.__player + "w"]}{self.__player}{self.__ansi["reset"]}'
                self.values[k] = f'{self.__ansi[self.__player + "w"]}{self.__player}{self.__ansi["reset"]}'
                self.is_winner = True
                print(f'{self.player_form} has won!')
                break
        else:
            if not any(isinstance(x, int) for x in self.values):
                self.is_tied = True
                print('Game Tied!')


def main():
    board = Board()
    print(board)

    while not board.is_winner and not board.is_tied:
        while True:
            try:
                choice = int(input(f'Player {board.player_form}: '))
                assert choice in board.get_valid()
            except ValueError:
                print("Not an integer! Please enter an integer.")
            except AssertionError:
                print("Choice unavailable. Try again.")
            else:
                break

        board.insert(choice)
        print(board)
        board.alternate_player()


# --------------------------------------------------
if __name__ == '__main__':
    main()
