import sys

class Pair:
  s1 = ''
  s2 = ''

  def __init__(self, s1, s2):
    self.s1 = s1.rstrip()
    self.s2 = s2.rstrip()

  def LCS(self):
    X = self.s1
    Y = self.s2

    x = len(X)
    y = len(Y)

    b = [[0 for x in range(y + 1)] for x in range(x + 1)]
    c = [[0 for x in range(y + 2)] for x in range(x + 2)]

    for i in range(1, x + 1):
      for j in range(1, y + 1):
        if X[i-1] == Y[j-1]:
          c[i][j] = c[i-1][j-1] + 1
          b[i][j] = 'nw'
        elif c[i-1][j] >= c[i][j-1]:
          c[i][j] = c[i-1][j]
          b[i][j] = 'n'
        else:
          c[i][j] = c[i][j-1]
          b[i][j] = 'w'
    return b

  def print_LCS(self, b, X, i, j):
    if i == 0 or j == 0:
      return
    if b[i][j] == 'nw':
      self.print_LCS(b, X, i-1, j-1)
      print(X[i-1], end='')
    elif b[i][j] == 'n':
      self.print_LCS(b, X, i-1, j)
    else:
      self.print_LCS(b, X, i, j-1)

# Pairs
pairs = []

with open( sys.argv[1], 'r' ) as f:
  for line in f:
    line = line.split()
    pair = Pair( line[0], line[1] )
    pairs.append(pair)

for pair in pairs:
  pair.print_LCS( pair.LCS(), pair.s1, len(pair.s1), len(pair.s2) )
  print()