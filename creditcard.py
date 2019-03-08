""" # Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38

                
"""
balance=int(input("Enter Balance:"))
annualInterestRate=float(input("Enter the Annual Interest Rate"))
monthlyPaymentRate=float(input("Enter Monthly Payment Rate"))
month=0
while month<12:
    monPaymentRate= balance * monthlyPaymentRate
    unpaidBalance= balance - monPaymentRate
    interestRate=(annualInterestRate/12.0)*unpaidBalance
    nextMonthBalance=unpaidBalance+interestRate
    month+=1
    balance=nextMonthBalance
    
print ("Remaining Balance:",round(balance,2))
