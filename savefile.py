ans=input("What is your next favorite color?")
with open("D:\\Python\\Python37-32\\st.txt","w") as st:
    st.write(ans)
with open("D:\\Python\\Python37-32\\st.txt","r") as st:
    print(st.read())
