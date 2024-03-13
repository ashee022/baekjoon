def solution(number, limit, power):
    divisor_counts = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisor_counts[j] += 1
    
    total_weight = 0
    for count in divisor_counts[1:]:  
        if count > limit:
            total_weight += power
        else:
            total_weight += count
            
    return total_weight
