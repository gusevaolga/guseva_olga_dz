import sys

def show_sales (start=0, end=0):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for i in range(start-1):
            f.readline()
        if end:
            for i in range(start-1, end):
                print(f.readline.strip())
        else:
            line = f.readline()
            while line:
                print(line.strip())
                line = f.readline()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        show_sales()
    elif len(sys.argv) == 2:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        show_sales(start, end)
    exit(0)
