
# This learning activity requires you to read the problem, and design and implement the solution using Python. 
# Add comments to your code to explain the purpose of different statements. Submit your code/output screenshots to the discussion forum.

# Each year, nearly everyone with an income faces the unpleasant task of computing their income tax return. 
# Assume you are working as software developer in a medium-sized business, 
# and your manager has asked you to implement an income tax calculator program with the following requirements.

# All taxpayers are charged a flat tax rate of 25%.
# All taxpayers are allowed a $18,500 standard deduction.
# For each dependent, a taxpayer is allowed an additional $1,200 deduction.
# Gross income must be entered to the smallest penny.
# Income tax is expressed as a decimal number with three decimal places.
# In this case, the user inputs are gross income and the number of dependents. The program calculates the income tax based on the inputs and tax law, and then displays the income tax.


# Prompt usr for gross income and the amount of dependants 

Gross = float(input("Enter your Gross Income: $"))
Dep = int(input("Enter the number of dependants: "))

# Calculate taxable income by subracting deductions 
TaxInc = Gross - 18500 - (Dep * 1200)

# Calculating the Income Tax by multiplying taxable income by rate
IncomeTax = round(TaxInc * 0.25, 3)


# Display income tax back to the user
print("Your income tax is $", (IncomeTax))
