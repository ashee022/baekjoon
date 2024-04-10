import sys

N = int(sys.stdin.readline())
x_y_list =[]

for i in range(0,N):
    x,y = map(int ,sys.stdin.readline().split())
    x_y_list.append((x,y))


sorted_x_y_list = sorted(x_y_list)

for i in sorted_x_y_list:
    print(i[0],i[1])