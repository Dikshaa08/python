#write a program that accepts basic salary of an employee calculate the HRA= 20% of basic
#DA=10%Ofbasic PF= 12%of basic Gross salary=Basic+HRA+DA Netsalary= Gross-PF If netsalary
#>80000-category="high earner" if 50000<netsalary<80000-"midearner" else-"low earner"

basic_salary = float(input("Enter the basic salary of the employee: "))

# Calculate components
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
pf = 0.12 * basic_salary

# Calculate gross and net salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Determine earning category
if net_salary > 80000:
    category = "high earner"
elif 50000 < net_salary <= 80000:
    category = "mid earner"
else:
    category = "low earner"

# Display results
print(f"\nSalary Breakdown:")
print(f"Basic Salary: ₹{basic_salary:.2f}")
print(f"HRA (20%): ₹{hra:.2f}")
print(f"DA (10%): ₹{da:.2f}")
print(f"PF (12%): ₹{pf:.2f}")
print(f"Gross Salary: ₹{gross_salary:.2f}")
print(f"Net Salary: ₹{net_salary:.2f}")
print(f"Category: {category}")
