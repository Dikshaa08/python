#a city wants to implement a traffic fine system inputs: speed,vehicletype(car,bike,truck) 
# ,seatbelt(yes/no) ,helmet(yes/no) rules: speed>80-fine 2000 car without seat belt-
#  +1000fine bike without helmet-+1500fine truck speed >60 -+3000fine display: 
# "Total fine =." IF NO rules voilated -"No fine,drive safe"
# Input details
speed = int(input("Enter vehicle speed (km/h): "))
vehicle_type = input("Enter vehicle type (car/bike/truck): ").lower()
seatbelt = input("Seatbelt worn? (yes/no): ").lower()
helmet = input("Helmet worn? (yes/no): ").lower()

# Initialize fine
fine = 0

# Apply rules
if speed > 80:
    fine += 2000

if vehicle_type == "car" and seatbelt == "no":
    fine += 1000

if vehicle_type == "bike" and helmet == "no":
    fine += 1500

if vehicle_type == "truck" and speed > 60:
    fine += 3000

# Display result
if fine == 0:
    print("🚗 No fine, drive safe!")
else:
    print(f"💸 Total fine = ₹{fine}")
