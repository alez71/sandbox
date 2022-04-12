mable = int(input("number of mable = "))
moves = []
prompt = "->"
enter = input(prompt)

while enter:
    moves.append(int(enter))
    enter = input(prompt)

print("allowed moves, ", moves)

grandy = [-1]

for i in range(mable):
    grandy.append(-1)


def game(mable):
    next = []
    for i in range(len(moves)):
        next.append(mable - moves[i])
    for i in next:
        if(i >= 0):
            game(i)
            if(mable == 0):
                grandy[mable] = 0
            temp = []
            for i in next:
                if(i > 0):
                    temp.append(grandy[i])
            k = 0
            while(True):
                if(temp.count(k) == 0):
                    grandy[mable] = k
                    break
                else:
                    k += 1

game(mable)

print(grandy)

z = input("enter to exit")