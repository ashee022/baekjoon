su_list =[]
for i in range(0,9):
    su = int(input())
    su_list.append(su)

print(max(su_list))
print(su_list.index(max(su_list))+1)
