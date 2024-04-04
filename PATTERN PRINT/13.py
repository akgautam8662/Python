'''PRINT THIS PATTEN :- 
                        A B C D E 
                        F G H I J 
                        K L M N O 
                        P Q R S T 
                        U V W X Y 
'''

# n=int(input("Enter Number : "))
n=5
i=1
count=0
while(i<=n):
    j=1
    while(j<=n):
        print(chr(65 + count), end=" ")
        count=count+1
        j=j+1
    print()
    i=i+1