def solution(s):
    s_list = []
    for char in s:
        if s_list and s_list[-1] == char:  
            s_list.pop()  
        else:
            s_list.append(char)  
    
    if not s_list:
        answer = 1
    else:
        answer = 0

    return answer
