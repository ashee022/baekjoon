def solution(nums):
    unique_count = len(set(nums))
    max_select = len(nums) // 2
    
    answer = min(unique_count, max_select)
    return answer
