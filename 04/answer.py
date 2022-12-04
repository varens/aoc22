import re

def main():
    matches = [0, 0]
    r = re.compile('(\d+)-(\d+),(\d+)-(\d+)')

    with open('04/input') as f:
        for line in f:
            ids = [int(x) for x in r.match(line).groups()]
            if (ids[0] >= ids[2] and ids[1] <= ids[3]) \
            or (ids[2] >= ids[0] and ids[3] <= ids[1]):
                matches[0] += 1

            if (ids[2] <= ids[1] <= ids[3]) or (ids[0] <= ids[3] <= ids[1]):
                matches[1] += 1

    print('1:', matches[0])
    print('2:', matches[1])

if __name__ == '__main__':
    main()