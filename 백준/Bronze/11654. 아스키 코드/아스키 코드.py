import sys

N= sys.stdin.readline().strip()

if N == str(N):
    print(ord(N))

else:
    print(chr(N))