#loan eligibility system

age =int(input("enter age:"))
income = int(input("enter income :"))
loan = int(input("enter loan:"))
cibil = int(input("enter cibl:"))

if not (21<=age <= 60):
    reason = "rejected due to low age!!"
elif income <25000:
    reason = "rejected due to low income!!"
elif loan> 0.5:
    reason = "rejected due to low criteria!!"
elif cibil <700:
    reason = "rejected due to low cibil score!!"
else:
   reason = "accepted!!"

print(reason)