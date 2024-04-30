import sys
input = sys.stdin.read

X = int(input().strip())

print(bin(X).count('1'))