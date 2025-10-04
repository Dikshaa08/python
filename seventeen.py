  #inputs: age,movietype(2d/3d) ,day(weekday/weekend). rules: base price =200 ,if 3d = +100 ,
#  weekend=+50 , age<12 =50% discount , age>60=30% discount calculate and display final
#  ticket price

# Movie ticket price calculator

# Input details
age = int(input("Enter age: "))
movie_type = input("Enter movie type (2D/3D): ").strip().lower()
day = input("Enter day type (Weekday/Weekend): ").strip().lower()

# Base price
price = 200

# Add charges based on movie type and day
if movie_type == "3d":
    price += 100
if day == "weekend":
    price += 50

# Apply age-based discount
if age < 12:
    discount = 0.5  # 50% discount
elif age > 60:
    discount = 0.3  # 30% discount
else:
    discount = 0.0  # No discount

# Final price calculation
final_price = price * (1 - discount)

# Display result
print(f"\nFinal Ticket Price: ₹{final_price:.2f}")
