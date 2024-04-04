'''PRINT THIS PATTEN :- 
                        4 3 2 1
                        4 3 2 1
                        4 3 2 1
                        4 3 2 1
'''     

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=1
    while(j<=n):
        print(n-j+1,end=" ")
        j=j+1
    print()
    i=i+1