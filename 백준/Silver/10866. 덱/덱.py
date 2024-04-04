import sys
from collections import deque

N = int(sys.stdin.readline().strip())
deque_list = deque()

for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push_front":
        deque_list.appendleft(int(command[1]))
    elif command[0] == "push_back":
        deque_list.append(int(command[1]))

    elif command[0] == "pop_front":
        if deque_list:
            print(deque_list.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deque_list:
            print(deque_list.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(deque_list))
    elif command[0] == 'empty':
        print(0 if deque_list else 1)
    elif command[0] == "front":
        print(deque_list[0] if deque_list else -1)
    elif command[0] == 'back':
        print(deque_list[-1] if deque_list else -1)
