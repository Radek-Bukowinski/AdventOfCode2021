with open('Day 3/data.txt', 'r') as DATAFILE:
  DATA = DATAFILE.read().splitlines()
  DATA = list(map(str, DATA))
  ones_count = 0
  zeros_count = 0
  i = -1
  gamma = []
  epsilon = []

  def recursion(i):
    ones_count = 0
    zeros_count = 0
    for x in range(len(DATA)):
      current = DATA[x]
      try:
        if(current[i] == '1'):
          ones_count = ones_count + 1
        elif(current[i] == '0'):
          zeros_count = zeros_count + 1
      except:
        print(current, i)

    if(ones_count > zeros_count):
      #print('more ones')
      #print("1: " + str(ones_count))
      gamma.append('1')
      epsilon.append('0')
    if(ones_count < zeros_count):
      #print('more zeros')
      #print("0: " + str(zeros_count))
      gamma.append('0')
      epsilon.append('1')

for i in range(12):
  recursion(i)


gamma_str = ''.join(gamma)
epsilon_str = ''.join(epsilon)

gamma_bin = int(gamma_str, 2)
epsilon_bin = int(epsilon_str, 2)

result = gamma_bin * epsilon_bin

print(gamma)
print(epsilon)

print(gamma_str)
print(epsilon_str)

print(gamma_bin)
print(epsilon_bin)

print(result)
