#FizzBuzz
for num in range(1, 16):
    # if number is % by 3 and 5
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
#if number is % by 3
    elif num % 3 == 0: 
        print("Fizz")
# if number is % by 5
    elif num % 5 == 0:
        print("Buzz")
 #if number isn't then it prints the number
    else:
        print (num)

#Scholarship Eligibility Checker
GPA = 2.7
Credits = 50

if GPA >=3.5 and Credits >=60:
    print("TRUE")
elif GPA <= 3.5 and Credits <= 60:
    print("FALSE")

#Find the Maximum of Three Numbers
# Get input
num1 = 6
num2 = 1
num3 = 21

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print(largest)
