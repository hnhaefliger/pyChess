def kingMoves(x, y, color, board):
    moves = []
    if x + 1 <= 7:
        if board[y][x+1][0] != color:
            moves.append([x+1, y])
    if x - 1 >= 0:
        if board[y][x-1][0] != color:
            moves.append([x-1, y])
    if y + 1 <= 7:
        if board[y+1][x][0] != color:
            moves.append([x, y+1])
    if y - 1 >= 0:
        if board[y-1][x][0] != color:
            moves.append([x, y-1])
    if x + 1 <= 7 and y + 1 <= 7:
        if board[y+1][x+1][0] != color:
            moves.append([x+1, y+1])
    if x + 1 <= 7 and y - 1 >= 0:
        if board[y-1][x+1][0] != color:
            moves.append([x+1, y-1])
    if x - 1 >= 0 and y - 1 >= 0:
        if board[y-1][x-1][0] != color:
            moves.append([x-1, y-1])
    if x - 1 >= 0 and y + 1 <= 7:
        if board[y+1][x-1][0] != color:
            moves.append([x-1, y+1])
    return moves

def queenMoves(x, y, color, board):
    moves = []
    moves = rookMoves(x, y, color, board) + bishopMoves(x, y, color, board)
    return moves

def bishopMoves(x, y, color, board):
    moves = []
    if x < y:
        smaller = x
    else:
        smaller = y
    for change in range(1, smaller + 1):
        if board[y-change][x-change][0] != color:
            moves.append([x-change, y-change])
            if board[y-change][x-change][0] != 'e':
                break
        else:
            break

    if x < (7 - y):
        smaller = x
    else:
        smaller = (7 - y)
    for change in range(1, smaller + 1):
        if board[y+change][x-change][0] != color:
            moves.append([x-change, y+change])
            if board[y+change][x-change][0] != 'e':
                break
        else:
            break

    if (7 - x) < y:
        smaller = (7 - x)
    else:
        smaller = y
    for change in range(1, smaller + 1):
        if board[y-change][x+change][0] != color:
            moves.append([x+change, y-change])
            if board[y-change][x+change][0] != 'e':
                break
        else:
            break

    if (7 - x) < (7 - y):
        smaller = (7 - x)
    else:
        smaller = (7 - y)
    for change in range(1, smaller + 1):
        if board[y+change][x+change][0] != color:
            moves.append([x+change, y+change])
            if board[y+change][x+change][0] != 'e':
                break
        else:
            break
    return moves

def rookMoves(x, y, color, board):
    moves = []
    for change in range(1, x + 1):
        if board[y][x-change][0] != color:
            moves.append([x-change, y])
            if board[y][x-change][0] != 'e':
                break
        else:
            break
        
    for change in range(1, (7 - x) + 1):
        if board[y][x+change][0] != color:
            moves.append([x + change, y])
            if board[y][x+change][0] != 'e':
                break
        else:
            break

    for change in range(1, y + 1):
        if board[y-change][x][0] != color:
            moves.append([x, y-change])
            if board[y-change][x][0] != 'e':
                break
        else:
            break

    for change in range(1, (7 - y) + 1):
        if board[y+change][x][0] != color:
            moves.append([x, y+change])
            if board[y+change][x][0] != 'e':
                break
        else:
            break
    return moves

def knightMoves(x, y, color, board):
    moves = []
    if x + 2 <= 7 and y + 1 <= 7:
        if board[y+1][x+2][0] != color:
            moves.append([x+2, y+1])
    if x - 2 >= 0 and y + 1 <= 7:
        if board[y+1][x-2][0] != color:
            moves.append([x-2, y+1])
    if x + 2 <= 7 and y - 1 >= 0:
        if board[y-1][x+2][0] != color:
            moves.append([x+2, y-1])
    if x - 2 >= 0 and y - 1 >= 0:
        if board[y-1][x-2][0] != color:
            moves.append([x-2, y-1])
    if x + 1 <= 7 and y + 2 <= 7:
        if board[y+2][x+1][0] != color:
            moves.append([x+1, y+2])
    if x - 1 >= 0 and y + 2 <= 7:
        if board[y+2][x-1][0] != color:
            moves.append([x-1, y+2])
    if x + 1 <= 7 and y - 2 >= 0:
        if board[y-2][x+1][0] != color:
            moves.append([x+1, y-2])
    if x - 1 >= 0 and y - 2 >= 0:
        if board[y-2][x-1][0] != color:
            moves.append([x-1, y-2])
    return moves
    
def pawnMoves(x, y, color, board):
    moves = []
    if color == 'b':
        if board[y+1][x] == 'e':
            moves.append([x, y+1])
            if y == 1:
                if board[y+2][x] == 'e':
                    moves.append([x, y+2])
        if x - 1 >= 0:
            if board[y+1][x-1][0] == 'w':
                moves.append([x-1, y+1])
        if x + 1 <= 7:
            if board[y+1][x+1][0] == 'w':
                moves.append([x+1, y+1])
                    
    if color == 'w':
        if board[y-1][x] == 'e':
            moves.append([x, y-1])
            if y == 6:
                if board[y-2][x] == 'e':
                    moves.append([x, y-2])
        if x - 1 >= 0:
            if board[y-1][x-1][0] == 'b':
                moves.append([x-1, y-1])
        if x + 1 <= 7:
            if board[y-1][x+1][0] == 'b':
                moves.append([x+1, y-1])
    return moves

def possibleMoves(x, y, piece, board):
    if piece[1] == 'k':
        return kingMoves(x, y, piece[0], board)
    elif piece[1] == 'q':
        return queenMoves(x, y, piece[0], board)
    elif piece[1] == 'b':
        return bishopMoves(x, y, piece[0], board)
    elif piece[1] == 'r':
        return rookMoves(x, y, piece[0], board)
    elif piece[1] == 'h':
        return knightMoves(x, y, piece[0], board)
    elif piece[1] == 'p':
        return pawnMoves(x, y, piece[0], board)
    
    
    
