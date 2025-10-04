#write a program that takes marks in physics,chemistry and math calculate total and
#  average admission criteria: average >=70 and each subject >=60 -"eligible for admission"
#  else if math >=90-"eligible under math special quota" else-"not eligible"
# Program to check admission eligibility based on marks

# Input marks
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
math = float(input("Enter marks in Math: "))

# Calculate total and average
total = physics + chemistry + math
average = total / 3

# Display total and average
print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")

# Check admission criteria
if average >= 70 and physics >= 60 and chemistry >= 60 and math >= 60:
    print("Status: Eligible for admission")
elif math >= 90:
    print("Status: Eligible under Math special quota")
else:
    print("Status: Not eligible")
