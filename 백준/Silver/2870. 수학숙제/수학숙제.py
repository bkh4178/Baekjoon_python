import sys
input = sys.stdin.readline

def main():
    N = int(input())
    num_list = []
    for _ in range(N):
        word = input().rstrip()
        i=0
        while i < len(word):
            if word[i].isdigit():
                j = i
                while j < len(word) and word[j].isdigit():
                    j += 1
                num_list.append(int(word[i:j]))
                i = j
            else:
                i += 1
    num_list.sort()
    for num in num_list:
        print(num)

if __name__ == "__main__":    main()