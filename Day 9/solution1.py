with open('C:/Users/Radek/Documents/Coding/Python/AdventOfCode2021/Day 9/test.txt', 'r') as DATAFILE:
    DATA = DATAFILE.read().splitlines()
    SDATA = []
    for x in range(len(DATA)):
        c = DATA[x]
        SDATA.append(list(c))

    #print(SDATA)

    index_up = True
    index_down = True
    index_left = True
    index_right = True

    low_points = []



    '''
    for i in range(len(DATA)):
        for j in range(len(DATA[0])):
            for k in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            #check DATA[i + k[0]][j + k[1]] and do operations and stuff to get the answer

    '''
    for y in range(len(SDATA)):
        for x in range(len(SDATA[y])):
            d = SDATA[y][x]
            try:
                if(y != 0 ):
                    d_up = SDATA[y - 1][x]
                else: 
                    d_up = SDATA[y][x]
            except IndexError:
                index_up = False
            
            try:
                d_down = SDATA[y + 1][x]
            except IndexError:
                index_down = False

            #gets elements from other side of list?!!!!!!!!!!!!!!!!!!!

            try:
                if(x != 0):
                    d_left = SDATA[y][x - 1]
                else:
                    d_left = SDATA[y][x]
            except IndexError:
                index_up = False

            try:
                d_right = SDATA[y][x + 1]
            except IndexError:
                index_up = False


            if(index_down == True and index_left == True and index_right == True and index_up == True):
                if(d <= d_down and d <= d_up and d <= d_left and d <= d_right):
                    low_points.append(d)
            
            if(index_down == False):
                if(d <= d_up and d <= d_left and d <= d_right):
                    low_points.append(d)
            
            if(index_up == False):
                if(d <= d_down and d <= d_left and d <= d_right):
                    low_points.append(d)

            if(index_left == False):
                if(d <= d_up and d <= d_down and d <= d_right):
                    low_points.append(d)

            if(index_right == False):
                if(d <= d_up and d <= d_left and d <= d_down):
                    low_points.append(d)


    
    print(low_points)