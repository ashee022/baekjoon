import sys

#N_list= list(map(int,sys.stdin.readline().strip().split()))

while True:
    a,b = map(int, sys.stdin.readline().strip().split())

    if a == 0:
        if b == 0:
           break
    print(a + b)