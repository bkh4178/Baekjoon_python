import sys
input = sys.stdin.readline
import bisect

def main():
    
    N = int(input())
    arr = list(map(int, input().split()))

    ordered_mat = []
    for num in arr:
        k = len(ordered_mat)
        if k == 0:
            ordered_mat.append(num)
        elif ordered_mat[k-1] >= num :
            idx = bisect.bisect_left(ordered_mat, num)
            ordered_mat[idx] = num
        else :
            ordered_mat.append(num)
    
    print(len(ordered_mat))

if __name__ == '__main__':
    main()