# n=int(input("enter the number"))
# i=1
# while i>=5:
#     j=1
#     while j<=i:
#         print(" _",end=" ")
#         j=j+1
#     print()
#     i=i+1

#  k 1
#    2 1
#    3 2 1
#    4 3 2 1
#    5 4 3 2 1
   
i=1
while i<=5:
    j=0
    while j<i:
        print(i-j,end=" ")
        j=j+1
    i=i+1
    print()