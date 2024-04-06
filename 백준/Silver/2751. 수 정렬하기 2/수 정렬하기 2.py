import sys

N = int(sys.stdin.readline())
N_list = []

for _ in range(N):
    N_c = int(sys.stdin.readline())
    N_list.append(N_c)

N_list_sorted = sorted(N_list)

for i in N_list_sorted:
    print(i)
