with open('data.txt', 'r') as DATAFILE:
  DATA = DATAFILE.read().splitlines()
  horizon = 0
  depth = 0
  for x in range(len(DATA)):
    current = DATA[x]
    if(current[0] == "u"):
      depth -= int(current[-1])
      print("d: " + str(depth))
    if(current[0] == "d"):
      depth += int(current[-1])
      print("d: " + str(depth))
    if(current[0] == "f"):
      horizon += int(current[-1])
      print("h: " + str(horizon))
