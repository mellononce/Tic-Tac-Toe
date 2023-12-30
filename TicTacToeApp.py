import tkinter as tk
from tkinter import messagebox
import random


class TicTacToeApp:
    def __init__(self):
        self.current_player = None
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.difficulty_var = tk.StringVar(value="Medium")  # default difficulty
        self.create_menu()
        self.difficulty = "Medium"  # Also maintain a regular Python string for actual logic use
        self.difficulty_var.trace_add("write", self.on_difficulty_change)  # Use trace_add for newer Tkinter versions

    def start_game(self):
        # First, check if the application is running before proceeding
        if self.window.winfo_exists():
            # Clears the window for the game
            for widget in self.window.winfo_children():
                widget.destroy()

        # Setup the game
        self.window.title("Tic Tac Toe")
        self.window.configure(bg='#ffffff')
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.initialize_board()

        # Start the main loop for the game window
        self.window.mainloop()

        # Recreate status_label or ensure it exists before updating it
        if hasattr(self, 'status_label') and self.status_label.winfo_exists():
            self.status_label.config(text=f"Difficulty: {self.difficulty}")

    def quit_game(self):
        self.window.destroy()  # Quit the application

    def create_menu(self):
        # Clear any existing widgets in the window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Configure the window's background
        self.window.configure(bg='#333333')

        # Title Label
        title_label = tk.Label(self.window, text="TIC TAC TOE", font=('Helvetica', 36, 'bold'), fg='white',
                               bg='#333333')
        title_label.pack(pady=20)

        # Play Button
        play_button = tk.Button(self.window, text="Play", command=self.start_game,
                                font=('Helvetica', 18, 'bold'), fg='white', bg='#333333', relief='flat')
        play_button.pack(pady=10, padx=20, fill='x')

        # Difficulty Label
        difficulty_label = tk.Label(self.window, text="Difficulty",
                                    font=('Helvetica', 18, 'bold'), fg='white', bg='#333333')
        difficulty_label.pack(pady=10, padx=20)

        # Difficulty Dropdown
        self.difficulty_var = tk.StringVar(value="Medium")  # default value
        difficulties = ["Easy", "Medium", "Hard"]  # Options for difficulty
        self.difficulty_dropdown = tk.OptionMenu(self.window, self.difficulty_var, "Easy", "Medium", "Hard")

        # Style the dropdown menu to blend in with the window
        self.difficulty_dropdown.config(font=('Helvetica', 14), fg='white', bg='#333333',
                                        relief='flat', borderwidth=0, highlightthickness=0)

        # Style the dropdown indicator to blend in
        self.difficulty_dropdown["menu"].config(font=('Helvetica', 14), bg='#333333', fg='white')
        self.difficulty_dropdown.pack(pady=10, padx=20)

        # Settings Button
        # settings_button = tk.Button(self.window, text="Settings", command=self.open_settings,
        #                            font=('Helvetica', 18, 'bold'), fg='white', bg='#333333',
        #                            relief='flat', highlightthickness=0, borderwidth=0)
        # settings_button.pack(pady=10, padx=20, fill='x')

        # Quit Button
        quit_button = tk.Button(self.window, text="Quit", command=self.quit_game,
                                font=('Helvetica', 18, 'bold'), fg='white', bg='#333333',
                                relief='flat', highlightthickness=0, borderwidth=0)
        quit_button.pack(pady=10, padx=20, fill='x')

        self.difficulty_var.trace_add("write", self.on_difficulty_change)  # Update the difficulty whenever it changes

    def on_difficulty_change(self, *args):
        # Update the difficulty setting in your game logic
        self.difficulty = self.difficulty_var.get()

    def set_difficulty(self, difficulty):
        # When changing difficulty elsewhere in your code, update self.difficulty_var
        self.difficulty_var.set(difficulty)

    def initialize_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', font=('Helvetica', 24), width=5, height=2,
                                   fg='white', bg='#333333',  # Neutral dark shades
                                   command=lambda i=i, j=j: self.on_click(i, j),
                                   relief='flat', borderwidth=0,
                                   highlightbackground='white', highlightcolor='white', highlightthickness=1)
                button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)  # Padding for grid lines
                self.buttons[i][j] = button
        self.grid_cells_equal_size()

        # Configure column weights (if not already set)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

        # Status Frame
        self.status_frame = tk.Frame(self.window, bg='#333333')
        self.status_frame.grid(row=3, column=0, columnspan=3, sticky="ew")

        # Message Label within the status frame
        self.status_label = tk.Label(self.status_frame, text=f"Difficulty: {self.difficulty}",
                                     font=('Helvetica', 14, 'bold'),
                                     fg='white', bg='#333333')
        self.status_label.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(10, 0))  # Added padding on the y-axis

        # Restart and Menu buttons
        self.restart_button = tk.Button(self.status_frame, text="Restart", command=self.restart, font=('Helvetica', 14),
                                        fg='white', bg='#333333', relief='flat')
        self.restart_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)  # Added padding

        self.menu_button = tk.Button(self.status_frame, text="Menu", command=self.create_menu, font=('Helvetica', 14),
                                     fg='white', bg='#333333', relief='flat')
        self.menu_button.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=10)  # Added padding

        # Ensure the buttons and label take equal space
        self.status_frame.grid_rowconfigure(0, weight=1)
        self.status_frame.grid_rowconfigure(1, weight=1)
        self.status_frame.grid_columnconfigure(0, weight=1)
        self.status_frame.grid_columnconfigure(1, weight=1)
        self.status_frame.grid_columnconfigure(2, weight=1)

    def grid_cells_equal_size(self):
        # Configure the rows and columns of the window to have equal weight
        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def on_click(self, i, j):
        # Only allow the move if the game is ongoing and the cell is empty
        if not self.game_over and self.board[i][j] is None and self.current_player == "X":
            # Update the board and button text
            self.board[i][j] = "X"
            self.buttons[i][j].configure(text="X", state='disabled')

            # Check for a winner or a tie
            winner, winning_line = self.check_winner()
            if winner or self.check_tie():
                self.end_game()
            else:
                # If the game is still ongoing, switch to the next player (AI)
                self.current_player = "O"
                self.window.after(100, self.ai_move)  # Proceed to AI move after a short delay

    def restart(self):
        # Reset the game variables
        self.current_player = "X"
        self.game_over = False
        self.board = [[None for _ in range(3)] for _ in range(3)]
        # Update the status label with the current difficulty when the game restarts
        self.status_label.config(text=f"Difficulty: {self.difficulty}")
        # self.restart_button.config(state='disabled')  # Disable restart button until next end game

        # Reinitialize the board buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state="normal", bg='#333333')

    def check_winner(self):
        # Check rows for winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0], [(i, 0), (i, 1), (i, 2)]

        # Check columns for winner
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] is not None:
                return self.board[0][j], [(0, j), (1, j), (2, j)]

        # Check diagonals for winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0], [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2], [(0, 2), (1, 1), (2, 0)]

        return None, None  # No winner

    def check_tie(self):
        # Get the winner information
        winner, _ = self.check_winner()  # Only interested in the winner, not the winning line

        # Check if all cells are filled and there is no winner
        if all(cell is not None for row in self.board for cell in row) and winner is None:
            return True
        return False

    def cross_out_winning_line(self, line, winner=None):
        # Determine the color based on the winner
        color = 'green' if winner == 'X' else 'red'  # Green for player win, red for AI win

        # Change the background color of the winning buttons
        for i, j in line:
            self.buttons[i][j].config(bg=color)

    def end_game(self):
        # Display the end game result
        # Update the status label with the game outcome
        winner, winning_line = self.check_winner()
        if winner:
            result_message = "You Win!" if winner == "X" else "You Lose!"
            self.cross_out_winning_line(winning_line, winner)
        elif self.check_tie():
            result_message = "Draw!"
        else:
            result_message = ""  # Just in case

        # Update the status label and enable the buttons
        self.status_label.config(text=result_message)
        # self.restart_button.config(state='normal')
        # self.menu_button.config(state='normal')
        self.game_over = True

    def minimax(self, is_maximizing, depth=0):
        winner, _ = self.check_winner()  # Unpack winner; ignore the winning line
        if winner or self.check_tie():  # Check end game conditions
            if winner == "O":  # AI wins
                return (10 - depth, None)  # Subtract depth to prioritize quicker wins
            elif winner == "X":  # Player wins
                return (-10 + depth, None)  # Add depth to prioritize delayed losses
            else:
                return (0, None)  # Tie game

        if is_maximizing:  # Maximizing (AI's move)
            best_score = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = "O"
                        score, _ = self.minimax(False, depth + 1)
                        self.board[i][j] = None
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move
        else:  # Minimizing (Player's move)
            best_score = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = "X"
                        score, _ = self.minimax(True, depth + 1)
                        self.board[i][j] = None
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move

    def ai_move(self):
        if self.current_player == "O" and not self.game_over:  # Ensure it's AI's turn and the game isn't over
            # AI makes a move based on difficulty
            if self.difficulty == "Easy":
                self.ai_move_easy()
            elif self.difficulty == "Medium":
                if not self.medium_strategy():  # If medium strategy doesn't make a move
                    self.ai_move_easy()
            elif self.difficulty == "Hard":
                _, best_move = self.minimax(True)
                if best_move:
                    self.make_move(*best_move, "O")

            # After AI move, check for end game conditions
            winner, winning_line = self.check_winner()
            if winner or self.check_tie():
                self.end_game()
            else:
                # No winner and no tie, explicitly switch back to the player
                self.current_player = "X"

    def ai_move_easy(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.make_move(i, j, "O")

    def medium_strategy(self):
        # Check each line for a win or block opportunity
        for line in self.all_lines():
            move = self.can_win_or_block(line, "O")  # Check if AI can win
            if move:  # If a winning move is found, make it
                self.make_move(move[0], move[1], "O")
                return True

            move = self.can_win_or_block(line, "X")  # Check if AI can block the player
            if move:  # If a blocking move is found, make it
                self.make_move(move[0], move[1], "O")
                return True

        # If no immediate win or block, then make a random move
        return False  # Indicate that no strategic move was made

    def make_move(self, i, j, player):
        if self.board[i][j] is None:  # Ensure the cell is empty
            self.board[i][j] = player
            self.buttons[i][j].configure(text=player, state='disabled')
            winner, winning_line = self.check_winner()
            if winner or self.check_tie():
                self.end_game()
            else:
                # Toggle the turn to the next player
                self.current_player = "X" if player == "O" else "O"

    def can_win_or_block(self, line, player):
        # Extract the line's values
        values = [self.board[i][j] for i, j in line]

        # Check for a winning or blocking opportunity
        if values.count(player) == 2 and values.count(None) == 1:
            # Return the coordinates of the empty spot for a potential move
            empty_spot = line[values.index(None)]
            return empty_spot  # Return the coordinates of the winning/blocking move
        return None

    def all_lines(self):
        lines = []

        # Rows
        for i in range(3):
            lines.append([(i, j) for j in range(3)])  # Each row

        # Columns
        for j in range(3):
            lines.append([(i, j) for i in range(3)])  # Each column

        # Diagonals
        lines.append([(i, i) for i in range(3)])  # Diagonal from top-left to bottom-right
        lines.append([(i, 2 - i) for i in range(3)])  # Diagonal from top-right to bottom-left

        return lines


if __name__ == "__main__":
    game = TicTacToeApp()
    game.window.mainloop()
