n=int(input("enter the number to check whether it is a prime or not :"))
for i in range(2,n):
    if n%i==0:
        print("it is not a prime number")
        break
else:
    print("it is a prime number")
    
