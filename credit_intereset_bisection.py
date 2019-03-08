"""
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
""""""
balance=5000.00
annualInterestRate=0.18
monthlyPaymentRate=0.02


month=0
while month<12:
    monPaymentRate=balance*monthlyPaymentRate
    unpaidBalance=balance - monPaymentRate
    annualInterest=(annualInterestRate/12.0)*unpaidBalance
    nextMonthBalance=unpaidBalance+annualInterest
    month+=1
    balance=nextMonthBalance
    
#BALANCE=0277.41
#WHAT SHOULD BE THE FIXED MONTHLY PAYMENT
print ("Remaining Balance:",round(balance,2))
Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310  
#######

interestRate=0.18/12
monthlyUnpaidBalance = prevBalance - fixedMonthlyPay
updatedBalance =(monthlyUnpaidBalance) + (interestRate * monthlyUnpaidBalance)
print ("Lowest Payment: ",fixedMonthlyPay)
guess= (balance/10)
"""
balance=999999
annualInterestRate=0.18
interestRate=annualInterestRate/12
"""
balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
"""

def checkIt(fixedMonthlyPay):
    month=0
    ubalance=balance
    while (month<12):
        monthlyUnpaidBalance = ubalance - fixedMonthlyPay
        updatedBalance =(monthlyUnpaidBalance) + (interestRate * monthlyUnpaidBalance)
        ubalance=updatedBalance
        month+=1
    return updatedBalance

def doThese():  
    fixedMonthlyPay=10
    low=round(balance/12,2)
    upper=round((balance * (1+interestRate)**12)/12,2)
    fixedMonthlyPay=(low+upper)/2
    while abs(checkIt(fixedMonthlyPay))>=0.01:
        if checkIt(fixedMonthlyPay)>0.01:
            low=fixedMonthlyPay
        else:
            upper=fixedMonthlyPay
        fixedMonthlyPay=(low+upper)/2
    print ("Lowest Payment:",round(fixedMonthlyPay,2))
    
doThese()









