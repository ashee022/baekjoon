import sys
import math

N = int(sys.stdin.readline().strip())
N_list = []

if int(N) % 2 == 1:
    for i in range(0,int(N)):
        C = int(sys.stdin.readline().strip())
        N_list.append(C)

N_list.sort()
print(round(sum(N_list) / len(N_list)))
print(N_list[math.floor(len(N_list)/2)])

N_dic = {}
for j in N_list:
    if j in N_dic:
        N_dic[j] += 1
    else:
        N_dic[j] = 1

max_c = max(N_dic.values())
maxs = []  
for num, freq in N_dic.items():
    if freq == max_c:
        maxs.append(num)

if len(maxs) > 1:
    maxs.sort()
    mode = maxs[1]
else:
    mode = maxs[0]

print(mode)
print(N_list[-1] - N_list[0])