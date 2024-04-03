import sys

N = int(sys.stdin.readline().strip())
stack_list = []

for i in range(0,N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        stack_list.append(int(command[1]))
    elif command[0] == "pop":
        if stack_list:
            print(stack_list.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack_list))
    elif command[0] == 'empty':
        print(0 if stack_list else 1)
    elif command[0] == "top":
        print(stack_list[-1] if stack_list else -1)
#효울성 문제 시관초과. sys을 이용해보자