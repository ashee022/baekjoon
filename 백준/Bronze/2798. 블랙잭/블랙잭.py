import sys
import itertools

N, M = map(int, sys.stdin.readline().strip().split())
N_list = list(map(int, sys.stdin.readline().strip().split()))

max_sum = 0
for card in itertools.combinations(N_list, 3):
    sums = sum(card)
    if sums <= M and sums > max_sum:
        max_sum = sums

print(max_sum)

#itertools를 잘쓰자... 삼중포문은 스레기다...