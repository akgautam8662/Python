'''PRINT THIS PATTEN :- 
                        1 2 3 
                        4 5 6 
                        7 8 9
'''     

n=int(input("Enter Number : "))

i =1
count=1
while(i<=n):
    j=1
    while(j<=n):
        print(count,end=" ")
        count=count+1
        j=j+1
    print()
    i=i+1