import tkinter as tk

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.create_widgets()

    def create_widgets(self):
        self.entries = [
            [tk.Entry(self.root, width=2, font=('Arial', 20), justify='center') for _ in range(9)] 
            for _ in range(9)
        ]

        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
        
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

    def solve_sudoku(self):
        self.update_board()
        if self.solve():
            self.update_gui()

    def update_board(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                self.board[i][j] = int(value) if value.isdigit() else 0

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_safe(self, row, col, num):
        return (
            not self.used_in_row(row, num)
            and not self.used_in_col(col, num)
            and not self.used_in_box(row - row % 3, col - col % 3, num)
        )

    def used_in_row(self, row, num):
        return num in self.board[row]

    def used_in_col(self, col, num):
        return num in [self.board[i][col] for i in range(9)]

    def used_in_box(self, start_row, start_col, num):
        return any(
            num in self.board[i][start_col : start_col + 3]
            for i in range(start_row, start_row + 3)
        )

    def update_gui(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
