import sys
input = sys.stdin.readline

S, T = map(int, input().split())
DNA = input().rstrip()
check = list(map(int, input().split()))
result = 0

s, e = 0, 0
count = [0] * 4
while e < S:
    if DNA[e] == 'A':
        count[0] +=1
    elif DNA[e] == 'C':
        count[1] += 1
    elif DNA[e] == 'G':
        count[2]+=1
    elif DNA[e] == 'T':
        count[3] += 1
        
    if e-s +1 == T:
        bul = True
        for i in range(4):
            if count[i] < check[i]:
                bul = False
                break
        if bul:
            result += 1
        if DNA[s]=='A':
            count[0] -= 1
        elif DNA[s] == 'C':
            count[1] -= 1
        elif DNA[s] == 'G':
            count[2] -= 1
        elif DNA[s] == 'T':
            count[3] -= 1
        s += 1
    e += 1
print(result)