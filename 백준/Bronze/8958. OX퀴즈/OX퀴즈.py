N = int(input())
OX_list = []
for i in range(1,N+1):
    OX = input()
    OX_list.append(OX)

for i_OX in OX_list:
    sum =0
    continues = 0
    for char in i_OX:
        if char == 'O':
            continues += 1
            sum += continues
        else:
            continues = 0
    print(sum)