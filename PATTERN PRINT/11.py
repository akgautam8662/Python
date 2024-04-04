'''PRINT THIS PATTEN :- 
                        1 
                        2 3 
                        3 4 5  
                        4 5 6 7 
'''

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=1
    value=i
    while(j<=i):
        print(value,end=" ")
        value=value+1
        j=j+1
    print()
    i=i+1