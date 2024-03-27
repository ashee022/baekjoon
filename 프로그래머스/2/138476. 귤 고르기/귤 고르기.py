from collections import Counter

def solution(k, tangerine):
    t_dic = Counter(tangerine)
    sort_t_dic = dict(sorted(t_dic.items(), key = lambda item: item[1], 
                            reverse= 1))
    result = 0
    for key, value in sort_t_dic.items():
        if k <= 0:
            break
        if value <= k:
            k -= value
            result += 1  
        else:
            result += 1
            break
        
    answer = result
    return answer