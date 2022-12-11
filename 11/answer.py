import re, math, operator
from functools import reduce

class Monkey:
    def __init__(self, items, op, next):
        self.items = items
        self.op = op
        self.next = next # ('div by?', if-true, if-false)
        self.activity = 0

    def catch(self, item):
        self.items.append(item)

    def inspect(self, chill_pill):
        while len(self.items):
            old = self.items.pop(0)
            self.activity += 1
            item = (eval(self.op)) % chill_pill \
                if chill_pill else math.floor(eval(self.op)/3)
            if item % self.next[0] == 0:
                yield (self.next[1], item)
            else:
                yield (self.next[2], item)

def main(part):
    monkeys = []
    si = re.compile(r'\d+')
    f = open('11/input').read()

    for monkey_raw in f.split('\n\n'):
        monkey_lines = monkey_raw.split('\n')
        items = [int(x) for x in si.findall(monkey_lines[1])]
        op = monkey_lines[2][19:]
        test = (int(monkey_lines[3].split()[-1]),
                int(monkey_lines[4].split()[-1]),
                int(monkey_lines[5].split()[-1]))
        monkeys.append(Monkey(items, op, test))

    monkey_activity = [0 for _ in range(len(monkeys))]
    chill_pill = reduce(operator.mul, [m.next[0] for m in monkeys]) \
        if part == 2 else 0
    rounds = 20 if part == 1 else 10000
    for _ in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for next_monkey, item in monkey.inspect(chill_pill):
                monkeys[next_monkey].catch(item)
            monkey_activity[i] = monkey.activity

    print('Part', part, reduce(operator.mul, sorted(monkey_activity)[-2:]))

if __name__ == '__main__':
    main(1)
    main(2)