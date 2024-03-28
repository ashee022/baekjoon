def solution(phone_number):
    plist = list(phone_number)
    for i in range(len(plist)-4):
        plist[i] = '*'
        
    answer = ''.join(plist)
    return answer