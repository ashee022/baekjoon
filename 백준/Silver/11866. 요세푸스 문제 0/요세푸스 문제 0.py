N_and_K = input()
N, K = N_and_K.split()
n, k =int(N), int(K)

i_list =[]
for i in range(1,n+1):
    i_list.append(i)

yosea_list = []
index = 0
while len(i_list) > 0:
    index = (index + (k - 1)) % len(i_list)
    yosea_list.append(i_list.pop(index))

str_list = [str(item) for item in yosea_list]
formatted_str = "<" + ", ".join(str_list) + ">"
print(formatted_str)