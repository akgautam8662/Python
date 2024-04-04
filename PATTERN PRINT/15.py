'''PRINT THIS PATTEN :- 
                        A B C D E 
                        A B C D E 
                        A B C D E 
                        A B C D E 
                        A B C D E
'''

n=int(input("Enter Number : "))

for i in range(n):
    for j in range(65,65+n):
        print(chr(j),end=" ")
    print()