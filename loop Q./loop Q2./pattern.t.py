# i=0
# j=5
# while i<5:
#     print(" "*(i*2)+"* "*((j*2)-1))
#     i=i+1
#     j=j-1
# i=5
# j=0
# while i>0:
#     print(" "*(i*2)+"* "*((j*2)-1))
#     i=i-1
#     j+=1


i=0
while i<5:
    j=1
    while j<=i:
        print(' ',end="")
        j+=1
    k=4 
    while k>=i:
        print("*",end=''+' ')
        k-=1
    print()
    i=i+2
r=0
while r<5:
    space=5-r-1
    while space>0:
        print(end=" ")
        space=space-1
    n=r+1
    while n>0:
        print("*",end=" ")
        n=n-1
    r=r+2
    print()
    







        
