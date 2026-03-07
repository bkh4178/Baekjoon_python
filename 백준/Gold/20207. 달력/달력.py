import sys
input=sys.stdin.readline

n=int(input())
cal=[0]*366

for _ in range(n):
    s,e=map(int,input().split())
    for i in range(s,e+1):
        cal[i]+=1
        
total=0 # 총 직사각형 면적
width=0 # 가로
height=0 # 세로

for day in range(1,366):
    if cal[day]>0: #일정 있는 날
        width+=1
        height=max(height,cal[day])
        
    else: #일정 없는 날
        if width>0:
            total+=width*height
            
            #다음 구간을 위한 변수 초기화
            width=0 
            height=0 
            
total += width * height
print(total)