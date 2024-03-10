def solution(cards1, cards2, goal):
    index1, index2 = 0, 0
    for card in goal:
        if index1 < len(cards1) and cards1[index1] == card:
            index1 += 1
        elif index2 < len(cards2) and cards2[index2] == card:
            index2 += 1
        else:
            return 'No' 
    return 'Yes'  
