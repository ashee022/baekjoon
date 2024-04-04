import sys

N = int(sys.stdin.readline().strip())
name_list = []

for _ in range(N):
    age, names = sys.stdin.readline().strip().split()
    name_list.append((int(age),names))

name_list.sort(key=lambda x: x[0])
for age, names in name_list:
    print(age, names)