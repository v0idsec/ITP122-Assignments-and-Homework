# printing numbers 1-10 using while loop
print("printing numbers 1-10 using while loop") 

x = 0 

while x <= 10:
    print(x)
    x += 1

#Creating space in terminal    
print("\n"*3)

# printing first 10 even numbers using for loop 
print("printing first 10 even numbers using for loop ")

evens = [2,4,6,8,10,12,14,16,18,20]
for i in evens:
    print(i, sep=",")

#Creating space in terminal 
print("\n"*3)
    
# printing first 10 odd numbers using while loop 
print("printing first 10 odd numbers using while loop")
num = 1
while num <= 20: 
    if num % 2 != 0:
        print(num)
    num += 1

#Creating space in terminal 
print("\n"*3)


# Printing the sum of the first 10 numbers using a for loop
print("printing the sum of the first 10 numbers using a for loop")
total = 0 
for num in range(1, 11):
    total+= num
print("the sum of numbers 1 - 10 is", total)
