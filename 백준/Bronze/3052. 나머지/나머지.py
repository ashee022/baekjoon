import sys

divison_count_list = []

for i in range(10):
    N = int(sys.stdin.readline().strip())
    d_N = N % 42
    if d_N not in divison_count_list:
        divison_count_list.append(d_N)

print(len(divison_count_list))