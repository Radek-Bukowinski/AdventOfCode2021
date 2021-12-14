with open('C:/Users/Radek/Documents/Coding/Python/AdventOfCode2021/Day 8/data.txt', 'r') as DATAFILE:
    count = 0
    DATA = []

    tc = 0

    letters = []

    '''
    for line in DATAFILE:
        count += 1
        if count % 2 == 0:
            DATA.append(line)
    '''

    for line in DATAFILE:
        ps = line.partition("|")
        DATA.append(ps[2])
        


    DATA = [s.replace("\n", "") for s in DATA]
    DATA = [q.split() for q in DATA]
    DATA = [j for sub in DATA for j in sub]

    for x in range(len(DATA)):
        for char in DATA[x]:
            letters.append(char)
        
        if(len(letters) == 2 or len(letters) == 4 or len(letters) == 3 or len(letters) == 7):
            tc += 1

        letters.clear() 

    print(tc)            

    