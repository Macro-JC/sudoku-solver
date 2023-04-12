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

def print_sudoku(sudoku):
    for i in range(9):
        # imprimimos seperacacion cada 3 filas
        if i == 3 or i == 6:
            print("|-------+-------+-------|")
        for j in range(9):
            # Separacion cada 3 columnas
            if j % 3 == 0:
                print("| ", end="")
            if sudoku[i][j]:
                print(str(sudoku[i][j]) + " ", end="")
            else:
                print(". ", end="")
        print("|")

def valid(sudoku, n, i, j):
    row = sudoku[i]
    column = [f[j] for f in sudoku]
    block = [sudoku[a][b]
             for a in range(9)
             for b in range(9)
             if i // 3 == a // 3
             and j // 3 == b // 3
             ]
    return n not in row and n not in column and n not in block

def solve(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1,10):
                    # probamos con n
                    if valid(sudoku, n, i, j):
                        sudoku[i][j] = n
                        if solve(sudoku):
                            return True
                        else:
                            sudoku[i][j] = 0
                # backtraking
                return False
    # solucionado !
    return True

print_sudoku(SUDOKU)

solve(SUDOKU)

print_sudoku(SUDOKU)