"""

 Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
"""
"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""

Balance=int(input("Enter Balance:"))
annualInterestRate=float(input("Enter AnnualInterestRate"))
month=0
minFixedMonthlyRate=.19
while (month<12):
    previousBalance=Balance
    monthlyintRate= (annualInterestRate)/12.0
    minFixedMonthlyPayment=minFixedMonthlyRate * previousBalance
    monthlyUnpaidBalance=(previousBalance)-(minFixedMonthlyPayment)
    Balance=(monthlyUnpaidBalance)+(monthlyintRate*monthlyUnpaidBalance)

    month+=1
    
print ("Lowest Payment",Balance)