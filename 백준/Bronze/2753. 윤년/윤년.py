import sys

N = int(sys.stdin.readline().strip())

if int(N) % 4 == 0 and int(N) % 100 != 0:
    print("1")
elif int(N) % 400 == 0:
    print("1")
else:
    print("0")