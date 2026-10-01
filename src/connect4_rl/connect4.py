import numpy as np

class Connect4:
    ROWS = 6
    COLS = 7
    # 1 is player 1, -1 is player 2, 0 is empty
    def __init__(self):
        self.board = np.zeros((self.ROWS, self.COLS), dtype=np.int8)
        self.current_player = 1


    def valid_actions(self):
        return np.where(self.board[0] == 0)[0]

    def step(self, action):
        if action not in self.valid_actions():
            raise ValueError(f"Invalid action: {action}")

        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row, action] == 0:
                self.board[row, action] = self.current_player
                break

        self.current_player = -self.current_player

        return self.board, self.current_player


    def print_board(self):
        print("Player 1: X, Player 2: O")
        print(" 0 1 2 3 4 5 6")
        print("---------------")

        for row in range(self.ROWS):
            print("|", end="")

            for col in range(self.COLS):
                value = self.board[row, col]

                if value == 1:
                    symbol = "X"
                elif value == -1:
                    symbol = "O"
                else:
                    symbol = " "

                print(symbol, end="|")

            print()
            print("------------")

    def check_win(self, player):
        # Horizontal ——
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if (
                    self.board[row, col] == player
                    and self.board[row, col + 1] == player
                    and self.board[row, col + 2] == player
                    and self.board[row, col + 3] == player
                ):
                    return True

        # Vertical |
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if (
                    self.board[row, col] == player
                    and self.board[row + 1, col] == player
                    and self.board[row + 2, col] == player
                    and self.board[row + 3, col] == player
                ):
                    return True

        # Diagonal \
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if (
                    self.board[row, col] == player
                    and self.board[row + 1, col + 1] == player
                    and self.board[row + 2, col + 2] == player
                    and self.board[row + 3, col + 3] == player
                ):
                    return True

        # Diagonal /
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if (
                    self.board[row, col] == player
                    and self.board[row - 1, col + 1] == player
                    and self.board[row - 2, col + 2] == player
                    and self.board[row - 3, col + 3] == player
                ):
                    return True

        return False

    def is_draw(self):
        return len(self.valid_actions()) == 0

    
if __name__ == "__main__":
    game = Connect4()

    game.step(3)
    game.step(4)
    game.step(3)
    game.step(4)
    game.step(3)

    game.print_board()