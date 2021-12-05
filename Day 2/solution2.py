with open('data.txt', 'r') as DATAFILE:
  DATA = DATAFILE.read().splitlines()
  horizon = 0
  depth = 0
  aim = 0
  for x in range(len(DATA)):
    current = DATA[x]
    if(current[0] == "u"):
      aim -= int(current[-1])
    if(current[0] == "d"):
      aim += int(current[-1])
    if(current[0] == "f"):
      horizon += int(current[-1])
      depth += (aim * int(current[-1]))
      print("h: " + str(horizon))
      print("d: " + str(depth))
