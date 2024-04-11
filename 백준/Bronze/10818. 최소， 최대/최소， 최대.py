import sys

N = int(sys.stdin.readline().strip())

while True:
    N_list = list(map(int, sys.stdin.readline().strip().split()))

    if len(N_list) == N:
        break

S_N_list = sorted(N_list)
print(S_N_list[0], S_N_list[-1])