import random
import os


class Player():
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, board):
        return

    def __str__(self):
        return " Human Player"


class EasyComputer():
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, board):
        return random.choice(board)

    def __str__(self):
        return " Easy Computer"


class NormalComputer():
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, board):
        return random.choice(board)

    def __str__(self):
        return " Normal Computer"


class GameBoard():
    def __init__(self):
        self.board = [[i for i in range(3)] for j in range(3)]
        self.player1 = object()
        self.player2 = object()

    def set_move(self):
        pass

    def add_new_player(self, player_type, player_id):
        if player_id == 1:
            if player_type == '1':
                self.player1 = Player("O")
                return True
            elif player_type == '2':
                self.player1 = EasyComputer("O")
                return True
            elif player_type == '3':
                self.player1 = NormalComputer("O")
                return True
            else:
                print("Input Invalid, please try again!!!")
                return False
        elif player_id == 2:
            if player_type == '1':
                self.player2 = Player("X")
                return True
            elif player_type == '2':
                self.player2 = EasyComputer("X")
                return True
            elif player_type == '3':
                self.player2 = NormalComputer("X")
                return True
            else:
                print("Input Invalid, please try again!!!")
                return False
        else:
            print("Invalid player id!!!")
            return False

    def empty_slots(self):
        pass

    def new_game(self):
        """
        reset the game board
        """
        self.board = [[i for i in range(3)] for j in range(3)]

    def print_instruction(self):
        self.clear_terminal()
        print("\033[103m\033[30mLet's begin a new Tic-Tac-Toe game!!! \033[0m")
        print("")
        listboard = [[j for j in range(i * 3, (i + 1) * 3)] for i in range(3)]
        print(' ' * 10 + '-'*15)
        for row in listboard:
            output = [str(i + 1) for i in row]
            print(' ' * 10 + '|  ' + ' | '.join(output) + '  |')
            print(' ' * 10 + '-'*15)
        print('')
        print('\033[47m\033[30m Enter number 1-9 to place your sign. \033[0m')
        print('')

    def clear_terminal(self):
        """
        use this function to clear the terminal when each new function loaded
        """
        return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    game_board = GameBoard()
    game_board.print_instruction()
    print("Select player1: ")
    valid = False
    while valid is not True:
        player1 = input("1. Player 2. Computer 3. Computer(Hard)")
        valid = game_board.add_new_player(player1, 1)
    print("Select player2: ")
    valid = False
    while valid is not True:
        player2 = input("1. Player 2. Computer 3. Computer(Hard)")
        valid = game_board.add_new_player(player2, 2)

    print(f"Player 1 is: {game_board.player1.letter} {game_board.player1}")
    print(f"Player 2 is: {game_board.player2.letter} {game_board.player2}")