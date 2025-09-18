      


#simple program for arithematic operations

print("arithmetic operations")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice = int(input("enter your choice(1-4:)"))
a = int(input("enter first number:"))
b = int(input("enter second number:"))

if choice == 1:
    print("result=",a+b)
elif choice ==2:
    print(" result=",a-b)
elif choice ==3:
    print("result =",a*b)
elif choice ==4:
    if b !=0:
         print("result =",a/b)           
    else:
            print("error:division by zero")

else:
    print("invalid choice")       


    