def main():
    total = [0]
    
    with open('input') as calories:
        for line in calories:
            if line == '\n':
                total.append(0)
                continue
            total[-1] += int(line)

    print('1:', max(total))
    print('2:', sum(sorted(total)[-3:]))

if __name__ == '__main__':
    main()