import random
import os
import time


class Player():
    """
    A player object control by user
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "A user"

    def make_move(self):
        """
        Get a user input and check the value
        if not in range then raise error message
        and request another input
        """
        user_input = None
        while type(user_input) is not int or user_input < 1 or user_input > 9:
            try:
                user_input = int(input("Input a number between 1-9: \n"))
                if user_input < 1 or user_input > 9:
                    raise ValueError
            except Exception:
                print('\033[31mInput invalid, please try again!!!\033[0m')
        return user_input


class EasyComputer():
    """
    A player object control by computer with random move
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "Easy Computer"

    def make_move(self):
        return random.randint(1, 9)


class NormalComputer():
    """
    A player object control by computer with minimax algorithm
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "Normal Computer"

    def make_move(self):
        return random.randint(1, 9)


class GameBoard():
    """
    A game board class to handle the functions in a tic tac toe game
    """
    def __init__(self):
        self.board = [None for i in range(9)]
        self.player1 = object()
        self.player2 = object()
        self.winner = None

    def get_move(self, player):
        """
        Get a number from player instance, if this move is valid
        then return the number,
        if invalid print a message and require another number
        """
        move = player.make_move()
        # get another input if the slot is not null
        while self.board[move - 1] is not None and self.winner is None:
            if isinstance(player, Player):
                print('\033[31mInput invalid, please try again!!!\033[0m')
            move = player.make_move()
        return move

    def add_new_player(self, player_type, player_id):
        """
        take a input as a argument and create a new player object
        if user is player 1, create a new object and assign into player1
        if user is player 2, create a new player object and assign into player2
        """
        # Player 1
        if player_id == 1:
            if player_type == '1':
                self.player1 = Player("O", "Player 1")
                return True
            elif player_type == '2':
                self.player1 = EasyComputer("O", "Player 1")
                return True
            elif player_type == '3':
                self.player1 = NormalComputer("O", "Player 1")
                return True
            else:
                print("Input Invalid, please try again!!!")
                return False
        # Player 2
        elif player_id == 2:
            if player_type == '1':
                self.player2 = Player("X", "Player 2")
                return True
            elif player_type == '2':
                self.player2 = EasyComputer("X", "Player 2")
                return True
            elif player_type == '3':
                self.player2 = NormalComputer("X", "Player 2")
                return True
            else:
                print("Input Invalid, please try again!!!")
                return False
        # prepared for some unexpected error
        else:
            print("Invalid player id!!!")
            return False

    def empty_slots(self):
        """
        Use a for loop to check how many empty slots and return a number
        """
        count = 0
        for i in range(len(self.board)):
            if self.board[i] is None:
                count += 1

        return count

    def new_game(self):
        """
        reset the game board and start a new game
        """
        self.clear_terminal()
        print("\033[103m\033[30mLet's get started!\033[0m")
        # reset present gameboard
        self.board = [None for i in range(9)]
        self.winner = None
        # assign the current player to a variable
        turn = self.player1
        # loop until there is no empty slots or someone win the match
        while self.empty_slots() > 0:
            self.clear_terminal()
            # print the contents
            print(f"{turn.pname}'s ({turn.letter}) turn:".center(56))
            self.print_board()
            # get the move from user or computer
            c_move = self.get_move(turn)
            # add a sign to the board
            self.board[c_move - 1] = turn.letter
            # check if someone win the match, then call result
            if self.check_winner(turn.letter) is True:
                self.winner = turn.pname
                self.result()
            # switch to next turn
            if turn == self.player1:
                turn = self.player2
            else:
                turn = self.player1
            time.sleep(2)

        # if no winner and the board is filled, call result method
        self.result()

    def check_winner(self, letter):
        """
        take a player object as argument and check the self.board array,
        if player won the match than set the self.winner and call result method
        if no winner then continue the process
        """
        # check all row on the board
        for i in range(3):
            row = self.board[i * 3:(i + 1) * 3]
            if all([i == letter for i in row]):
                return True
        # check column in the board
        for i in range(3):
            col = [self.board[i + j * 3] for j in range(3)]
            if all([i == letter for i in col]):
                return True
        # check diagonal
        diagonal_left = [self.board[0], self.board[4], self.board[8]]
        diagonal_right = [self.board[2], self.board[4], self.board[6]]
        if all([i == letter for i in diagonal_left]):
            return True
        if all([i == letter for i in diagonal_right]):
            return True
        # if pass all loops return false
        return False

    def result(self):
        self.clear_terminal()
        self.print_board()
        # get the winner and print the relevant text
        if self.winner is None:
            print("It is a tie!!!".center(56))
        else:
            print(f"The Winner is... {self.winner}!!!".center(58))
        # get y or n to begin another match or close the programme
        try_again = None
        while try_again != "y" or try_again != "n":
            try_again = input("Try again? (Y/N)\n".center(58)).lower()
            if try_again == "y":
                self.game_start()
            elif try_again == "n":
                exit()
            else:
                print('\033[31mInput invalid, please try again!!!\
\033[0m'.center(64))

    def print_board(self):
        """
        print the current gameboard
        """
        # first line
        print(' ' * 20 + '-'*15)
        # second to last line with bottom border
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            output = [i if i is not None else ' ' for i in row]
            print(' ' * 20 + '|  ' + ' | '.join(output) + '  |')
            print(' ' * 20 + '-'*15)

    def print_instruction(self):
        """
        Print out the welcome page with instruction
        """
        self.clear_terminal()
        # banner
        print("\033[103m\
\033[30m Let\'s begin a new Tic-Tac-Toe game! \033[0m".center(72))
        print("")
        # game board first line
        print(' ' * 20 + '-'*15)
        # second to last line with border
        for row in [[j for j in range(i * 3, (i + 1) * 3)] for i in range(3)]:
            output = [str(i + 1) for i in row]
            print(' ' * 20 + '|  ' + ' | '.join(output) + '  |')
            print(' ' * 20 + '-'*15)
        print('')
        print('Select two player to begin.'.center(56))
        print('')

    def clear_terminal(self):
        """
        use this function to clear the terminal when each new function loaded
        """
        return os.system('cls' if os.name == 'nt' else 'clear')

    def game_start(self):
        """
        handle the game process
        """
        self.print_instruction()
        # Create the player 1, and use a while loop to validate input value
        print("Select player1: ")
        valid = False
        while valid is not True:
            player1 = input("1. Player 2. Computer 3. Computer(Hard)\n")
            valid = self.add_new_player(player1, 1)
        # Create the player 2, and use a while loop to validate input value
        print("Select player2: ")
        valid = False
        while valid is not True:
            player2 = input("1. Player 2. Computer 3. Computer(Hard)\n")
            valid = self.add_new_player(player2, 2)
        # Print out the player object in the board
        print(f"Player 1: {self.player1} use {self.player1.letter}")
        print(f"Player 2: {self.player2} use {self.player2.letter}")
        time.sleep(3)
        self.new_game()


if __name__ == "__main__":
    # Create a new game board instance and run the play function
    game_board = GameBoard()
    game_board.game_start()