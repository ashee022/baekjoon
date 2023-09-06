num = int(input())
scores = list(map(int, input().split()))  

max_score = max(scores)
new_sum = 0

for score in scores:
    new_sum += score / max_score * 100

new_avg = new_sum / num
print(new_avg)