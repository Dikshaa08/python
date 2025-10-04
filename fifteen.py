#write a program that asks for product price and user type (regular,premium,vip) 
# discount rules: regular :<500-5%,>=500-10% premium:<1000-15% ,>=1000-20% vip: flat
#  20% discount always also apply extra 5% discount if payment mode ="online" finally 
# display the discounted price
# Input details
price = float(input("Enter product price: ₹"))
user_type = input("Enter user type (regular/premium/vip): ").lower()
payment_mode = input("Enter payment mode (online/offline): ").lower()

# Base discount calculation
discount = 0

if user_type == "regular":
    if price < 500:
        discount = 0.05
    else:
        discount = 0.10
elif user_type == "premium":
    if price < 1000:
        discount = 0.15
    else:
        discount = 0.20
elif user_type == "vip":
    discount = 0.20
else:
    print("Invalid user type.")
    exit()

# Extra discount for online payment
if payment_mode == "online":
    discount += 0.05

# Final price calculation
discounted_price = price * (1 - discount)

# Display result
print(f"\n🛍️ Final discounted price: ₹{discounted_price:.2f}")
