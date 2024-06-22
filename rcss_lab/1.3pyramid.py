n = int(input('Enter the value for n: '))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(' ', end='') 

    # Print numbers
    for k in range(1, 2 * i):
        print(i, end='')

    # Move to the next line
    print()
    
