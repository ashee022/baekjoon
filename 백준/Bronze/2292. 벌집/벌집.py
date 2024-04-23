import sys

count = 1
N = int(sys.stdin.readline().strip())

room = 1
while(N > room):
    room = room + (6*count)
    count +=1
print(count)