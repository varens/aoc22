import re, copy

def main():
    pre, post = open('05/input').read().split('\n\n')
    stacks = []

    stack_n = int(re.search('(\d+)\s+$', pre).group(1))
    stacks = [[] for _ in range(stack_n)]

    # populate the stacks
    for line in pre.split('\n'):
        i = 0
        while True:
            i = line.find('[', i)
            if i == -1: break
            stacks[int(i/4)].insert(0, line[i+1])
            i += 1

    stacks2 = copy.deepcopy(stacks)

    # move the crates
    m = re.compile('\D+(\d+)\D+(\d)\D+(\d)')
    for line in post.split('\n')[:-1]:
        n, f, t = [int(x) for x in m.match(line).groups()]
        stacks[t-1].extend(stacks[f-1][-n:][::-1])
        del stacks[f-1][-n:]

    print('1:', ''.join([x[-1] for x in stacks]))

    for line in post.split('\n')[:-1]:
        n, f, t = [int(x) for x in m.match(line).groups()]
        stacks2[t-1].extend(stacks2[f-1][-n:])
        del stacks2[f-1][-n:]

    print('2:', ''.join([x[-1] for x in stacks2]))

if __name__ == '__main__':
    main()