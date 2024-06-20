def calculate_bill(units):
    bill = 0
    
    # Calculate bill based on units consumed
    if units <= 200:
        bill = units * 0.5
    elif units <= 400:
        bill = (200 * 0.5) + ((units - 200) * 0.65)
    elif units <= 600:
        bill = (200 * 0.5) + (200 * 0.65) + ((units - 400) * 0.8)
    else:
        bill = (200 * 0.5) + (200 * 0.65) + (200 * 0.8) + ((units - 600) * 1.0)
    
    # Apply 15% surcharge if bill exceeds Rs. 400
    if bill > 400:
        bill += bill * 0.15
    
    # Ensure minimum bill of Rs. 100
    if bill < 100:
        bill = 100
    
    return bill

# Get number of units consumed from the user
units = float(input("Enter the number of units consumed: "))

# Calculate and print the electricity bill
bill = calculate_bill(units)
print(f"The electricity bill for {units} units is Rs. {bill:.2f}")