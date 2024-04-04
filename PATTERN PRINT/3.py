'''PRINT THIS PATTEN :- 
                        ****
                        ***
                        **
                        * 
'''

n=int(input("Enter Number : "))

i=1
while(i<=n):
    j=n
    while(j>=i):
        print("*",end="")
        j=j-1
    print()
    i=i+1