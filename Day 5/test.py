with open("Day 5/data.txt", 'r') as f:
    d = f.read().splitlines()
    d = [[[int(x) for x in y.split(',')] for y in z.split(' -> ')] for z in d]

  #1#
  orthogonal = [x for x in d if (x[0][0] == x[1][0]) or (x[0][1] == x[1][1])]
  counts = np.zeros((np.amax(orthogonal)+1, np.amax(orthogonal)+1), int)

  for vent in orthogonal:
    x1, x2 = vent[0][0], vent[1][0]
    y1, y2 = vent[0][1], vent[1][1]
    if x1 == x2:
      change = abs(y1 - y2) + 1
      minimum = min(y1, y2)
      for i in range(minimum, minimum + change):
        counts[i][x1] += 1
    else:
      change = abs(x1 - x2) + 1
      minimum = min(x1, x2)
      for i in range(minimum, minimum + change):
        counts[y1][i] += 1

  danger = 0
  for row in counts:
    for count in row:
      if count > 1:
        danger += 1
  print(danger)