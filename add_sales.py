import sys

if __name__ == '__main__':
    with open('bakery.csv', 'a', encoding='utf-8') as f_bakery:
        f_bakery.write(sys.argv[1])
        f_bakery.write('\n')