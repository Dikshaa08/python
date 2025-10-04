#To qualify for a scholarship student have to go through three....screening tests
#Aptitude test(marks out of 100)
#coding test(marks out of100)
#viva test(marks out of 50)
#eligibility depends on the given criteria student have to secure more than 95 marks in coding test.Total of aptitude and viva should
#be more than 130 ,average marks are more than 100
# Scholarship Eligibility Checker
# Scholarship Eligibility Checker

# Input marks
aptitude = int(input("Enter Aptitude Test marks (out of 100): "))
coding = int(input("Enter Coding Test marks (out of 100): "))
viva = int(input("Enter Viva Test marks (out of 50): "))

# Calculate total and average
total = aptitude + coding + viva
average = total / 3

# Check eligibility
if coding > 95 and (aptitude + viva) > 130 and average > 100:
    print("\n Congratulations! You are eligible for the scholarship.")
else:
    print("\n Sorry! You are not eligible for the scholarship.")

