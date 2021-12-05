with open('Day 3/data.txt', 'r') as DATAFILE:
    DATA = DATAFILE.read().splitlines()
    DATA = list(map(str, DATA))

    oxygen = DATA
    co2 = DATA

    ones_count = 0
    zeros_count = 0

    
    for i in range(12):
        for x in range(len(DATA)):
            c = DATA[x]
            if(c[i] == '1'):
                ones_count = ones_count + 1
            if(c[i] == '0'):
                zeros_count = zeros_count + 1
        #print(i)
        if(ones_count > zeros_count):
            print("more ones")
            for index, element in enumerate(oxygen):
                #print(oxygen[index])
                oci = oxygen[index]
                if(oci[i] == '0'):
                    oxygen.pop(index)
                    print("element popped")
    
        if(ones_count < zeros_count):
            print("more zeros")
            for index, element in enumerate(oxygen):
                #print(oxygen[index])
                oci = oxygen[index]
                if(oci[i] == '1'):
                    oxygen.pop(index)
                    print("element popped")
        

print(oxygen)