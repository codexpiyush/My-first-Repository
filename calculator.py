def add(num1,num2):
    return (num1+num2)
def sub(num1,num2):
    if num1>num2:
        return (num1-num2)
    else:
        return (num2-num1)
def mul(num1,num2):
    return (num1*num2)
def div(num1,num2):
    return (num1//num2)
def avg(num1,num2):
    return ((num1+num2)/2)

opp=input("enter yes to do calculation : ")
opp1=opp.upper()
if (opp1=="YES"):
    while (opp1=="YES"):
        number1=int(input("please enter the number 1 "))
        number2=int(input("please enter the number 2 "))
        print("Please enter your choice : \n"
                "1. Addition\n"
                "2. Substraction\n"
                "3. Multiplication\n"
                "4. division\n"
                "5. Average\n")
        select=int(input("")) 
        if select ==1:
                print("the sum of numbers is : ",add(number1,number2))
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
        elif select==2:
                print("the substraction of numbers is :",sub(number1,number2))
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
        elif select==3:
                print("the multiplication of numbers is :",mul(number1,number2))
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
        elif select==4:
                print("the division of numbers is :",div(number1,number2))
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
        elif select==5:
                print("the average of numbers is :",avg(number1,number2))
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
        else:
                print("You have entered wrong number")
                opp1=input("Do you want to do more calculation please enter yes otherwise no : ").upper()
else:
      print("you have entered something wrong")