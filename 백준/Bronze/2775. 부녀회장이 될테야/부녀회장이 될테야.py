import sys
N = int(sys.stdin.readline().strip())

count = []

for _ in range(N):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    floor = list(range(n + 1))

    for i in range(k):
        for j in range(1, n + 1):
            floor[j] += floor[j - 1]

    count.append(floor[n])

for counts in count:
    print(counts)