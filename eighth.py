#employee salary slip generator
#write a program that accepts basic salary of an employee and calculate  the following:
#hra=20%of basic
#da = 10% of basic
#pf = 12% of basic
#gross_sal= basic+hra+da
#net_sal = gross-pf

basic = float(input("enter salary:"))

hra = 0.20*basic
da = 0.10*basic
pf = 0.12*basic
gross_sal = basic + hra + da
net_sal = gross_sal - pf

if net_sal >= 80000:
    cat = "high earner"
elif 50000 <= net_sal <80000:
    cat = "mid earner"
else:
    cat = "low earner"

print("your basic salary:",basic)
print("net salary :",net_sal)
print("category:",cat)