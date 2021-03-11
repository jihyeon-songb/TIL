import sys
sys.stdin = open('input.txt')

board = [list(map(int,input().split())) for _ in range(9)]
zero = []
result_list = []

check = 0
def Sudoku(zero,board,c):
    global result_list
    global check
    if check:
        return

    if c == len(zero):
        for i in range(9):
            for j in range(9):
                result_list += [board[i][j]]
        check = 1
        return result_list

    x, y = zero[c]
    numbers = [1,2,3,4,5,6,7,8,9]
    
    for j in range(9):
        if board[x][j] in numbers:
            numbers.remove(board[x][j])
        if board[j][y] in numbers:
            numbers.remove(board[j][y])
    
    start_x = x // 3 * 3
    start_y = y // 3 * 3
    for j in range(start_x,start_x+3):
        for k in range(start_y,start_y+3):
            if board[j][k] in numbers:
                numbers.remove(board[j][k])
    if not numbers:
        return

    for j in numbers:
        board[x][y] = j
        Sudoku(zero,board,c+1)
        board[x][y] = 0
        
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero += [[i,j]]

result = Sudoku(zero, board, 0)
for i in range(9):
    for j in range(9*i,9*i+9):
        print("{}".format(result[j]), end = ' ')
    print()