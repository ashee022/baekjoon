def win_team(N, team_list):
    max_from_left = [team_list[0]]
    for i in range(1, N):
        max_from_left.append(max(max_from_left[i-1], team_list[i]))
    
    max_from_right = [team_list[-1]]
    for i in range(N-2, -1, -1):
        max_from_right.append(max(max_from_right[-1], team_list[i]))
    max_from_right.reverse()
    
    win_red = 0
    win_blue = 0
    
    for i in range(N-1):
        red_strong = max_from_left[i]
        blue_strong = max_from_right[i+1]
    
        if red_strong > blue_strong:
            win_red += 1
        elif blue_strong > red_strong:
            win_blue += 1
        
    if win_red > win_blue:
        return "R"
    elif win_blue > win_red:
        return "B"
    else:
        return "X"
    

N = int(input())
team_list = list(map(int, input().split()))

winner = win_team(N,team_list)
print(winner)
