customer_name = input("Welcome, what is your name? ")
starting_balance = 5000.25

print (f"Hello {customer_name} you're starting balance is {starting_balance}")

pay_check = input("How much of your paycheck would you like to deposit? ")
expenditure_item = input("Looks like you went shopping. What did you buy? ")
expenditure = input("How much does a banjo cost: ")

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    ending_balance = balance + deposits - expense_amount
    print (f"good day,{user_name} after spending money on {expense_item} in the amount of {expense_amount} your current checking balance is: {ending_balance} ")