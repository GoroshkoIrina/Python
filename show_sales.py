import sys

if __name__ == '__main__':
    with open('bakery.csv', 'r', encoding='utf-8') as f_bakery:
        if len(sys.argv) == 1:
            print("======= ALL Sales: =======")
            for line in f_bakery:
                print(line, end='')
        if len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
            print("======= Sales from #", sys.argv[1], " line: =======", sep='')
            i = 1
            for line in f_bakery:
                if i >= int(sys.argv[1]):
                    print(line, end='')
                i += 1
        if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit() and int(sys.argv[1]) > 0 and int(sys.argv[2]) > 0 and int(sys.argv[2]) > int(sys.argv[1]):
            print("======= Sales from #", sys.argv[1], " to #", sys.argv[2], " lines: =======", sep='')
            i = 1
            for line in f_bakery:
                if i >= int(sys.argv[1]) and i <= int(sys.argv[2]):
                    print(line, end='')
                i += 1
