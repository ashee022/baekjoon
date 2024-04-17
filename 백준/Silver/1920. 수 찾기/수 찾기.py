import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split()))

N_dict = {num: True for num in N_list}

M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().strip().split()))

outputs = []
for i in M_list:
    if i in N_dict:
        outputs.append('1')
    else:
        outputs.append('0')

print("\n".join(outputs))