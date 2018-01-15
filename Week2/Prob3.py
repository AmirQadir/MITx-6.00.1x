balance = int(input("Enter your balance"))
annualInterestRate = float(input("Enter your annualInterestRate"))

original = balance
monthlyInterestRate = (annualInterestRate) / 12
epsilon = 0.01
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
ans = (upperBound + lowerBound) / 2.0

while abs(0 - original) >= epsilon:
    original = balance

    for i in range(0, 12):
        original = round(((original - ans) * (1 + monthlyInterestRate)), 2)
    if original >= 0:
        lowerBound = ans
    else:
        upperBound = ans
    ans = (upperBound + lowerBound) / 2.0

print("Lowest Payment: " + str(round(ans, 2)))
