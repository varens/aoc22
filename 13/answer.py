import json
from functools import cmp_to_key

'''
int < int correct order
int > int incorrect
int == int continue

len([]) < len([]) correct
len([]) > len([]) incorrect
len([]) == len([]) continue

int => [int]
'''

def processinput(input_file: str) -> list[list]:
    packets = []
    for pair in open(input_file).read().split('\n\n'):
        packets.extend([json.loads(p) for p in pair.split('\n')])
    return packets

def isinorder(left, right):
    if type(left) == type(right) == int:
        if left == right: return
        return left < right

    if type(left) == type(right) == list:
        if len(left) == len(right) == 0: return
        if len(left) == 0: return True
        if len(right) == 0: return False
        for i in range(len(left)):
            if i > (len(right) - 1): return False
            if (ret := isinorder(left[i], right[i])) is not None: return ret
        if i < (len(right) - 1): return True
    
    if type(left) == int: return isinorder([left], right)
    if type(right) == int: return isinorder(left, [right])
    
def cmpwrap(a, b):
    cmp = isinorder(a, b)
    if cmp: return -1
    elif cmp is None: return 0
    else: return 1

if __name__ == '__main__':
    packets = processinput('13/input')
    isum = 0

    for i in range(0, len(packets), 2):
        if isinorder(packets[i], packets[i+1]):
            isum += int(i/2) + 1
    print('01: ', isum)

    packets.extend([[[2]], [[6]]])
    packets.sort(key=cmp_to_key(cmpwrap))
    print('02: ', (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
