# write a program to design a app for retail store,calculate final bill and discount on multiple brands according to thegiven choice
#woodland -20% discount
#Levis - 30% discount
#vermoda - 35% discount
#us polo- 40% discount               
# user can shop from mWultiple brands ,also with amount exceeding 5000, offer a gift voucher of Rs500
# Retail Store Billing App

# Brand discounts
brand_discounts = {
    "woodland": 0.20,
    "levis": 0.30,
    "vermoda": 0.35,
    "us polo": 0.40
}

# Store user's purchases
purchases = {}

print(" Welcome to the Retail Store App!")
print("Available brands and their discounts:")
for brand, discount in brand_discounts.items():
    print(f"- {brand.title()} : {int(discount * 100)}% off")

# Accept multiple brand purchases
while True:
    brand = input("\nEnter brand name (or type 'done' to finish): ").lower()
    if brand == "done":
        break
    if brand not in brand_discounts:
        print("❌ Invalid brand. Please choose from the listed brands.")
        continue
    try:
        amount = float(input(f"Enter purchase amount for {brand.title()}: ₹"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        purchases[brand] = purchases.get(brand, 0) + amount
    except ValueError:
        print("Please enter a valid amount.")

# Calculate final bill
total_original = 0
total_discounted = 0

print("\n🧾 Final Bill Summary:")
for brand, amount in purchases.items():
    discount = brand_discounts[brand]
    discounted_amount = amount * (1 - discount)
    print(f"- {brand.title()}: Original ₹{amount:.2f}, After {int(discount*100)}% discount: ₹{discounted_amount:.2f}")
    total_original += amount
    total_discounted += discounted_amount

print(f"\nTotal Original Amount: ₹{total_original:.2f}")
print(f" Total After Discounts: ₹{total_discounted:.2f}")

# Gift voucher condition
if total_discounted > 5000:
    print("Congratulations! You've earned a ₹500 gift voucher!")

print("\nThank you for shopping with us! 🛒")
