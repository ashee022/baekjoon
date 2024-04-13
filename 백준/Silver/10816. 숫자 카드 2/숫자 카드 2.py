import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
M_list = list(map(int,sys.stdin.readline().split()))

count_dict = {}
for number in N_list:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

results = []
for number in M_list:
    results.append(count_dict.get(number, 0))

print(' '.join(map(str, results)))