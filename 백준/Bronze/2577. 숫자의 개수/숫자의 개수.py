import sys
from collections import Counter

m_N = 1

for i in range(3):
    N = int(sys.stdin.readline().strip())
    m_N *= N

str_m_N = str(m_N)

count = Counter(str_m_N)

for i in range(10):
    print(count[str(i)])