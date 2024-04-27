import sys

while(True):
    N, Y = map(int,sys.stdin.readline().split())
    if N > Y:
        print("Yes")
    elif N == 0 and Y == 0:
        break
    else:
        print("No")