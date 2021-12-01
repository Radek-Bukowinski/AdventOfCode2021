with open('Day 1/data.txt', 'r') as DATAFILE:
  DATA = DATAFILE.read().splitlines()
  increase_count = 0
  for x in range(len(DATA)):
    if (len(DATA) - x) > 3:
      if((int(DATA[x + 3]) - int(DATA[x])) > 0):
        increase_count += 1
  print(increase_count)
