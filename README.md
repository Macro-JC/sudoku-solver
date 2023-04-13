# Sudoku Solver in Python
This is a simple Sudoku solver written in Python. The program uses a backtracking algorithm to solve the puzzle. The `solve` function takes a 9x9 grid of integers as input, where 0 represents an empty cell. The function returns `True` if the puzzle is solvable and `False` otherwise. The solved puzzle is printed to the console using the `print_sudoku` function.

To use the solver, define a 9x9 grid of integers representing the Sudoku puzzle and pass it to the solve function. The solved puzzle will be printed to the console.

Example usage:

```python
SUDOKU = [
    [0,0,0,1,0,0,2,9,0],
    [0,0,3,0,2,0,6,0,0],
    [0,0,0,0,9,0,0,0,0],
    [1,0,0,0,0,8,0,0,0],
    [3,0,0,0,7,1,0,0,0],
    [2,9,6,0,0,0,0,0,0],
    [0,6,0,0,0,0,0,0,3],
    [0,0,5,0,0,0,0,1,0],
    [0,0,0,5,0,4,0,0,7],
]

solve(SUDOKU)

```
