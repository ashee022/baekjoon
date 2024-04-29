import sys

M, N, H = map(int,sys.stdin.readline().strip().split())
days= (H - M) / (M - N)

if (H - M) % (M - N) != 0:
    days += 1

days +=1
print(int(days))