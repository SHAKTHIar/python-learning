attempt=0
while attempt <3:
    n=input("Do you agree(Yes/No):")
    if n=="yes":
        print("Yes Finally You agreed ;)")
        break
    attempt+=1
else:
    print("Your 3 strike are over :|")