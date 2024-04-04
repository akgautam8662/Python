'''PRINT THIS PATTEN :- 
                        1       
                        1 2     
                        1 2 3   
                        1 2 3 4 
'''

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=1
    count=1
    while(j<=i):
        print(count,end=" ")
        count=count+1
        j=j+1
    print()
    i=i+1
   