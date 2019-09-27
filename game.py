import boardGen, moves

def play(event):
    global selection, turn, possible_moves
    x = int((event.x - event.x % 80) / 80)
    y = int((event.y - event.y % 80) / 80)
    
    if selection == '' and board[y][x] != 'e':
        if board[y][x][0] == turn:
            selection = [x, y]
            possible_moves = moves.possibleMoves(x, y, board[y][x], board)
            if board[y][x][1] == 'k':
                if board[y][x][0] == 'w':
                    if x == 4 and y == 7:
                        if board[7][7] == 'wr':
                            if board[7][6] == 'e' and board[7][5] == 'e':
                                possible_moves.append([7, 7])
                        if board[7][0] == 'wr':
                            if board[7][3] == 'e' and board[7][2] == 'e' and board[7][1] == 'e':
                                possible_moves.append([0, 7])
                else:
                    if x == 4 and y == 0:
                        if board[0][7] == 'br':
                            if board[0][6] == 'e' and board[0][5] == 'e':
                                possible_moves.append([7, 0])
                        if board[0][0] == 'br':
                            if board[0][3] == 'e' and board[0][2] == 'e' and board[0][1] == 'e':
                                possible_moves.append([0, 0])
            main.select(x, y)
            for move in possible_moves:
                main.highlight(move[0], move[1])
                
    elif [x, y] == selection:
        main.unselect(selection[0], selection[1])
        for move in possible_moves:
            main.unhighlight(move[0], move[1])

        selection = ''
        possible_moves = []
        
    elif [x, y] in possible_moves:
        moved = False
        if board[selection[1]][selection[0]][1] == 'k':
            if board[selection[1]][selection[0]][0] == 'w':
                if selection == [4, 7]:
                    if [x, y] == [0, 7]:
                        main.move(0, 7, 2, 7)
                        main.move(4, 7, 1, 7)
                        board[7][2], board[7][1] = board[7][0], board[7][4]
                        board[7][1], board[7][4] = 'e','e'
                        moved = True
                    elif [x, y] == [7, 7]:
                        main.move(7, 7, 5, 7)
                        main.move(4, 7, 6, 7)
                        board[7][5], board[7][6] = board[7][7], board[7][4]
                        board[7][7], board[7][4] = 'e','e'
                        moved = True
            else:
                if selection == [4, 0]:
                    if [x, y] == [0, 0]:
                        main.move(0, 0, 2, 0)
                        main.move(4, 0, 1, 0)
                        board[0][2], board[0][1] = board[0][0], board[0][4]
                        board[0][0], board[0][4] = 'e','e'
                        moved = True
                    elif [x, y] == [7, 0]:
                        main.move(7, 0, 5, 0)
                        main.move(4, 0, 6, 0)
                        board[0][5], board[0][6] = board[0][7], board[0][4]
                        board[0][7], board[0][4] = 'e','e'
                        moved = True
        if not(moved):      
            main.move(selection[0], selection[1], x, y)
            board[y][x] = board[selection[1]][selection[0]]
            board[selection[1]][selection[0]] = 'e'

        main.unselect(selection[0], selection[1])
        for move in possible_moves:
            main.unhighlight(move[0], move[1])
            
        possible_moves = []
        selection = ''
        
        if turn == 'w':
            turn  = 'b'
        else:
            turn = 'w'

        found = False
        for line in board:
            for piece in line:
                if piece == turn + 'k':
                    found = True
                    break

        if not(found):
            if turn == 'b':
                print('White wins')
            else:
                print('Black wins')
            main.destroy()
                

board = [['br', 'bh', 'bb', 'bq', 'bk', 'bb', 'bh', 'br'],['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['e', 'e', 'e', 'e', 'e', 'e' ,'e' ,'e'],['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],['wr', 'wh', 'wb', 'wq', 'wk', 'wb', 'wh', 'wr']]

main = boardGen.board(play)
global selection, turn, possible_moves
turn = 'w'
selection = ''
possible_moves = []
main.root.mainloop()
