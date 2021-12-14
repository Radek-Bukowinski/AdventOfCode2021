with open("Day 6/data.txt", "r") as DATAFILE:
  for line in DATAFILE:
    DATA = line.split(',')
  
  DATA = [int(DATA[x]) for x in range(len(DATA))]

  totals = [0 for x in range(9)]

  for element in DATA:
    totals[element] += 1

  for x in range(256):
    totals[7] += totals[0] 
    totals = totals[1:] + totals[:1]

  print(sum(totals))