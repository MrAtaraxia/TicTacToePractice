#! usr/bin/env python3
"""
python TicTacToeBASIC.py
A basic TicTacToe Game.

Only allows 'valid' moves
Properly checks for game end.
Asks if you want to play again at game end.

TODO:
The only things I can think to add are
Customizable names and symbols.
Selecting if you want to be player 1 or 2
Networking, play with a remote person.
AI, play against a computer opponent.

"""


def make_the_board():
    board = [[str(x) + str(y) for x in range(0, 3)] for y in range(0, 3)]
    return board


def main_game_loop():
    # The main game.
    play1 = ObjectPlayer("Player1", "$")
    play2 = ObjectPlayer("Player2", "*")
    game = ObjectGame(play1, play2)
    continue_the_loop = True
    using_exit = False
    while continue_the_loop:
        game.draw_the_board()  # draw_the_board(game.board)

        the_input = input(game.players[game.current_player].name + " (" +
                          game.players[game.current_player].symbol + ") " +
                          "Please type the number of the location you want or type Exit to end the program.")

        legal_move = 0

        for x in range(0, len(game.board)):
            for y in range(0, len(game.board[0])):
                if game.board[x][y] == the_input:
                    game.board[x][y] = game.players[game.current_player].symbol
                    legal_move = 1
                    game.next_player()
                    break

        game_end = check_for_game_end(game.board)

        for play in game.players:
            if play.symbol == game_end:
                print("Congratulations " + play.name + "!")
                print("Player: " + play.name + " is the winner!")
                continue_the_loop = False

        if the_input.lower() == "exit":
            continue_the_loop = False
            using_exit = True
        elif game_end == "Game Over":
            print("The game is over. No one won. :(")
            continue_the_loop = False
        elif legal_move == 0:
            print("That does not appear to be a legal move, please try again.")

    end_game(using_exit)


def draw_the_board(the_board):
    print(the_board[0][0], "|", the_board[0][1], "|", the_board[0][2])
    print("------------")
    print(the_board[1][0], "|", the_board[1][1], "|", the_board[1][2])
    print("------------")
    print(the_board[2][0], "|", the_board[2][1], "|", the_board[2][2])


def process_the_input():
    the_input = input("Where would you like to go?")
    print(the_input)


def check_for_game_end(board):
    # checks if someone has won the game.
    if board[0][0] == board[0][1] == board[0][2] or \
            board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] or \
            board[0][1] == board[1][1] == board[2][1] or \
            board[0][0] == board[1][1] == board[2][2] or \
            board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    if board[2][0] == board[2][1] == board[2][2] or \
            board[0][2] == board[1][2] == board[2][2]:
        return board[2][2]
    # Checks if there are any spaces that have not been taken yet.
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] == str(y) + str(x):
                return False
    return "Game Over"


def end_game(if_exit):
    end = False
    if if_exit:
        end = True
    while not end:
        the_input = input("Would you like to play again Y/N?")
        if the_input.lower() == "y" or the_input.lower() == "yes" or the_input.lower() == "(y)es":
            main_game_loop()
            end = True  # This will make it so there are not multiple of these afterwards.
        elif the_input.lower() == "n" or the_input.lower() == "no" or the_input.lower() == "(n)o":
            end = True
        elif the_input.lower() == "o" or the_input.lower() == "or":
            print("Seriously...")
        else:
            print("Please enter (Y)es or (N)o")


class ObjectPlayer:
    def __init__(self, name, symbol, ai=None):
        self.name = name
        self.symbol = symbol
        self.ai = ai
        if self.ai:
            self.ai.owner = self


class ObjectGame:
    def __init__(self, player1, player2, number_of_players=2):
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]
        self.number_of_players = number_of_players
        self.current_player = 0
        self.board = make_the_board()

    def next_player(self):
        self.current_player += 1
        self.current_player = self.current_player % self.number_of_players

    def draw_the_board(self):
        print(self.board[0][0], "|", self.board[0][1], "|", self.board[0][2])
        print("------------")
        print(self.board[1][0], "|", self.board[1][1], "|", self.board[1][2])
        print("------------")
        print(self.board[2][0], "|", self.board[2][1], "|", self.board[2][2])


class ComponentBasicAI:
    def __init__(self, player=None):
        self.owner = player

    def take_turn(self, board):
        # Returns the value of the location that the ai wants to take.
        allowed_moves = []
        opponent = []
        player = []
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] == str(y) + str(x):
                    allowed_moves.append(board[x][y])
                elif board[x][y] == self.owner.symbol:
                    player.append(str(y) + str(x))
                else:
                    opponent.append(str(y) + str(x))
        for move in allowed_moves:
            if move == "11":
                return 11
        # Checks to see if there are any cells that will allow the player to 'win'
        # if so takes one of those locations.
        # Checks to see if there are any cells that will allow the opponent to 'win'
        # if so takes one of those locations.
        # Checks to see if there are any cells that will make the player 1 away from winning
        #


if __name__ == "__main__":
    main_game_loop()
