import sys
input = sys.stdin.readline
s = input().rstrip()
target = input().rstrip()

stack = []
m = len(target)
for c in s:
    stack.append(c)
    if len(stack) >= m and ''.join(stack[-m:]) == target:
        del stack[-m:]

result = ''.join(stack)
print(result if result else 'FRULA')