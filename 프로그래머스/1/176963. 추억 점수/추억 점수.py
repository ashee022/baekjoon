def solution(name, yearning, photo):
    yearning_dict = dict(zip(name, yearning))
    
    scores = []
    
    for pic in photo:
        score = 0  
        for person in pic:
            score += yearning_dict.get(person, 0)
        scores.append(score)
    
    return scores
