n = int(input())
group_count = 0

for i in range(1,n+1):
    word = input()
    word_list = []
    is_group = True

    for char in word:
        if char not in word_list:
            word_list.append(char)
        elif char != word_list[-1]:
            is_group = False
            break
    if is_group:
        group_count += 1

print(group_count)
