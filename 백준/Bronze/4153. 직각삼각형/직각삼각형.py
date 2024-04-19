import sys

while(True):
    N_list = list(map(int,sys.stdin.readline().strip().split()))
    if N_list[0] == 0:
        break
    sorted_N_list = sorted(N_list)
    if (sorted_N_list[0] * sorted_N_list[0]) + (sorted_N_list[1] * sorted_N_list[1]) == sorted_N_list[2] * sorted_N_list[2] :
        print('right')
    else:
        print('wrong')
    N_list = []