import tkinter, os

class board:
    def move(self, x1, y1, x2, y2):
        self.board.move(self.squares[y1][x1], (x2 - x1) * 80, (y2 - y1) * 80)
        if self.squares[y2][x2] != '':
            self.board.delete(self.squares[y2][x2])
        self.squares[y2][x2] = self.squares[y1][x1]
        self.squares[y1][x1] = ''

    def createpiece(self, x, y, color, piece):
        img = self.pieces[color][piece]
        self.squares[y][x] = self.board.create_image(x*80+40, y*80+40, image=img)

    def __init__(self, trigger):
        self.click = ''

        self.root = tkinter.Tk()
        self.root.geometry('640x640')
        self.root.title('Chess')

        self.board = tkinter.Canvas(self.root, width=640, height=640)
        self.board.pack()

        self.pieces = {'black': {}, 'white': {}}
        directories = os.listdir('pieces')
        directories.remove('.DS_Store')

        for directory in directories:
            subdirs = os.listdir('pieces/' + directory)
            for subdir in subdirs:
                self.pieces[directory][subdir.replace('.gif', '')] = tkinter.PhotoImage(file='pieces/'+directory+'/'+subdir).subsample(5,5)

        self.squares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        self.boardsquares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        for x in range(8):
            for y in range(8):
                if x % 2 == y % 2:
                    self.boardsquares[y][x] = self.board.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='#b3b3b3')
                else:
                    self.boardsquares[y][x] = self.board.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='#666666')

        self.createpiece(0, 0, 'black', 'rook')
        self.createpiece(7, 0, 'black', 'rook')
        self.createpiece(1, 0, 'black', 'knight')
        self.createpiece(6, 0, 'black', 'knight')
        self.createpiece(2, 0, 'black', 'bishop')
        self.createpiece(5, 0, 'black', 'bishop')
        self.createpiece(4, 0, 'black', 'king')
        self.createpiece(3, 0, 'black', 'queen')
        for x in range(8):
            self.createpiece(x, 1, 'black', 'pawn')
            self.createpiece(x, 6, 'white', 'pawn')
        self.createpiece(0, 7, 'white', 'rook')
        self.createpiece(7, 7, 'white', 'rook')
        self.createpiece(1, 7, 'white', 'knight')
        self.createpiece(6, 7, 'white', 'knight')
        self.createpiece(2, 7, 'white', 'bishop')
        self.createpiece(5, 7, 'white', 'bishop')
        self.createpiece(4, 7, 'white', 'king')
        self.createpiece(3, 7, 'white', 'queen')

        self.board.bind('<Button>', trigger)

    def highlight(self, x, y):
        self.board.itemconfig(self.boardsquares[y][x], fill='lightblue')

    def unhighlight(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardsquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardsquares[y][x], fill='#666666')

    def select(self, x, y):
        self.board.itemconfig(self.boardsquares[y][x], fill='green')

    def unselect(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardsquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardsquares[y][x], fill='#666666')

    def destroy(self):
        self.root.destroy()
        
