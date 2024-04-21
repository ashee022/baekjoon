import sys
import math

N, M = map(int, sys.stdin.readline().strip().split())

print(math.factorial(N) // (math.factorial(M)*math.factorial(N-M)))
#성능테스트. 재귀 쓰지마라