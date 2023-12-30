class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[3 for _ in range(board_size)] for _ in range(board_size)]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, value):
        self.board[x][y] = value

    def is_full(self):
        return all(cell != 3 for row in self.board for cell in row)

    def check_win(self, symbol):
        for i in range(self.board_size):
            if all(self.board[i][j] == symbol for j in range(self.board_size)) or \
               all(self.board[j][i] == symbol for j in range(self.board_size)):
                return True

        if all(self.board[i][i] == symbol for i in range(self.board_size)) or \
           all(self.board[i][self.board_size - i - 1] == symbol for i in range(self.board_size)):
            return True

        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0

    def current_player(self):
        return self.players[self.current_player_index]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        while True:
            self.board.print_board()
            player = self.current_player()
            x, y = map(int, input(f"{player.name} ({player.symbol}), enter 'x y': ").split())

            if self.board.get_cell(x, y) == 3:
                self.board.set_cell(x, y, player.symbol)
                if self.board.check_win(player.symbol):
                    print(f"Congratulations {player.name}! You won!")
                    break
                elif self.board.is_full():
                    print("It's a tie!")
                    break
                else:
                    self.switch_player()
            else:
                print("That cell is already taken. Please choose another cell.")

        self.board.print_board()


game = Game(3)
game.play()
