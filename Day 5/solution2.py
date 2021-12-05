import math

with open("Day 5/test.txt", "r") as DATAFILE:
    DATA = DATAFILE.read().splitlines()
    DATA = [[[int(x) for x in y.split(',')] for y in z.split(' -> ')] for z in DATA]
    straights = [x for x in DATA if (x[0][0] == x[1][0]) or (x[0][1] == x[1][1])]
    diagonals = [x for x in DATA if (x[0][0] != x[1][0]) and (x[0][1] != x[1][1])]

    grid = [[0 for x in range(0,10)] for y in range(0,10)]
    lowestx = []
    #print(grid)

    '''
    for x in range(len(straights)):
        
        #if line is horizontal, this passes
        deltax = math.dist([straights[x][1][0]] , [straights[x][0][0]])
        if(straights[x][1][0] > straights[x][0][0]):
            lowestx = straights[x][0][0]
            highestx = straights[x][1][0]
            difference = highestx - lowestx
            if(deltax > 0):
                for y in range(difference + 1):
                    grid[straights[x][0][1]][lowestx + y] += 1
                    #print(grid[lowestx + y][straights[x][0][0]])
        else:
            lowestx = straights[x][1][0]
            highestx = straights[x][0][0]
            difference = highestx - lowestx
            if(deltax > 0):
                for y in range(difference + 1):
                    grid[straights[x][1][1]][lowestx + y] += 1
                    #print(grid[lowestx + y][straights[x][1][0]])

        deltay = math.dist([straights[x][1][1]] , [straights[x][0][1]])
        if(straights[x][1][1] > straights[x][0][1]):
            lowestx = straights[x][0][1]
            highestx = straights[x][1][1]
            difference = highestx - lowestx
            if(deltay > 0):
                for y in range(difference + 1):
                    grid[lowestx + y][straights[x][0][0]] += 1
                    #print(grid[lowestx + y][straights[x][1][1]])
        else:
            lowestx = straights[x][1][1]
            highestx = straights[x][0][1]
            difference = highestx - lowestx
            if(deltay > 0):
                for y in range(difference + 1):
                    grid[lowestx + y][straights[x][1][0]] += 1
                    #print(grid[lowestx + y][straights[x][1][1]])

        '''
            #print("Horizontal Line: " + str(straights[x]))

       #
       #
       #
       #
       #
       #
       #
       #
       #
    
    for x in range(len(diagonals)):
        deltax2 = math.dist([diagonals[x][1][0]] , [diagonals[x][0][0]])
        if(diagonals[x][1][0] > diagonals[x][0][0]):
            lowestx = diagonals[x][0][0]
            highestx = diagonals[x][1][0]
            difference = highestx - lowestx

            lowesty = diagonals[x][0][1]
            highesty = diagonals[x][1][1]
            difference2 = highesty - lowesty

            if(deltax2 > 0):
                for q in range(difference + difference2):
                    for y in range(1):
                        for z in range(1):
                            grid[lowesty + (q - difference2)][lowestx + (q - difference)] += 1
                        #print(grid[lowestx + y][straights[x][0][0]])
        else:
            lowestx = straights[x][1][0]
            highestx = straights[x][0][0]

            lowesty = diagonals[x][1][1]
            highesty = diagonals[x][0][1]
            difference = highestx - lowestx

            difference2 = highesty - lowesty
            if(deltax2 > 0):
                for q in range(difference + difference2):
                    for y in range(1):
                        for z in range(1):
                            grid[lowesty + (q - difference2)][lowestx + (q - difference)] += 1
                    #print(grid[lowestx + y][straights[x][1][0]])

        

            #print("Vertical Line: " + str(straights[x]))

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if(grid[x][y] >= 2):
                count += 1
    print("Count: " + str(count))           

    #print(DATA[0][0][0]) #returns first element
    '''
    DATA[0][0][0]
    DATA[0] -> 2 coordinates
    DATA[0][0] -> 1 coordinate
    DATA[0][0][0/1] -> 1 x or y of coordinate
    '''
    #differenceX = math.dist([DATA[0][1][0]] , [DATA [0][0][0]])
    #differenceY = math.dist([DATA[0][1][1]] , [DATA [0][0][1]])
    #print(DATA[0][1][0])
    #print(DATA[0][0][0])
    #print(DATA[0][1][1])
    #print(DATA[0][0][1])
    #print(differenceX)
    #print(differenceY)

    '''
    print(straights)
    if (straights != diagonals):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print(diagonals)
    '''

    print(grid)