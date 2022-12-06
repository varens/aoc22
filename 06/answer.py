import re

def main():
    
    f = open('06/input')
    
    m = re.search(r'(?:(\w)(?!\w{0,2}\1)){4}', f.read())
    print('1:', m.span()[0])

    f.seek(0)
    
    buff = ''
    while True:
        c = f.read(1)
        if not c: break
        j = buff.find(c)
        if j == -1:
            buff += c
            if len(buff) == 14:
                print('2:', f.tell())
                break
        else:
            buff = buff[j+1:] + c

if __name__ == '__main__':
    main()