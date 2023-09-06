A,B = map(int, input().split())

#3,16

for i in range(A,B+1):
    if i < 2:
        continue
    flag = True
    for j in range(2,int(i**0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i)

