with open('Day 1/data.txt', 'r') as DATAFILE:
  DATA = DATAFILE.read().splitlines()
  increase_count = 0
  for x in range(len(DATA)):
    if((int(DATA[x]) - int(DATA[x - 1])) > 0):
      increase_count = increase_count + 1
print("Increase count: " + str(increase_count))
