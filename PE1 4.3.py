def calculate_interest(principal, rate, time):
    
    #Calculates simple interest.
    return (principal * rate * time)

def compound_interest(principal, rate, times_per_year, time):

    #Calculates compound interest.
    amount = principal * (1 + (rate / times_per_year)) ** (times_per_year * time)
    return round(amount - principal, 2)  # Round to 2 decimal places

# Example Test Cases
print(calculate_interest(1000, 0.05, 2))  # Output: 100
print(calculate_interest(10000, 0.03, 25))  # Output: 7500

print(compound_interest(1000, 0.05, 4, 10))  # Output: 643.62
print(compound_interest(10000, 0.07, 4, 25))  # Output: 46681.56
