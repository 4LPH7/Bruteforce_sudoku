# Sudoku Solver with GUI

This project implements a **Sudoku Solver** with a graphical user interface (GUI) using Python and the `customtkinter` library. The solver uses a backtracking algorithm to solve the Sudoku puzzle and updates the GUI in real-time to show progress.

---

## Features

- **Real-Time Updates:** Watch as the solver fills in the Sudoku grid in real-time.
- **Random Puzzle Generator:** Generates a new Sudoku puzzle with random numbers for each run.
- **Modern GUI:** Built with `customtkinter` for a sleek, modern interface.
- **Optimized Solver:** Utilizes backtracking with randomized number placement for improved efficiency.

---

## Prerequisites

- Python 3.7 or higher
- `customtkinter` library

Install `customtkinter` using pip:
```bash
pip install customtkinter
```

---

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script:
   ```bash
   python sudoku_solver.py
   ```

---

## Usage

1. Launch the application to see a randomly generated Sudoku puzzle.
2. Click the **Solve** button to start solving the puzzle.
3. The GUI will update in real-time, and the status bar will indicate the completion time or if no solution exists.

---

## How It Works

1. **Puzzle Generation:**
   - Randomly fills between 12 to 25 cells while ensuring a valid Sudoku setup.

2. **Backtracking Algorithm:**
   - Fills in numbers one by one, backtracking whenever an invalid number is placed.
   - Shuffles the order of numbers to attempt for better performance.

3. **GUI Updates:**
   - Each change in the board is immediately reflected in the GUI using `update_idletasks`.

---

## Screenshots

*(Add screenshots of the GUI here if available)*

---

## Future Improvements

- Add support for importing puzzles from a file or user input.
- Improve puzzle generation to ensure unique solutions.
- Enhance GUI with themes and animations.

---

## License

This project is open-source and available under the MIT License.

---

## Author

- **Your Name**
- GitHub: [@4LPH7](https://github.com/4LPH7)

Feel free to contribute or suggest improvements!

