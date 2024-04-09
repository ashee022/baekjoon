N = int(input())

def fac(i):
    if i <= 1:
        return 1
    else:
        return i * fac(i-1)

N_fac = str(fac(N))
zero_count = 0

for i in N_fac[::-1]:
    if int(i) == 0:
        zero_count += 1
    elif int(i) != 0:
        break

print(zero_count)