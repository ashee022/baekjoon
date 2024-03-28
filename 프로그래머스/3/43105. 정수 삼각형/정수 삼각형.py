def solution(triangle):
    tall = len(triangle)

    # 바텀업. 다이나믹 프로그래밍
    for i in range(tall-2, -1, -1):  # 바닥은 이미 계산할게 없기때문에 -2부터해야됨
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]
