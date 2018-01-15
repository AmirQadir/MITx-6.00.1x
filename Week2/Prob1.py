

balance = int(input("Enter the current balance:"))
annualInterestRate = float(input("Enter the annualInterestRate"))
monthlyPaymentRate = float(input("monthlyPaymentRate"))

for i in range(12):
    mir = annualInterestRate / 12.0  # Monthly Interest Rate
    mmp = monthlyPaymentRate * balance  # Minimum Monthly Payment
    mub = balance - mmp  # Monthly unpaid balance
    ubem = mub + (mir * mub)  # Updated balnace each month
    balance = ubem

print("Remaining balance:", ("%.2f" % balance))

