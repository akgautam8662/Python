'''PRINT THIS PATTEN :- 
                              A
                            A B
                          A B C
                        A B C D
                      A B C D E
'''

n=int(input("Enter Number : "))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(65+k),end=" ")
    print()