import sys

N = int(sys.stdin.readline().strip())

for i in range(0,N):
    a, b = map(int,sys.stdin.readline().strip().split())
    print(a + b)