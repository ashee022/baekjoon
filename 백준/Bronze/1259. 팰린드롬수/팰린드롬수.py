import sys

while(True):
    N_list = []
    reverse_N_list = []
    N = sys.stdin.readline().strip()
    if N == '0':
        break
    if N == "":
        break
    for i in range(0,len(N)):
        N_list.append(N[i])
    for i in range(-1,-len(N)-1,-1):
        reverse_N_list.append(N[i])

    if N_list == reverse_N_list:
        print("yes")
    else:
        print("no")