employeeName = str(input("Enter name: "))
numberShift = float(input("Enter number of shifts: "))
numberTransaction = float(input("Enter number of transactions: "))
transactionValue = float(input("Enter Value of transactions: "))
employeeBonus = 0.00
productivityScore = transactionValue / numberTransaction /numberShift


if productivityScore <= 30:
    employeeBonus = 50.00
else:
    if 31 <= productivityScore <= 69:  
        employeeBonus = 75.00
    else:
        if 70 <= productivityScore <= 199:  
            employeeBonus = 100.00
        else:
            if productivityScore >= 200:  
                employeeBonus = 200.00

print("Employee Name: " + employeeName)
print ("Employee Bonus: $"+str(employeeBonus))