'''PRINT THIS PATTEN :- 
                        1 2 3 4
                        1 2 3 4
                        1 2 3 4
                        1 2 3 4
'''

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=1
    while(j<=n):
        print(j,end="  " ) 
        j=j+1
    print()
    i=i+1