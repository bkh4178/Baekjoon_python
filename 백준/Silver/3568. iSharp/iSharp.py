import sys
input = sys.stdin.readline

def main():
    line = input().rstrip().rstrip(';')
    split_w = line.split()
    base = split_w[0]
    vars = split_w[1:]
    for v in vars:
        v = v.rstrip(',')
        name = ''
        extra = ''
        for c in v:
            if c.isalpha():
                name += c
            else:
                extra += c
        new_var = base
        i = len(extra)-1
        while i >= 0:
            if extra[i] == ']':
                new_var += '[]'
                i -= 2
            else:
                new_var += extra[i]
                i -= 1
        print(new_var, name, sep=' ', end=';\n')


if __name__ == "__main__":    main()