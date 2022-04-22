from functools import partial
from operator import truediv
from tkinter import *
from copy import deepcopy

#constant
SUDOKUSIZE = 9

#global values

debugon = FALSE

game = []
savedgame = []
#text requires StringVar instead of direct string due to tkinker
#Or I understood that wrongly, but this works
text = []

class cell:
    def __init__(self, row, col) -> None:
        #starting number
        self.number = int(0)
        #starting list of allowed number
        self.allowed = [1,2,3,4,5,6,7,8,9]
        self.row = row
        self.col = col

    def printinfo(self):
        """print infomation about the cell
        """
        print("INFO: Cell location: (", self.row, ",", self.col, ")")
        print("INFO: Holding number: ", self.number)
        print("INFO: Allowed input number :", self.allowed)

    def setnum(self, num: int):
        """Set holding number to input, remove value of number from "allowed" list,
           This will also call a remove function to remove its number from other cells at the same horizonal, vertical and block

        Args:
            num (int): taget number to change to
        """
        self.number = num
        try:
            self.allowed.clear()
            remove(num, self.row, self.col)
        except:
            pass

    def remove(self, num: int):
        """Remove number from allowed list

        Args:
            num (int): number to remove
        """
        try:
            self.allowed.remove(num)
        except:
            pass


def extend_to_length(ls : list, targetlen: int) -> list:
    """extend a given list to a given length, empty places are set to 0

    Args:
        l (list): list to extend
        len (_type_): target length

    Returns:
        list: extended list
    """
    return ls[:targetlen] + [0]*(targetlen - len(ls))

def remove(num: int, row: int, col: int):
    """remove all same number from the allowed list from other cell at the same horizonal vertical and block of the orgin\n
    (sudoku rule)

    Args:
        num (int): target
        row (int): row index of orgin
        col (int): col index of orgin
    """
    global game
    #remove horizontal and veritcal
    for i in range(SUDOKUSIZE):
        game[row][i].remove(num)
        game[i][col].remove(num)

    #remove block
    #block id
    rowid = row//3 * 3
    colid = col//3 * 3
    for i in range(3):
        game[rowid][colid+i].remove(num)
        game[rowid+1][colid+i].remove(num)
        game[rowid+2][colid+i].remove(num)

def brutefill(game: list[list[cell]]) -> int:
    """Brute force method to check the cells with only 1 number allowed\n
    then set the cell to that number

    Returns:
        int: number of changes made
    """
    changednum = 0
    #global text
    for i in range(SUDOKUSIZE):
        for j in range(SUDOKUSIZE):
            if len(game[i][j].allowed) == 1:
                num = game[i][j].allowed[0]#get the only number
                print("found at", i,j,num)
                game[i][j].setnum(num)
                #text[i][j].set(num)
                changednum += 1
    return changednum

def singleallowedfill(game: list[list[cell]]) -> int:
    """Search for cases when a number only appear once in a row/column/block\n
    (as each row/column/block require a complete set of 1-9, a number appearing once in it means that
    it is the only place that it can be in even if that cell allow other numbers)

    Args:
        game (list[list[cell]]): gameboard to search

    Returns:
        int: number of changes made
    """
    changenum = 0
    countlist = []





def logicaldeduction(orginalgame: list[list[cell]]):
    """Performs a logical deduction on the game board in case when the brute force method falls
    the function will iterate over the allowed list of a cell, set the number to any one in the allow list,
    then attempts to find any contradiction in the game copy
    """
    print("no")


def findemptycell(game: list[list[cell]]) -> bool:
    """find if there is any cell in the gameboard that holds the number 0

    Args:
        game (list[list[cell]]): gameboard to search for 0

    Returns:
        bool: true on found, false on not found
    """
    for i in game:
        for j in i:
            if(j.number == 0):
                return True
    return False



def solve(game: list[list[cell]]):
    changenum = 0
    changenum += brutefill(game)
    changenum += singleallowedfill(game)
    

def reset():
    """Reset all cell in the game board to initial state with number 0
    """
    global text
    for i in range(SUDOKUSIZE):
        for j in range(SUDOKUSIZE):
            game[i][j] = cell(i,j)
            text[i][j].set("0")

def find():
    print("find")

def save():
    """make a copy of current game state, copy is stored internally
    will be lost when the program is closed
    """
    global savedgame
    savedgame = deepcopy(game)

def load():
    """load the game state from saved game
    """
    global game
    game = deepcopy(savedgame)
    for i in range(9):
        for j in range(9):
            text[i][j].set(game[i][j].number)

def change(row: int, col: int, w: Entry):
    global game, text
    """Changes the current holding value of the given cell to the given input

    Args:
        row (int): The row index of the target
        col (int): The column index of the target
        w (Entry): An Entry widget created by tkinter, holding the input text
        text (list[StringVar]): The text list holding the values of every cell
    """
    if(debugon):
        printcellinfo(row, col)
        return
    else:
        try:
            game[row][col].setnum(int(w.get()))
            text[row][col].set(w.get())
            w.select_range(0,END)
        except ValueError:
            print("ERROR: Input is not a integer or is empty")


def printcellinfo(row: int, col: int):
    """print infomation about cell

    Args:
        row (int): row index of target
        col (int): column index of target
    """
    game[row][col].printinfo()

def initialization():
    """
    initialize the game with 9x9 empty cell,\n
    The Cells are occupied by a "cell" object
    """
    global game
    for i in range(SUDOKUSIZE):
        game.append([])
        for j in range(SUDOKUSIZE):
            game[i].append(cell(i,j))

def debugswt():
    """
    toogle the debug state
    """
    global debugon
    debugon = not debugon
    print("INFO: debug is now: ", debugon)


def main():
    global text, game
    #Create & Configure root 
    root = Tk()
    root.resizable(False, False)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    #Create & Configure frame 
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    for i in range(SUDOKUSIZE):
        text.append([])
        for j in range(SUDOKUSIZE):
            text[i].append(StringVar())

    #other button
    Grid.columnconfigure(root, 10, weight=1)
    w = Entry(frame)
    w.grid(row=0, column=10)
    w.focus()

    #Create a 9x9 (rows x columns) grid of buttons (cells) inside the frame 
    #each button represent the number at that location
    #clicking the button would change the num to the given input of the input box
    for row_index in range(SUDOKUSIZE):
        Grid.rowconfigure(frame, row_index, weight=1)
        for col_index in range(SUDOKUSIZE):
            num = text[row_index][col_index]
            num.set(0)
            Grid.columnconfigure(frame, col_index, weight=1)
            btn = Button(frame) #create a button inside frame
            btn.img = PhotoImage() #override with empty image
            btn.config(height=50,width=50, image=btn.img, font=("Helvetica",'15'), compound=CENTER, textvariable=num, command=lambda i=row_index,j=col_index: change(i,j, w))
            x = y = 0

            #sperate each 3x3 block
            if((row_index+1)%3 == 0):
                y = 10
            if((col_index+1)%3 == 0):
                x = 10

            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W, padx=(0,x), pady=(0,y))


    #button to solve the sudoko
    cal = Button(frame,image=btn.img, height=50, width=80, text="Solve",compound=CENTER, command=partial(solve, game))
    cal.grid(row=1, column=10, pady=(0,10), padx=(0,10))

    #button to reset whole 9x9 board to 0
    resetbtn = Button(frame,image=btn.img, height=50, width=80, text="Reset",compound=CENTER, command=reset)
    resetbtn.grid(row=2, column=10,pady=(0,10), padx=(0,10))

    #button mainly for debuging use
    #click the button the remove all occupied cell's (cell that is not 0) number from its range of effect
    #i.e. if one cell is not 0, remove that number from all horizonal, vertical and block's cell's "allowed" list 
    #so that they are not allowed to be placed with the same number
    #(rule of sudoku, same number cant appear in the same row, column and block)
    findbtn = Button(frame,image=btn.img, height=50, width=80, text="Find",compound=CENTER, command=find)
    findbtn.grid(row=3,column=10,pady=(0,10), padx=(0,10))
    
    #save the whole game board interally, will be lost if program is closed, there is only ONE save slot, mainly for debug uses
    savebtn = Button(frame,image=btn.img, height=50, width=80, text="Save",compound=CENTER, command=save)
    savebtn.grid(row=4,column=10,pady=(0,10), padx=(0,10))

    #load the saved game board
    loadbtn = Button(frame,image=btn.img, height=50, width=80, text="Load",compound=CENTER, command=load)
    loadbtn.grid(row=5,column=10,pady=(0,10), padx=(0,10))

    #toggle debug state, changes the behaviour when clicking the cells
    debugbtn = Checkbutton(frame, text="debug", command= debugswt)
    debugbtn.grid(row=6, column=10)
    #cal.config(command=find)


    initialization()
    root.mainloop()



if __name__ == "__main__":
    main()