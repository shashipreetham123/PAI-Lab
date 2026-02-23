def check_constraints (row, col, cols, diag1, diag2) :
    
    if col in cols or (row-col) in diag1 or (row+col) in diag2 :
        return False

    return True

def backtrack(board, row, cols, diag1, diag2, n, solutions) :
    
    if row == n :
        solutions.append(board.copy())
        return
    
    for col in range(n) :
        
        if not check_constraints(row, col, cols, diag1, diag2) :
            continue
        
        board[row] = col
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        
        backtrack(board, row + 1, cols, diag1, diag2, n, solutions)
        
        board[row] = -1
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)
        
def solve_nqueens(n):
    solutions = []
    
    cols = set()
    diag1 = set()
    diag2 = set()
    
    board = [-1] * n
    
    backtrack(board, 0, cols, diag1, diag2, n, solutions)
    
    return solutions


def print_board(board) :
    n = len(board)
    
    for row in range(n) :
        
        for col in range(n) :
            
            if board[row] == col :
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
    
n = int(input("Enter the value of N : "))

solutions = solve_nqueens(n)

for i in range(len(solutions)) :
    
    sol = solutions[i]
    
    print(f"Solution : {i + 1}")
    
    print_board(sol)