def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    def backtrack(row):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    solutions = []
    backtrack(0)
    return solutions
def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()
def count_queens(solution,c=0):
        for row in solution:
            for cell in row:
                if cell == 1:
                    c+=1
        return c
n = 4
u=1
r=[]
solutions = solve_n_queens(n)

if solutions:
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        print_solution(solution)
    print('Count of Queens:', count_queens(solution))
else:
    print(f"No solutions found for {n}-Queens.")