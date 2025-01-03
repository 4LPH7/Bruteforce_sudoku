import random
import time
import customtkinter as ctk

def is_valid(board, row, col, num):
    """Check if placing a number in a cell is valid."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_cell(board):
    """Find an empty cell in the board. Returns (row, col) or None."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku_gui(board, grid_labels):
    """Solve the Sudoku board using backtracking and update GUI."""
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cells, puzzle is solved

    row, col = empty_cell

    # Optimize number order based on possible placements
    possible_numbers = list(range(1, 10))
    random.shuffle(possible_numbers)

    for num in possible_numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            update_grid(grid_labels, board)

            if solve_sudoku_gui(board, grid_labels):
                return True

            # Undo the move
            board[row][col] = 0
            update_grid(grid_labels, board)

    return False

def update_grid(grid_labels, board):
    """Update the GUI grid with the current board state."""
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                grid_labels[i][j].configure(text="", text_color="gray")
            else:
                grid_labels[i][j].configure(text=str(num), text_color="blue")

    grid_labels[0][0].update_idletasks()

def generate_random_sudoku():
    """Generate a random Sudoku puzzle."""
    board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(random.randint(12, 25)):  # Randomly fill between 12 to 25 cells
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
    return board

def main():
    """Main function to run the Sudoku solver with GUI."""
    sudoku_board = generate_random_sudoku()

    app = ctk.CTk()
    app.title("Sudoku Solver")

    frame = ctk.CTkFrame(app, width=500, height=500)
    frame.pack(pady=10, padx=10)

    grid_labels = []
    for i in range(9):
        row_labels = []
        for j in range(9):
            label = ctk.CTkLabel(frame, text="", width=50, height=50, corner_radius=5, font=("Arial", 18), fg_color="lightgray")
            label.grid(row=i, column=j, padx=2, pady=2)
            row_labels.append(label)
        grid_labels.append(row_labels)

    update_grid(grid_labels, sudoku_board)

    def solve():
        start_time = time.time()
        if solve_sudoku_gui(sudoku_board, grid_labels):
            end_time = time.time()
            status_label.configure(text=f"Sudoku Solved in {end_time - start_time:.2f} seconds!", text_color="green")
        else:
            status_label.configure(text="No Solution Exists.", text_color="red")

    solve_button = ctk.CTkButton(app, text="Solve", command=solve, font=("Arial", 16))
    solve_button.pack(pady=10)

    status_label = ctk.CTkLabel(app, text="Solving Sudoku...", font=("Arial", 14))
    status_label.pack()

    app.mainloop()

if __name__ == "__main__":
    main()
