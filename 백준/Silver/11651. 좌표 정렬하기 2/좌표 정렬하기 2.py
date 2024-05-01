import sys

N = int(sys.stdin.readline().strip())

X_Y_list = []
for i in range(N):
    X, Y = map(int,sys.stdin.readline().strip().split())
    X_Y_format = f"[x:{X} y:{Y}]"
    X_Y_list.append(X_Y_format)

X_Y_list.sort(key=lambda xy: (int(xy.split('y:')[1].rstrip(']')), int(xy.split('x:')[1].split(' ')[0])))

for i in X_Y_list:
    y = int(i.split('y:')[1].rstrip(']'))
    x = int(i.split('x:')[1].split(' ')[0])
    print(f"{x} {y}")