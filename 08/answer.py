from functools import reduce

def main():
  grid = []

  with open('08/input') as f:
    for line in f:
      grid.append([int(x) for x in list(line)[:-1]])
      
  t_grid = list(zip(*grid))

  total = 0
  skipped = 0
  no_go = 0
  visible = 0
  maxscore = 0

  def getscore(x, y, t):
    scores = [0]*4 # up, right, down, left
    
    viewu = t_grid[y][:x][::-1]
    for tn in viewu:
      scores[0] += 1
      if tn >= t: break
      
    viewr = grid[x][y+1:]
    for tn in viewr:
      scores[1] += 1
      if tn >= t: break
      
    viewd = t_grid[y][x+1:]
    for tn in viewd:
      scores[2] += 1
      if tn >= t: break
      
    viewl = grid[x][:y][::-1]
    for tn in viewl:
      scores[3] += 1
      if tn >= t: break
      
    return reduce(lambda x, y: x*y, scores)

  for x in range(len(grid)):
    for y in range(len(t_grid)):
      if x == 0 or y == 0 or x == len(grid)-1 or y == len(t_grid)-1:
        visible += 1
        continue
      t = grid[x][y]
      
      if (score := getscore(x, y, t)) > maxscore:
        maxscore = score
      
      if t>max(grid[x][:y]) or t>max(grid[x][y+1:]) or t>max(t_grid[y][:x]) or t>max(t_grid[y][x+1:]):
        visible += 1
        continue
      skipped += 1
      
  print('1:', visible)
  print('2:', maxscore)

if __name__ == '__main__':
  main()