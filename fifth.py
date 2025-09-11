#program to accept price of 10 different items from user, caculate total amount

item1 = int(input("enter 1st items price :"))
item2 = int(input("enter 2nd items price :"))
item3 = int(input("enter 3rd items price :"))
item4 = int(input("enter 4th items price :"))
item5 = int(input("enter 5th items price :"))
item6 = int(input("enter 6th items price :"))
item7 = int(input("enter 7th items price :"))
item8 = int(input("enter 8th items price :"))
item9 = int(input("enter 9th items price :"))
item10 = int(input("enter 10th items price :"))

total = item1+item2+item3+item4+item5+item6+item7+item8+item9+item10

if total>2000:
    dis = total*20/100
    total = total - dis
    print("total amount of 10 items:",total)
else:
    print("total amount of 10items :",total)
