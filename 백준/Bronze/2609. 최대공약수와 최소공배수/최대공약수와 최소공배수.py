import sys

input_data = sys.stdin.readline().strip()
N, M = map(int, input_data.split())

a, b = N, M
while b != 0:
    a, b = b, a % b
gcd_value = a

lcm_value = N * M // gcd_value

print(gcd_value)
print(lcm_value)
#유클리드 알고리즘 안쓰니, 성능테스트에서 안됨, 메모