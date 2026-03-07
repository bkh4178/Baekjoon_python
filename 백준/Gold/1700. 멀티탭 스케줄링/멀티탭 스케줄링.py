import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    plug = []
    off_count = 0
    for i in range(len(arr)):
        x = arr[i]
        if x in plug: continue
        elif len(plug) < N: plug.append(x)
        elif len(plug) == N:
            victim = None
            maximum = -1
            
            for p in plug:
                next = K+1
                for j in range(i+1, K):
                    if arr[j] == p:
                        next = j
                        break

                if next == K+1:
                    victim = p
                    break
                if next > maximum:
                    maximum = next
                    victim = p
            plug.remove(victim)
            plug.append(x)
            off_count += 1

    print(off_count)

if __name__ == '__main__':
    main()