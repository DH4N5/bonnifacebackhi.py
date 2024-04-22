a=input("what is the first number:  ")
b=input("what is the second number: ")
c=input("what is the operation\n 1=add\n 2=sub\n 3=div\n 4=multiply\n give only number:")
a=float(a)
b=float(b)
c=int(c)
if c==1:
 addition= a+b
 print("add =",addition)
elif c==2:
 sub=a-b
 print("sub =",sub)
elif c==3:
 divide=a/b
 print("divide =",divide)
elif c==4:
 multiply=a*b
 print("multiply =",multiply)
 