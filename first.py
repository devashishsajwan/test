#check the number is prime or not by taking input from user
i=int(input("enter no"))
for z in range(2,i):
    if i%z==0:
        print("not prime")
        break
    else:
        print("prime")
        break
