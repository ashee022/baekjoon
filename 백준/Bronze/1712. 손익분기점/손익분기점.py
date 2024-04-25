import sys
A,B,C = map(int,sys.stdin.readline().strip().split())

if B >= C:
    print(-1)
else:
    count = A // (C - B) + 1
    print(count)