while True: 
    n=int(input("Enter your amount: "))
    if n<=100:
         print("free")
    elif n>=101 and n<=500:
        x=n-100
        print(x*2.25)
    elif n>=501 and n<=1000:
        x=n-100
        print(x*5)
            