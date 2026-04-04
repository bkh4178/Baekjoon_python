import sys
input = sys.stdin.readline

def main():
    count = {}
    total = 0
    for line in sys.stdin:
        name = line.strip()
        if name not in count:
            count[name] = 1
        else:
            count[name] += 1
        total += 1

    for name in sorted(count.keys()):
        percent = count[name] / total * 100
        print(f"{name} {percent:.4f}")
if __name__ == "__main__":    main()