m,n = map(int, input().split())


hang_a = []

for i in range(m):
    row_list_1 = list(map(int, input().split()))
    hang_a.append(row_list_1)

hang_b = []
for i in range(m):
    row_list_2 = list(map(int, input().split()))
    hang_b.append(row_list_2)

hang_plus = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(hang_a[i][j] + hang_b[i][j])
    hang_plus.append(row)

for k in hang_plus:
    print(" ".join(map(str,k)))

