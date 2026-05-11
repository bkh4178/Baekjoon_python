from itertools import permutations
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

def solution(numbers):
    answer = 0
    result = set()
    
    for r in range(1, len(numbers)+1):
        for p in permutations(numbers, r):
            result.add(int(''.join(p)))
    for num in result:
        if is_prime(num):
            answer += 1
    return answer