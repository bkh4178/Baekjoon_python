import sys
input = sys.stdin.readline

n = int(input())
a = n//3
if n%3 == 0:
    num_tr = 0
    for i in range(1, a):
        num_tr += (n-3*i)
    print(num_tr + 1)
else:
    num_tr = 0
    for i in range(1, a+1):
        num_tr += (n-3*i)
    print(num_tr)
    