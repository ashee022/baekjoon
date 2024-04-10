import sys

N = int(sys.stdin.readline().strip())
x_y_list = []

for _ in range(N):
    x, y = sys.stdin.readline().split()
    x_y_list.append((int(x), y))

for x, y in x_y_list:
    result = ''
    for char in y:
        result += char * x
    print(result)