balance = int(input("Enter your balance"))
annualInterestRate = float(input("Enter the annualInterestRate "))


original = balance
monthlyPaymentRate = annualInterestRate / 12.0
update = 0
while (original > 0):
    original = balance
    update += 10
    for i in range(12):
        original = original - update
        original += original * monthlyPaymentRate

diff = original - balance

print("Lowest Payment:", (update))
