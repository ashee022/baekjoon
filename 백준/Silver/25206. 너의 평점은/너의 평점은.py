hakjun_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
    'P': 0.0
}
#입력은 과목, 3.0(스코어) , b(학점)
total_hakjun = 0 #학점의 총합
total_score = 0 #학점 * 과목평점

for i in range(0,20):
    subject,score,hakjun = input().split()
    score = float(score)

    if hakjun != 'P':
        total_score = total_score + score * hakjun_dict[hakjun]
        total_hakjun = score + total_hakjun
print(total_score/total_hakjun)
