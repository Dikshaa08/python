'''programs on decision making
1.write a program to accept choice from user and print result
s print sunday
m  print monday 
t print tuesday
w print wednesday
th print thursday
f print friday
sa print saturday
'''
#program to accept choice from user

choice = input("Enter choice (s, m, t, w, th, f, sa): ").lower()

if choice == "s":
    print("Sunday")
elif choice == "m":
    print("Monday")
elif choice == "t":
    print("Tuesday")
elif choice == "w":
    print("Wednesday")
elif choice == "th":
    print("Thursday")
elif choice == "f":
    print("Friday")
elif choice == "sa":
    print("Saturday")
else:
    print("Invalid choice!")

'''
2.write  a program to accept choice  from user and print result
1 print hi
2 print welcome
3 print bye
'''
# Program to accept choice from user and print result

choice = input("Enter choice (1, 2, 3): ")

if choice == "1":
    print("Hi")
elif choice == "2":
    print("Welcome")
elif choice == "3":
    print("Bye")
else:
    print("Invalid choice!")

'''
3.write a program to accept characters from user and print characters are in capital  or small letter
'''# Program to check if character is capital or small

ch = input("Enter a character: ")

if len(ch) == 1:   # ensure only one character is entered
    if ch.isupper():
        print("Character is in CAPITAL letter")
    elif ch.islower():
        print("Character is in small letter")
    else:
        print("It is not an alphabet")
else:
    print("Please enter only one character")



'''
4.write aq program to design  a app for movie ticket booking
a.first accept choice of seat(classic@ rs100 /preium @rs300/ recliner@ rs500)
b. accept number of seats
c.now according to amount provide offers
1. amount between 500 to 1500
offers include(choice of a meal worth rs200 or2%discount)
ii.amount more than 1500
offers include(choice of a meal worth rs500 or 4% discount)
'''
# Movie Ticket Booking App

print("----- Welcome to Movie Ticket Booking -----")
print("Seat Options:")
print("1. Classic @ Rs.100")
print("2. Premium @ Rs.300")
print("3. Recliner @ Rs.500")

# Accept seat choice
seat_choice = input("Enter seat type (classic/premium/recliner): ").lower()

# Assign price based on seat type
if seat_choice == "classic":
    price = 100
elif seat_choice == "premium":
    price = 300
elif seat_choice == "recliner":
    price = 500
else:
    print("Invalid seat type!")
    exit()

# Accept number of seats
num_seats = int(input("Enter number of seats: "))

# Calculate total amount
amount = price * num_seats
print(f"\nTotal Amount = Rs.{amount}")

# Provide offers based on amount
if 500 <= amount <= 1500:
    print("You are eligible for the following offers:")
    print("1. Choice of a meal worth Rs.200")
    print("2. 2% discount")
    offer = input("Enter your choice (meal/discount): ").lower()
    if offer == "discount":
        discount = amount * 0.02
        final_amount = amount - discount
        print(f"Discount applied! Final Amount = Rs.{final_amount:.2f}")
    else:
        print("Meal worth Rs.200 added to your booking!")
        print(f"Final Amount = Rs.{amount}")
elif amount > 1500:
    print("You are eligible for the following offers:")
    print("1. Choice of a meal worth Rs.500")
    print("2. 4% discount")
    offer = input("Enter your choice (meal/discount): ").lower()
    if offer == "discount":
        discount = amount * 0.04
        final_amount = amount - discount
        print(f"Discount applied! Final Amount = Rs.{final_amount:.2f}")
    else:
        print("Meal worth Rs.500 added to your booking!")
        print(f"Final Amount = Rs.{amount}")
else:
    print("No offers available for this amount.")
    print(f"Final Amount = Rs.{amount}")

    '''5. write a program to design a app for retail store, calculate final bill and discount on multiple brands according to the given choice 
    wooland - 20% discount
    levis - 30% discount
    vermoda - 35% discount
    us polo - 40% discount
    user can shop form multiple brands ,also with amount exceeding 5000,offer agift voucher of RS.500
   '''
    # Retail Store Billing App

def retail_store():
    print("Welcome to the Retail Store")
    print("Available Brands and Discounts:")
    print("1. Woodland - 20% off")
    print("2. Levis - 30% off")
    print("3. Vero Moda - 35% off")
    print("4. US Polo - 40% off")
    print("Enter '0' to finish shopping.\n")

    # Brand discount dictionary
    discounts = {
        "wooland": 20,
        "levis": 30,
        "vermoda": 35,
        "us polo": 40
    }

    total = 0  # Final bill
    while True:
        brand = input("Enter brand (woodland/levis/vermoda/us polo or 0 to exit): ").lower()
        if brand == "0":
            break
        if brand not in discounts:
            print("Invalid brand! Please try again.")
            continue

        try:
            amount = float(input(f"Enter purchase amount for {brand}: Rs. "))
        except ValueError:
            print("Invalid input. Enter a valid amount.")
            continue

        discount = discounts[brand]
        final_price = amount - (amount * discount / 100)
        print(f"Discounted price for {brand}: Rs. {final_price:.2f}\n")
        total += final_price

    print("="*40)
    print(f"Total Bill: Rs. {total:.2f}")
    if total > 5000:
        print("Congratulations! You get a Gift Voucher worth Rs. 500 ")
    print("Thank you for shopping with us!")

# Run the app
retail_store()

    
    
'''6. to qualify for a scholorship student have to go through three screening tests
    1.apttitude test
    2.coding test
    3.viva test
    eligibility depends on the given criteria
    student have to secure more than 95 marks in coding test,
    total of aptitude andviva should be more than 130,
    average marks are more than 180
    '''
# Scholarship Eligibility Program

def scholarship_check():
    print("=== Scholarship Eligibility Check ===")
    
    # Input marks
    aptitude = int(input("Enter marks in Aptitude Test: "))
    coding = int(input("Enter marks in Coding Test: "))
    viva = int(input("Enter marks in Viva Test: "))

    total = aptitude + coding + viva
    average = total / 3

    # Apply conditions
    if coding > 95 and (aptitude + viva) > 130 and average > 180:
        print("\n Congratulations! You are eligible for the scholarship.")
    else:
        print("\n Sorry, you are not eligible for the scholarship.")
    
    print(f"Your Total: {total}, Average: {average:.2f}")

# Run the function
scholarship_check()



'''7.write a program to
    '''
    