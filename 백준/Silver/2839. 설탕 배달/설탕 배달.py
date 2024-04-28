import sys

N = int(sys.stdin.readline().strip())

three_bong = 0
five_bong = N // 5

na_salt = N % 5

while five_bong >= 0:
    if na_salt % 3 == 0:
        three_bong = na_salt // 3
        print(five_bong + three_bong)
        break
    five_bong -= 1
    na_salt += 5

else:
    print(-1)