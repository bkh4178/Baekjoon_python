import sys
import re
input = sys.stdin.readline

html_raw = input().rstrip()

div = re.findall(r'<div title="(.*?)">(.*?)</div>', html_raw)

for title, content in div :
    print(f'title : {title}')

    p = re.findall(r'<p>(.*?)</p>', content)
    for i in p :
        c = re.sub(r'<.*?>', '', i)
        c = re.sub(r'\s+', ' ', c)
        c = c.strip()
        print(c)