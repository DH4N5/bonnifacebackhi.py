n=int(input("Enter your number: "))
prime=True
for i in range(2,n):
    if(n%i==0):
        prime=False
        break

if(prime==True):
    print("Prime")
else:
    print("Composite")