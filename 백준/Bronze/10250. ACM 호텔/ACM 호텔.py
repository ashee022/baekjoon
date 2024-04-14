import sys

T = int(sys.stdin.readline().strip())

for i in range(0,T):
    H,W,N = map(int,sys.stdin.readline().split())

    Hotel_list = []

    for i_W in range(1,W+1):
        for i_H in range(1, H+1):
            Hotel_list.append(i_H * 100 + i_W)

    print(Hotel_list[N - 1])