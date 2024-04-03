import sys
from collections import deque

N = int(sys.stdin.readline().strip())
que_list = deque()

for i in range(0,N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        que_list.append(int(command[1]))
    elif command[0] == "pop":
        if que_list:
            print(que_list.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que_list))
    elif command[0] == 'empty':
        print(0 if que_list else 1)
    elif command[0] == "front":
        print(que_list[0] if que_list else -1)
    elif command[0] == 'back':
        print(que_list[-1] if que_list else -1)
#효울성 문제 시관초과. sys을 이용해보자