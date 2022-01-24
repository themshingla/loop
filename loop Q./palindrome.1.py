# n=int(input("enter the number"))
# pal=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if pal==rev:
#     print("is palidrome")
# else:
#     print("not palindrone")

i=1
sum=1
while i<=4:
    j=1
    while j<=i:
        print(sum,end='')
        sum=sum+1
        j=j+1
    i=i+1
    print()
    
