'''PRINT THIS PATTEN :- 
                        1 1 1 1
                        2 2 2 2
                        3 3 3 3
                        4 4 4 4 
'''

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=1
    while(j<=n):
        print(i,end=" ")
        j=j+1
    print()
    i=i+1