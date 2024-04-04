
'''PRINT THIS PATTEN :- 
                       A
                       A B 
                       A B C
                       A B C D
                       A B C D E
                       A B C D
                       A B C
                       A B 
                       A 
 '''

n=int(input("Enter Number : "))

for i in range(n):
    for j in range(i+1):
            print(chr(j+65),end=" ")
    print()
for i in range(n):
    for j in range(n - i - 1):
        print(chr(65 + j), end=" ")
    print()