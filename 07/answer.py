import re

IDEAL = 30000000
TOTAL = 70000000

tree = {'': 0}

def process(stream):
  pwd = ''
  ls = False
  file_m = re.compile(r'(\d+)')
  for line in stream:
    if line.startswith('$ cd'):
      ls = False
      if line.endswith('..'):
        # add pwd total to parent
        parent = '/'.join(pwd.split('/')[:-1])
        tree[parent] += tree[pwd]
        pwd = parent
      else:
        pwd += '/' + line[5:]
    elif line.startswith('$ ls'):
      ls = True
      tree.setdefault(pwd, 0)
    elif ls:
      m = file_m.match(line)
      if m: tree[pwd] += int(m.group(1))

  while pwd != '':
    if pwd.find('/'):
      parent = '/'.join(pwd.split('/')[:-1])
      tree[parent] += tree[pwd]
      pwd = parent
    else:
      tree[''] += tree[pwd]
      pwd = ''

def main():
  input_stream = open('07/input').read().split('\n')
  process(input_stream)
  total = 0
  for size in tree.values():
    if size <= 100000:
      total += size
  print('1:', total)
  
  total_used = tree['']
  for size in sorted(tree.values()):
    if (TOTAL - total_used + size) >= IDEAL:
      print('2:', size)
      break

if __name__ == '__main__':
  main()