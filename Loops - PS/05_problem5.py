number = int(input("Enter a number: "))

if number <= 1:
    print("This is not a prime number!")
else:
    i = 2
    is_prime = True
    while i * i <= number:  # Check up to the square root of the number
        if number % i == 0:
            is_prime = False
            break
        i += 1  # Increment to check the next divisor
    
    if is_prime:
        print("This is a prime number!")
    else:
        print("This is not a prime number!")
