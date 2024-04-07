from collections import deque

N_deque =deque()

N = int(input())
for i in range(1,N+1):
    N_deque.append(i)

while 1 < len(N_deque):
    N_deque.popleft()
    N_deque.append(N_deque.popleft())
print(N_deque[0])