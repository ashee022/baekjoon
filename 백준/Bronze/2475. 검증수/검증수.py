st = input("")
st_list = list(map(int,st.split()))
Mst_list = list(map(lambda x : x**2,st_list))

print(sum(Mst_list)%10)


