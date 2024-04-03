N = int(input(""))
eng_list = []
for i in range(0,N):
    engs = input()
    eng_list.append(engs)

unique_eng_list = list(set(eng_list))
unique_eng_list.sort(key=lambda x: (len(x), x))

for eng in unique_eng_list:
    print(eng)