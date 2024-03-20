def solution(left, right):
    nums_list = []
    
    for i in range(left,right+1):
        num_list=[]
        for n in range(1,i+1):
            if i % n == 0:
                num_list.append(i)
        
        if len(num_list) % 2 == 0:
            nums_list.append(i)
        else:
            nums_list.append(-i)
                
    answer = sum(nums_list)
    return answer