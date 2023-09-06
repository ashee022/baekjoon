s = input().upper()
s_list = list(s)

s_dict = {}
for i in s_list:
    if i.isalpha():
        if i in s_dict:
            s_dict[i] = s_dict[i] + 1
        else:
            s_dict[i] = 1

s_maxs = max(s_dict,key=s_dict.get)
max_count = 0

max_su = s_dict[s_maxs]

for i in s_dict.values():
    if i == max_su:
        max_count = max_count + 1

if max_count > 1:
    print("?")
else:
    print(s_maxs)