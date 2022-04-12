mable = int(input("number"))
grandy = [-1]

for i in range(mable):
    grandy.append(-1)

def game(mable):
    if(mable>=0):
        game1 = game(mable-1)
        game4 = game(mable-4)
        print(game1,game4)
        if(mable == 0):
            t = input("check1")
            grandy[mable] = 0
            return 0
        if(grandy[game1] != -1 and grandy[game4] != -1):
            t = input("check2")
            temp = [int(grandy[game1]),int(grandy[game4])]
            #temp = [0,0]
            print(temp)
            t = input("check3")
            k = 0
            while(True):
                print(temp)
                t = input("check4")
                if(temp.count(k) == 0):
                    print(temp.count(k))
                    t = input("check5")
                    grandy[mable] = k
                    break
                else:
                    k += 1
            print(grandy)
            t = input("check6")
        return mable
    else:
        return 0    

game(mable)

print(grandy)
k = input("press enter to exit")