st = input("")

st_list = list(map(int,st.split()))

if st_list[0] > st_list[1]:
    print(">")
elif st_list[0] < st_list[1]:
    print("<")
else:
    print("==")