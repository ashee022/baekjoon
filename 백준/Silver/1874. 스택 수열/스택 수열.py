import sys

N = int(sys.stdin.readline().strip())
stack = []
result = []
s_number = 1

for _ in range(N):
    number = int(sys.stdin.readline().strip())

    while s_number <= number:
        stack.append(s_number)
        result.append("+")
        s_number += 1

    if stack[-1] == number:
        stack.pop()
        result.append("-")

    else:
        print("NO")
        sys.exit()

for i in result:
    print(i)