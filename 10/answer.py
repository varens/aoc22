def main():
  exec = [1]
  with open('10/input') as inputfh:
    for inputline in inputfh:
      intsr = inputline.split()
      if len(intsr) > 1:
        exec.extend([int(intsr[1]), 0])
      else:
        exec.append(0)
  
  strengthsum = 0
  for cycle in range(20, 221, 40):
    strengthsum += sum(exec[0:cycle]) * cycle
  
  sprite = 0
  display = [str()] * 6
  for row in range(0, 240, 40):
    for pixel in range(40):
      sprite += exec[row + pixel - 1] if row+pixel < len(exec) else 0
      display[row // 40] += ['.', '#'][pixel in range(sprite-1, sprite+2)]
  
  print('1:', strengthsum)
  print('2:', *display, sep='\n')
  

if __name__ == '__main__':
  main()