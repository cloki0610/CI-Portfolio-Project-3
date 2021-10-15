"""
Required random for random choice and integers,
os for clear terminal function
time for deley the output refresh
math for create a negative infinitive number
"""
import random
import os
import time
import math


class Player():
    """
    A player object control by user
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "A user"

    def make_move(self, game_board):
        """
        Get a user input and check the value
        if not in range then raise error message
        and request another input
        """
        user_input = None
        avaliable_move = [i + 1 for i, spot in enumerate(game_board.board)
                          if spot is None]
        # Use while loop to validate the input
        # If input invalid raise the exception
        while (isinstance(user_input, int) is False or
               user_input < 1 or
               user_input > 9):
            try:
                user_input = int(input("Input a number between 1-9: \n"
                                 .center(81)))
                if user_input not in avaliable_move:
                    raise ValueError
            except ValueError:
                print('\033[31mInput invalid, please try again!!!\033[0m'
                      .center(87))
        # Return result
        return user_input


class EasyComputer():
    """
    A player object control by computer with random move
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "Computer(Easy)"

    def make_move(self, game_board):
        """
        Get a number from the user instance
        """
        return random.randint(1, len(game_board.board))


class HardComputer():
    """
    A player object control by computer with minimax algorithm
    """
    def __init__(self, letter, pname):
        self.letter = letter
        self.pname = pname

    def __str__(self):
        return "Computer(Hard)"

    def make_move(self, game_board):
        """
        If the board is empty, return a random number as choice,
        if the board is not empty, call find_move method and return a number
        """
        empty_slots = game_board.empty_slots()
        if empty_slots == 9:
            return random.choice([1, 3, 5, 7, 9])
        else:
            return self.find_move(game_board)

    def find_move(self, state):
        """
        use recursive and minimax algorithm to calculate the best move
        1. find all the avaliable move and store into a array
        2. use for loop to every avaliable move
        3. make a move
        4. use find_best_score method to get a score of each mvoe
        5. undo the move
        6. compare the best score,
            if this is the best score, then assign this move as best_move
        7. return the best move
        """
        best_move = 0
        best_score = -math.inf
        # Find all the avaliable move
        avaliable_move = [i for i, spot in enumerate(state.board)
                          if spot is None]
        # Use a for loop and fin_best_score method to get the bes move
        for move in avaliable_move:
            state.board[move] = self.letter
            score = self.find_best_score(state, self.letter, False)
            state.board[move] = None
            if score > best_score:
                best_score = score
                best_move = move
        # Return result
        return best_move + 1

    def find_best_score(self, state, current_letter, is_my_turn):
        """
        User recursion to find all the possible result of the game,
        each result will sum with the empty slot and count as a score,
        and store the score into a array,
        then return a sum of the array
        """
        # Find all the avaliable_move
        avaliable_move = [i for i, spot in enumerate(state.board)
                          if spot is None]
        # base case
        if len(avaliable_move) == 0 and state.winner is None:
            return 0
        elif state.winner is not None:
            return len(avaliable_move) + 1 if state.winner == self.pname \
                else -1 * (len(avaliable_move) + 1)
        # Use for loop to count the scores
        scores = []
        for move in avaliable_move:
            # switch user
            if current_letter == "O":
                current_letter = "X"
            else:
                current_letter = "O"
            # set a move
            state.board[move] = current_letter
            # check winner
            if state.check_winner(current_letter) is True:
                if current_letter == "O":
                    state.winner = "Player 1"
                else:
                    state.winner = "Player 2"
            # use recursion to find all next move
            scores.append(self.find_best_score(state, current_letter,
                                               not is_my_turn))
            # undo all  changes
            state.board[move] = None
            state.winner = None
            if current_letter == "O":
                current_letter = "X"
            else:
                current_letter = "O"
        # return the sum of the scores
        return sum(scores)


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
        move = player.make_move(self)
        # get another input if the slot is not null
        while self.board[move - 1] is not None:
            if isinstance(player, Player):
                print('\033[31mYou cannot select a filled grid.\033[0m'
                      .center(87))
            move = player.make_move(self)
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
                self.player1 = HardComputer("O", "Player 1")
                return True
            else:
                print("\033[31mInput Invalid, please try again!!!\033[0m"
                      .center(87))
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
                self.player2 = HardComputer("X", "Player 2")
                return True
            else:
                print("\033[31mInput Invalid, please try again!!!\033[0m"
                      .center(87))
                return False
        # prepare for some unexpected error
        else:
            print("Invalid player id!!!")
            return False

    def clear_terminal(self):
        """
        use this function to clear the terminal when each new function loaded
        """
        return os.system('cls' if os.name == 'nt' else 'clear')

    def empty_slots(self):
        """
        Use the list comprehensions get all the avaliable array,
        and return it's length
        """
        avaliable_move = [i for i, spot in enumerate(self.board)
                          if spot is None]

        return len(avaliable_move)

    def check_winner(self, letter):
        """
        take a letter of user instance as argument,
        and check the self.board array,
        if the letter connect a line in game board,
        that means a player win the game and the method will return True,
        if passed all for loops then return False,
        means the match still in progress or it is a tie.
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

    def print_board(self):
        """
        print the current gameboard
        """
        # first line
        print(("\033[47m\033[30m " + " " * 14 + '-'*13 + " " * 14 +
               " \033[0m").center(93))
        # second to last line with border
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            output = [i if i is not None else ' ' for i in row]
            print(("\033[47m\033[30m" + " " * 14 + ' | ' + ' | '.join(output) +
                  ' | ' + " " * 14 + "\033[0m").center(93))
            print(("\033[47m\033[30m " + " " * 14 + '-'*13 + " " * 14 +
                   " \033[0m").center(93))

    def print_instruction(self):
        """
        Print out the welcome page with instruction
        """
        self.clear_terminal()
        # banner
        print("\033[103m   \
\033[30m Let\'s begin a new Tic-Tac-Toe game!    \033[0m".center(93))
        # game board first line
        print(("\033[47m\033[30m " + " " * 14 + '-'*13 + " " * 14 +
               " \033[0m").center(93))
        # second to last line with border
        for row in [[j for j in range(i * 3, (i + 1) * 3)] for i in range(3)]:
            output = [str(i + 1) for i in row]
            print(("\033[47m\033[30m" + " " * 14 + ' | ' + ' | '.join(output) +
                  ' | ' + " " * 14 + "\033[0m").center(93))
            print(("\033[47m\033[30m " + " " * 14 + '-'*13 + " " * 14 +
                   " \033[0m").center(93))
        print('')
        print('Select two player to begin.'.center(79))
        print('')

    def result(self):
        """
        Get the winner value from constructor and print the results
        """
        self.clear_terminal()
        self.print_board()
        # if no winner, print message to let user know it is a tie
        if self.winner is None:
            print("")
            print("\033[103m\033[30m It is a tie!!! \033[0m\n".center(95))
            print("")
        # if player 1 is winner display result with blue background
        elif self.winner == "Player 1":
            print(("\033[44m" + " " * 43 + "\033[0m").center(87))
            print(("\033[44m" + " " * 8 +
                   f"The Winner is... {self.winner}!!!" +
                   " " * 7 + "\033[0m").center(87))
            print(("\033[44m" + " " * 43 + "\033[0m").center(87))
        # if player 2 is winner display result with red background
        elif self.winner == "Player 2":
            print(("\033[41m" + " " * 43 + "\033[0m").center(87))
            print(("\033[41m" + " " * 8 +
                   f"The Winner is... {self.winner}!!!" +
                   " " * 7 + "\033[0m").center(87))
            print(("\033[41m" + " " * 43 + "\033[0m").center(87))
        else:
            print("self.winner Error, please check and try again!!!")
        # get y or n to begin another match or close the programme
        try_again = None
        while try_again != "y" or try_again != "n":
            try_again = input(("\033[103m\033[30m" + " " * 14 +
                               "Try again? (Y/N)" + " " * 13 + "\033[0m\n")
                              .center(95)).lower()
            if try_again == "y":
                self.player_select()
            elif try_again == "n":
                exit()
            else:
                print('\033[31mInput invalid, please try again!!!\
\033[0m'.center(85))

    def new_game(self):
        """
        reset the game board and start a new game
        """
        self.clear_terminal()
        # reset present gameboard
        self.board = [None for i in range(9)]
        self.winner = None
        # assign the current player to a variable
        turn = self.player1
        # loop until there is no empty slots or someone win the match
        while self.empty_slots() > 0:
            self.clear_terminal()
            print(("\033[103m\033[30m" + " " * 13 + "***TIC TAC TOE***" +
                   " " * 13 + "\033[0m").center(93))
            # print the contents
            standard_output = f"{turn.pname}'s ({turn.letter}) turn:"
            if turn.letter == "O":
                letter_output = "\033[44m\033[37m" + " " * 12 + \
                                standard_output + " " * 11 + "\033[0m"
            else:
                letter_output = "\033[41m\033[37m" + " " * 12 + \
                                standard_output + " " * 11 + "\033[0m"
            print((letter_output).center(93))
            self.print_board()
            # get the move from user or computer
            current_move = self.get_move(turn)
            # add a sign to the board
            self.board[current_move - 1] = turn.letter
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

    def player_select(self):
        """
        Handle the welcome message and player selection,
        after create two valid player,
        the method will call the new game methond
        """
        # Print the instruction method
        self.print_instruction()
        print(("\033[47m\033[30m" + " " * 13 + "Select player1:" +
              " " * 15 + "\033[0m").center(93))
        # Create the player 1, and use a while loop to validate input value
        valid = False
        while valid is not True:
            player1 = input("1.Player 2.Computer(Easy) \
3.Computer(Hard)\n".center(81))
            valid = self.add_new_player(player1, 1)
        print(("\033[47m\033[30m" + " " * 13 + "Select player2:" +
               " " * 15 + "\033[0m").center(93))
        # Create the player 2, and use a while loop to validate input value
        valid = False
        while valid is not True:
            player2 = input("1.Player 2.Computer(Easy) \
3.Computer(Hard)\n".center(81))
            valid = self.add_new_player(player2, 2)
        # Print out the new player instance in the board
        print(f"Player 1: {self.player1} use {self.player1.letter}".center(77))
        print(f"Player 2: {self.player2} use {self.player2.letter}".center(77))
        # Begin a new game after 3 seconds
        time.sleep(5)
        self.new_game()


if __name__ == "__main__":
    # Create a new game board instance and run the play function
    board = GameBoard()
    board.player_select()
