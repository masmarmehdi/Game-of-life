# Task 1 : displaying the initial board

width = int(input('Input the width of the board:'))
height = int(input('Input the height of the board:'))


def initial_board(width, height):
    board = []
    for i in range(height):
        board.append([])
        for j in range(width):
            board[i].append(0)
    return board


board = initial_board(width, height)


def display_board(board):
    print('Board:')
    for cell in range(len(board)):
        for element in board:
            print(f'[{element[cell]}]', end=' ')
        print()


display_board(board)
