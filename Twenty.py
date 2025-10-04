#Inputs: distance, order_amount ,user_type(normal/gold/platinum) rules: base delivery= Rs50 if distance>5km -+rs10/km extra 
# freee delivery if order_amount>=1000 membership benefits: Gold- 20% discounton order platinum-30% discount on order normal - 
# no discount display final bill amount including delivery
def calculate_final_bill(distance, order_amount, user_type):
    # Apply membership discount
    if user_type.lower() == "gold":
        discount = 0.20
    elif user_type.lower() == "platinum":
        discount = 0.30
    else:
        discount = 0.0

    discounted_amount = order_amount * (1 - discount)

    # Calculate delivery fee
    if order_amount >= 1000:
        delivery_fee = 0
    else:
        delivery_fee = 50
        if distance > 5:
            delivery_fee += (distance - 5) * 10

    final_bill = discounted_amount + delivery_fee

    return f"Final Bill: ₹{final_bill:.2f} (Order: ₹{discounted_amount:.2f} + Delivery: ₹{delivery_fee:.2f})"
