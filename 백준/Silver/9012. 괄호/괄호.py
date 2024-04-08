N = int(input())

for _ in range(N):
    vps = input()
    balance = 0

    for v in vps:
        if v == "(":
            balance += 1
        elif v == ")":
            balance -= 1
        if balance < 0:
            print("NO")
            break

    else:
        if balance == 0:
            print("YES")
        else:
            print("NO")
