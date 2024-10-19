class TicTacToe:
    class InvalidMove(Exception):
        def __init__(self, message) -> None:
            super().__init__(message)
            self.message = message

    def __init__(self):
        """
        Initialize a 3x3 board and set the current player to 1 (Aalu)
        """
        self.board = {
            0: [0, 0, 0],
            1: [0, 0, 0],
            2: [0, 0, 0]
        }
        self.CHOICES = {
            1: "Aalu",   # Player 1
            -1: "Cross"  # Player -1
        }
        self.current_player = 1  # Aalu starts first

    def check_win(self, value):
        """
        Check if the current player has won.
        @param value: The value of the current player (1 or -1)
        @return: True if there's a win, else False
        """
        win_list = [value, value, value]

        row_win = any([self.board[x] == win_list for x in range(3)])

        column_win = any(
            [True for x in range(3) if [self.board[y][x] for y in range(3)] == win_list]
        )

        positive_diagonal_win = [self.board[x][x] for x in range(3)] == win_list

        negative_diagonal_win = [self.board[x][2 - x] for x in range(3)] == win_list

        return row_win or column_win or positive_diagonal_win or negative_diagonal_win

    def move(self, x, y, value):
        """
        @param x: row (0, 1, or 2)
        @param y: column (0, 1, or 2)
        @param value: 1 (Aalu) or -1 (Cross)
        @raises InvalidMove: If the cell is already occupied.
        """
        if self.board[x][y] != 0:
            raise self.InvalidMove("This position is already occupied!")

        self.board[x][y] = value

        if self.check_win(value):
            print(f"{self.CHOICES[value]} wins!")
            return True

        # If the board is full but no winner, declare draw
        if all(self.board[row][col] != 0 for row in range(3) for col in range(3)):
            print("It's a draw!")
            return True

        return False 

    def display_board(self):
        """
        Display the current state of the board.
        """
        for row in self.board.values():
            print(" | ".join([self.CHOICES.get(x, " ") for x in row]))
            print("-" * 9)

    def play(self):
        """
        Play the game until there is a win or a draw.
        """
        game_over = False
        while not game_over:
            self.display_board()
            print(f"Player {self.CHOICES[self.current_player]}'s turn.")
            try:
                x = int(input("Enter row (0, 1, or 2): "))
                y = int(input("Enter column (0, 1, or 2): "))
                game_over = self.move(x, y, self.current_player)
                # Switch player turn
                self.current_player *= -1
            except ValueError:
                print("Please enter valid numbers!")
            except self.InvalidMove as e:
                print(e)

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
