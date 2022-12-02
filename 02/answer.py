def partone():
    outcome = {
        'AX':3,
        'AY':6,
        'AZ':0,
        'BX':0,
        'BY':3,
        'BZ':6,
        'CX':6,
        'CY':0,
        'CZ':3
    }
    shape = {
        'X':1,
        'Y':2,
        'Z':3
    }
    
    total = 0

    with open('02/input') as f:
        for line in f:
            oh, mh = line[0], line[2]
            total += outcome[oh+mh] + shape[mh]
            
    print('1:', total)
    
def parttwo():
    shape = {
        'AX':3,
        'AY':1,
        'AZ':2,
        'BX':1,
        'BY':2,
        'BZ':3,
        'CX':2,
        'CY':3,
        'CZ':1
    }
    outcome = {
        'X':0,
        'Y':3,
        'Z':6
    }

    total = 0

    with open('02/input') as f:
        for line in f:
            oh, mh = line[0], line[2]
            total += outcome[mh] + shape[oh+mh]
            
    print('2:', total)

if __name__ == '__main__':
    partone()
    parttwo()