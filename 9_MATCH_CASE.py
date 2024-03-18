# MATCH CASE STATEMENTS: 

# Python match statements were introduced in python 3.10 

day=int(input("Enter your no: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wendesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ : # _ is for defult case..       
        print("You enter invalid No of day.")