n=int(input("Enter The Number:"))
for i in range (1,n+1):
    if i%2==0:
        print("E")
    elif i%2==1 and i%3==0:
        print("03")
    else:
        print(i)