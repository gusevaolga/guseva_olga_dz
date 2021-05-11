import sys

def add_sale (price):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{price}\п')


if __name__ == "__main__":
    if sys.argv == 2:
        add_sale(sys.argv[1])
    exit(0)


