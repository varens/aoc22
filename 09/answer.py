def main(ropelen):
  coords = set()
  rope = [[0,0,0,0] for _ in range(ropelen)]
  
  f = open('09/input')
  for line in f:
    d, n = line.split(' ')
    # direction, head
    for _ in range(int(n)):
      # save previous
      rope[0][2], rope[0][3] = rope[0][0], rope[0][1]
      if d == 'R':
        rope[0][0] += 1
      elif d == 'L':
        rope[0][0] -= 1
      elif d == 'U':
        rope[0][1] += 1
      else:
        rope[0][1] -= 1
        
      # rope knots
      for j in range(1, len(rope)):
        # save previous
        # rope[j][2], rope[j][3] = rope[j][0], rope[j][1]
        # x_abs = abs(rope[j-1][0] - rope[j][0])
        # y_abs = abs(rope[j-1][1] - rope[j][1])
        # if (x_abs > 1 or y_abs > 1):
        #   rope[j][0] = rope[j-1][2]
        #   rope[j][1] = rope[j-1][3]

        if rope[j][1] > rope[j-1][1] + 1:
          rope[j][1] -= 1
          if rope[j][0] > rope[j-1][0]:
            rope[j][0] -= 1
          elif rope[j][0] < rope[j-1][0]:
            rope[j][0] += 1
        elif rope[j][1] < rope[j-1][1] - 1:
          rope[j][1] += 1
          if rope[j][0] > rope[j-1][0]:
            rope[j][0] -= 1
          elif rope[j][0] < rope[j-1][0]:
            rope[j][0] += 1
        elif rope[j][0] > rope[j-1][0] + 1:
          rope[j][0] -= 1
          if rope[j][1] > rope[j-1][1]:
            rope[j][1] -= 1
          elif rope[j][1] < rope[j-1][1]:
            rope[j][1] += 1
        elif rope[j][0] < rope[j-1][0] - 1:
          rope[j][0] += 1
          if rope[j][1] > rope[j-1][1]:
            rope[j][1] -= 1
          elif rope[j][1] < rope[j-1][1]:
            rope[j][1] += 1

      coords.add(f'{rope[-1][0]}{rope[-1][1]}')
  f.close()
  
  print(f'{int(ropelen/2%3)}:', len(coords))
  

if __name__ == '__main__':
  main(2)
  main(10)