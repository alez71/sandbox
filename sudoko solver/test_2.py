from tkinter import *
from copy import deepcopy

class Stored:
    def __init__(self) -> None:
        self.allowed = [1,2,3,4,5,6,7,8,9]

    def remove(self,value):
        try:
            self.allowed.remove(value)
        except ValueError:
            #print("value not in list")
            return

    def get(self):
        print(self.allowed)

    def report(self,x):
        return int(self.allowed.count(x))


debugon = FALSE

space = []
game = []
savedgame = []
def initiation():
    global game, space
#create intinal allowed board
    for i in range(9):
        space.append([])
        for j in range(9):
            space[i].append(Stored())
#Create inital grid
    game = [[0 for i in range(9)]for i in range(9)]

def reset():
    for i in range(9):
        for j in range(9):
            text[i][j].set(0)
            ##print(text[i][j].get())
    space.clear()
    game.clear
    initiation()

def save():
    global savedgame, game
    savedgame = deepcopy(game)


def load():
    global game, savedgame
    reset()
    game = deepcopy(savedgame)
    reflash()

def debug(row,col):
    space[row][col].get()
    print(game[row][col])

def debugswt():
    global debugon
    debugon = not debugon
    print(debugon)

#change display of buttons
def change(row,col):
    if debugon:
        debug(row,col)
        return
    else:
        k = game[row][col] = int(w.get())
        text[row][col].set(k)
        w.select_range(0,END)

def fillin():
    #block
    for q in range(9):
        #taget number
        for k in range(1,10):
            di = 0
            dj = 0
            sum = 0
            check = TRUE
            for i in range(3):
                for j in range(3):
                    sum += space[i+q//3*3][j+q%3*3].report(k)
                    # if q == 8 and k == 7:
                    #     print(k,"---",i+q//3*3,j+q%3*3,"---",sum)
                    if sum == 1 and check:
                        check = FALSE
                        di = i+q//3*3
                        dj = j+q%3*3
            if sum == 1:
                #print("blockcheck",di,dj,k)
                game[di][dj] = k
    for k in range(1,10):
        #horizontal check
        for i in range(9):
            #new row
            sum = di = dj = 0
            hcheck = TRUE
            for j in range(9):
                sum += space[i][j].report(k)
                # if k == 1:
                #     print(k,"---",i,j,"---",sum)
                if sum > 1:
                    pass
                elif sum == 1 and hcheck:
                    hcheck = FALSE
                    di = i
                    dj = j
            if sum == 1:
                #print("horcheck",di,dj,k)
                game[di][dj] = k
        #vertical check
        for j in range(9):
            sum = di = dj = 0
            vcheck = TRUE
            for i in range(9):
                sum += space[i][j].report(k)
                # if k == 1:
                #     print(k,"---",i,j,"---",sum)
                if sum > 1:
                    pass
                elif sum == 1 and vcheck:
                    vcheck = FALSE
                    di = i
                    dj = j
            if sum == 1:
                #print("vercheck",di,dj,k)
                game[di][dj] = k
                    



def blockremove(row,col,a):
    #print(a)
    for i in range(3):
        for j in range(3):
            #print(row+i,col+j)
            space[row//3*3+i][col//3*3+j].remove(a)


def reflash():
    for i in range(9):
        for j in range(9):
            k = game[i][j]
            text[i][j].set(k)


def cal():
    fillin()
    reflash()

def find():
    if any(0 in x for x in game):
        #remove blocked numbers
        a = 0
        for i in range(9):
            for j in range(9):
                if game[i][j] != 0:
                    a = game[i][j]
                    for k in range(1,10):
                        space[i][j].remove(k)
                        space[k-1][j].remove(a)
                        space[i][k-1].remove(a)
                        #print(i//3,j//3)
                    blockremove(i,j,a)
    else:
        return

# def test():
#     for i in range(9):
#         for j in range(9):
#             if game[i][j] == 0:
#                 save()
#                 for k in space[i][j]:
#                     game[i][j] = k
#                     try:
#                         cal()
#                     except



#Create & Configure root 
root = Tk()
root.resizable(False, False)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create 81 StringVar
text = []
for i in range(9):
    text.append([])
    for j in range(9):
        text[i].append(StringVar())
##print(text)
#Create a 9x9 (rows x columns) grid of buttons inside the frame

for row_index in range(9):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(9):
        num = text[row_index][col_index]
        num.set(0)
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame) #create a button inside frame
        btn.img = PhotoImage() #override with empty image
        btn.config(height=50,width=50, image=btn.img, font=("Helvetica",'15'), compound=CENTER, textvariable=num, command=lambda i=row_index,j=col_index: change(i,j))
        x = y = 0
        if((row_index+1)%3 == 0):
            y = 10
        if((col_index+1)%3 == 0):
            x = 10
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W, padx=(0,x), pady=(0,y))

#other button
Grid.columnconfigure(root, 10, weight=1)
w = Entry(frame)
w.grid(row=0, column=10)
w.focus()
cal = Button(frame,image=btn.img, height=50, width=80, text="Calculate",compound=CENTER, command=cal)
cal.grid(row=1, column=10, pady=(0,10), padx=(0,10))
resetbtn = Button(frame,image=btn.img, height=50, width=80, text="Reset",compound=CENTER, command=reset)
resetbtn.grid(row=2, column=10,pady=(0,10), padx=(0,10))
findbtn = Button(frame,image=btn.img, height=50, width=80, text="Find",compound=CENTER, command=find)
findbtn.grid(row=3,column=10,pady=(0,10), padx=(0,10))
savebtn = Button(frame,image=btn.img, height=50, width=80, text="Save",compound=CENTER, command=save)
savebtn.grid(row=4,column=10,pady=(0,10), padx=(0,10))
loadbtn = Button(frame,image=btn.img, height=50, width=80, text="Load",compound=CENTER, command=load)
loadbtn.grid(row=5,column=10,pady=(0,10), padx=(0,10))

debugbtn = Checkbutton(frame, text="debug", command= debugswt)
debugbtn.grid(row=6, column=10)
#cal.config(command=find)


initiation()
root.mainloop()

