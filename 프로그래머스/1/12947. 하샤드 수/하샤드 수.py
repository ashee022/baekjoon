def solution(x):
    original_x = x
    hasha_su = 0
    
    while x > 0:
        hasha = x%10
        hasha_su += hasha
        x = x // 10
        
    if original_x % hasha_su == 0:
        answer = True
    else:
        answer = False
    return answer