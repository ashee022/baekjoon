def solution(A,B):
    A.sort()
    B.sort(reverse=1)

    sums = []
    for a, b in zip(A, B):
        ab_mul = a * b
        sums.append(ab_mul)
    
    answer = sum(sums)
    return answer