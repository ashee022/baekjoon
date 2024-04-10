import sys

N = int(sys.stdin.readline().strip())
x_y_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_y_list.append((x, y))

ranking_list = [1 for i in range(N)]

for i in range(N):
    for j in range(N):
        if x_y_list[i][0] < x_y_list[j][0]:
            if x_y_list[i][1] < x_y_list[j][1]:
                ranking_list[i] += 1

for rank in ranking_list:
    print(rank, end=' ')
