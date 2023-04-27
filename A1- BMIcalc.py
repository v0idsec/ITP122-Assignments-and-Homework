#BMI CALCULATOR

# first Ill create a nice greeting to greet the user
print("-"*55)
print("\tWelcome to the LoseWeightNow BMI calculator.")
print("-"*55)


# Here is where we will collect the user info to use for calculations and Display
FirstName = input("What is your first name? : ")
LastName = input("What is your last name? : ")
Age = int(input("How old are you? : "))
Weight = float(input("How much do you way in Kg? : "))
Height = float(input("How tall are you in meters? : "))

# Calculating BMI
# The formula to calculate BMI is 
# Weight in KG / Height in meters, squared, Formula in Python is below 

BMI = Weight / (Height ** 2)

# Now to print results back to user
# using 'f' before the string allows variables to be inserted in curly braces {}
# Also using the ':.1f' in the end of the string, we can keep the BMI value to one decimal place so we dont overwhelm the user

print(f"Weclome {FirstName} {LastName}, you are {Age} years old, and your BMI is {BMI:.1f}.")











# REFERENCES

# CDC - Calculating BMI using the metric system - BMI for Age Training Course - DNPAO. (2019, January 23). Www.cdc.gov. 
# https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the

# %.2f in Python – What does it Mean? (2022, June 22). FreeCodeCamp.org. 
# https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/#:~:text=In%20Python%2C%20there%20are%20various‌
