''' 
EMI Caculator
formula = (loan_amount * rate_of_intrest * (rate_of_intrest + 1)**loan_period) / ((rate_of_intrest + 1)**loan_period) - 1
'''
import math

def emi_calculator(total_amount, intrest, time, down_payment = 0):

    loan_amount = total_amount - down_payment
    rate_of_intrest = intrest / (100 * 12)
    loan_period = time * 12
    
    amount_intrest = loan_amount * rate_of_intrest
    intrest_time = (rate_of_intrest + 1)**loan_period

    # Error-handling (Exception-handeling)
    try:
        emi = amount_intrest * (intrest_time/(intrest_time-1))
    except ZeroDivisionError:
        emi = loan_amount / loan_period

    emi = math.ceil(emi)
    return emi

amount = float(input("Please Enter Total Amount (With Downpayment if, any)= Rs. "))
rate = float(input("Please Enter Rate of Intrest per Annum.= "))
period = int(input("Loan Period in Years: "))
dp_confirm = (input("\nDid you pay any Downpayment (Yes/ No):")).upper()
if dp_confirm == "YES":
    downpayment = float(input("Please Enter Downpayment amount= Rs."))
else:
    downpayment = 0

emi = emi_calculator(amount,rate,period,downpayment)
print(f"\nYour Monthly EMI is = Rs.{emi}")

payble_amount = emi*period*12
payble_amount = math.ceil(payble_amount)

print(f"\nTotal Intrest is= Rs.{payble_amount-amount}")
print(f"You have to Pay Rs.{payble_amount} in Total")
