factorials = {}  # Dictionary to store factorials
 
def factorial(n):
    # Check if the factorial is already calculated and stored in the dictionary   
    if n in factorials:  
        return factorials[n]
  
    # Calculate the factorial if it's not in the dictionary 
    if n == 0: 
        result = 1
    else:
        result = n * factorial(n - 1) 

    # Store the calculated factorial in the dictionary
    factorials[n] = result

    return result

print(factorial(5))  # Output: 120
print(factorial(10))  # Output: 3628800
print(factorial(5))  # Output: 120 (retrieved from the dictionary)
