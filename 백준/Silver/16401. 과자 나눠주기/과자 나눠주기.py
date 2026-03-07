import sys
input = sys.stdin.readline

def main():
    def s(arr, l):
        count = 0
        for snack in arr:
            count += snack//l
        return count
    
    M, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = 1, max(arr)
    result = 0

    while left <= right:
        mid = (left + right)//2
        if s(arr, mid) >= M:
            result = mid
            left = mid+1
        else: right = mid-1

    print(result)

        
if __name__ == '__main__':
    main()