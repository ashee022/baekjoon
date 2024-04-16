import sys
import heapq

N = int(sys.stdin.readline().strip())

N_list = []
abs_N_list= []

for i in range(0,N):
    N_c = int(sys.stdin.readline().strip())

    if N_c != 0:
        heapq.heappush(N_list, (abs(N_c),N_c))

    else:
        if N_list:
            abs_N, real_N = heapq.heappop(N_list)
            abs_N_list.append(str(real_N))
        else:
            abs_N_list.append('0')

print("\n".join(abs_N_list))
#heapq 쓰면 자동으로 오름차순되는듯