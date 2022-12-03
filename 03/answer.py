from string import ascii_letters as a

def partone():
    sum = 0

    with open('03/input') as f:
        for line in f:
            mid = int(len(line)/2)
            extra  = [x for x in line[:mid] if x in line[mid:]].pop()
            sum += a.index(extra) + 1

    print('1:', sum)

def parttwo():
    elf_grp = []
    badges = ''

    with open('03/input') as f:
        for line in f:
            elf_grp.append(line.strip())
            if len(elf_grp) == 3:
                badges += set(elf_grp[0]).intersection(*elf_grp[1:]).pop()
                elf_grp = []

    print('2:', sum([a.index(l) + 1 for l in badges]))

if __name__ == '__main__':
    partone()
    parttwo()