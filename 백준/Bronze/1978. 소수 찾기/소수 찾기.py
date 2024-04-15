import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split()))

count_sosu = 0

for i in N_list:
    if i == 1:
        continue
    sosu = True
    for j in range(2,i):
        if i % j == 0:
            sosu = False
            break

    if sosu == True:
        count_sosu +=1
print(count_sosu)