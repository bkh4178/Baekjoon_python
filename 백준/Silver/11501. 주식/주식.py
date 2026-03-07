import sys
input = sys.stdin.readline

def main(): 
    case_num = int(input())
    for _ in range(case_num):
        date = int(input())
        cost_list = list(map(int, input().split()))
        cost_list.reverse()
        benefit = 0
        max_stock = cost_list[0]
        for i in range(1, date):
            if cost_list[i] < max_stock:
                benefit += (max_stock - cost_list[i])
            elif cost_list[i] > max_stock:
                max_stock = cost_list[i]
        
        print(benefit)

if __name__ == '__main__':
    main()