class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[3 for i in range(board_size)] for j in range(board_size)]

    def print_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.board[i][j], end=" ")
            print()

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, value):
        self.board[x][y] = value


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_name(self, name):
        self.name = name


class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = Board(board_size)
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1
        self.game_over = False

    def play(self):
        while not self.game_over and not self.check_tie():
            self.board.print_board()
            print(f"It's {self.current_player.get_name()}'s turn ({self.current_player.get_symbol()})")
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            if self.board.get_cell(x, y) == 3:  # Assuming 0 represents an empty cell
                self.board.set_cell(x, y, self.current_player.get_symbol())
                if self.check_win(self.current_player.get_symbol()):  # Updated call
                    print(f"Congratulations {self.current_player.get_name()}! You won!")
                    self.game_over = True
                else:
                    self.switch_player()
            else:
                print("That cell is already taken. Please choose another cell.")

        self.board.print_board()
        if self.check_tie():
            print("It's a tie!")
            self.game_over = True

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_win(self, symbol):  # Accepts the symbol to check for the win
        board = self.board.get_board()
        # Check rows, columns, and diagonals for a win
        for i in range(self.board_size):
            if self.check_row(board, i, symbol) or self.check_column(board, i, symbol) or self.check_diagonal(board,
                                                                                                              symbol):
                return True
        return False

    def check_row(self, board, row, symbol):
        for i in range(self.board_size):  # Checking the entire row
            if board[row][i] != symbol:
                return False
        return True

    def check_column(self, board, col, symbol):
        for i in range(self.board_size):  # Checking the entire column
            if board[i][col] != symbol:
                return False
        return True

    def check_diagonal(self, board, symbol):
        # Check main diagonal
        win = True
        for i in range(self.board_size):
            if board[i][i] != symbol:
                win = False
                break
        if win:
            return True

        # Check secondary diagonal
        win = True
        for i in range(self.board_size):
            if board[i][self.board_size - i - 1] != symbol:
                win = False
                break
        return win

    def check_tie(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == 3:
                    return False
        return True


game = Game(3)
game.play()
