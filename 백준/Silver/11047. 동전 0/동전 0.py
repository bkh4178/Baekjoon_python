import sys
input = sys.stdin.readline

def main():
    N, cost = map(int, input().split())
    coin_list = []
    for i in range(N):
        coin_list.append(int(input()))
    coin_list.reverse()

    count = 0
    for coin in coin_list:
        count += cost//coin
        cost = cost%coin
    
    print(count)

if __name__ == '__main__':
    main()