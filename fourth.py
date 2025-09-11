#write a program to accept marks of 5 subjects from user calculate total, calculate percentage, print results pass or  fail on the basis of       percentage
num1 = int(input("enter 1st subject marks:"))
num2 = int (input("enter 2nd subject marks:"))
num3 = int(input("enter 3rd subject marks:"))
num4 = int(input("enter 4th subject marks:"))
num5 = int (input("enter 5th subject marks:"))

total = num1+num2+num3+num4+num5
per = total/5

if per>=50:
     print("pass")

else:
     print("fail")

