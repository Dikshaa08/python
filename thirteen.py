#create a program that checks loan eligibility input: age, monthly income,existing loan, 
# cibil score, conditions: age mustbe between 21-60,income must be >=25000 ,existing loan
# mustbe <=50% of income ,cibil score >=700 if all conditions are satisfied -"eligible for 
# loan" else display reason forrejection (eg-"Rejected due to low cibil score")
# Input details
age = int(input("Enter age: "))
monthly_income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))
cibil_score = int(input("Enter CIBIL score: "))

# Initialize rejection reasons
reasons = []

# Check conditions
if not (21 <= age <= 60):
    reasons.append("Rejected due to age not in eligible range (21-60)")

if monthly_income < 25000:
    reasons.append("Rejected due to low monthly income (< ₹25,000)")

if existing_loan > 0.5 * monthly_income:
    reasons.append("Rejected due to high existing loan (>50% of income)")

if cibil_score < 700:
    reasons.append("Rejected due to low CIBIL score (<700)")

# Final decision
if not reasons:
    print("✅ Eligible for loan")
else:
    print("❌ Not eligible for loan")
    for reason in reasons:
        print(f"- {reason}")
