import random
import os


class Player():
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, board):
        return


class EasyComputer():
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, board):
        return random.choice(board)


class NormalComputer():
    pass


class GameBoard():
    def __init__(self, board):
        self.board = board

    def set_move(self):
        pass

    def print_instruction(self):
        clear_terminal()
        print("\033[103m\033[30mLet's begin a new Tic-Tac-Toe game!!!\033[0m")
        listboard = [[j for j in range(i * 3, (i + 1) * 3)] for i in range(3)]
        print(' ' * 10 + '-'*15)
        for row in listboard:
            output = [str(i + 1) for i in row]
            print(' ' * 10 + '|  ' + ' | '.join(output) + '  |')
            print(' ' * 10 + '-'*15)


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def new_game():
    return


if __name__ == "__main__":
    clear_terminal()
    game_board = GameBoard([[i for i in range(3)] for j in range(3)])
    game_board.print_instruction()