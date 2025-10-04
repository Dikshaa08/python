#Inputs: account_balance,amount_to_withdraw ,account_type(saving/current),day(weekend/weekday). rules: withdrawal allowed
#  only if balance>=withdrawal +1000(min. balance) weekend transactions charge extra rs.50 fee saving account daily limit = 25000 
# : current amount= 50000 output: success/failure with reason and updated balance
def process_withdrawal(account_balance, amount_to_withdraw, account_type, day):
    fee = 50 if day.lower() == "weekend" else 0
    total_deduction = amount_to_withdraw + fee
    min_balance_required = 1000

    # Check daily limit
    if account_type.lower() == "saving" and amount_to_withdraw > 25000:
        return "Failure: Exceeds daily limit for saving account", account_balance
    if account_type.lower() == "current" and amount_to_withdraw > 50000:
        return "Failure: Exceeds daily limit for current account", account_balance

    # Check balance sufficiency
    if account_balance < total_deduction + min_balance_required:
        return "Failure: Insufficient balance after maintaining minimum ₹1000", account_balance

    # Successful transaction
    updated_balance = account_balance - total_deduction
    return "Success: Withdrawal processed", updated_balance
