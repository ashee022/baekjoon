import sys

N= sys.stdin.readline().strip()

for i in range(0,int(N)):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(int(a) + int(b))