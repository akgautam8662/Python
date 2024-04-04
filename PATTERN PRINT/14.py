'''PRINT THIS PATTEN :- 
                        A A A A A 
                        B B B B B 
                        C C C C C 
                        D D D D D 
                        E E E E E 
'''
# while loop
n=int(input("Enter Number : "))

i=0
while(i<n):
    j=1
    while(j<=n):
        print(chr(65+i),end=" ")
        j=j+1
    print()
    i=i+1


# for loop
n=int(input("Enter Number : "))

for i in range(n):
    for j in range(n):
        print(chr(65+i),end=" ")
    print()