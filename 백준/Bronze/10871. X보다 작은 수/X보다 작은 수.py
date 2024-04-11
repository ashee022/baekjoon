import sys

N, X = map(int, sys.stdin.readline().strip().split())

i_list = list(map(int, sys.stdin.readline().strip().split()))

for i in i_list:
    if i < X:
        print(i, end=' ')