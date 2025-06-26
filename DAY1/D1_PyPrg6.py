# Ask the user toi enter ann integer
# Using a try-exceot bloack to handlke potential ValueError if non-integer
try:
    number = int(input("Please enter an integer: "))

    # Check if the number is positive, negative or zero
    if number > 0:
        print(f"The number {number} is positive.")
    elif number <0:
        print(f"The number {number} is negative.")
    else: # Thiscondition will be true if number is 0
        print(f"The number {number} is zero.")

except ValueError:
    print(f"Invalid input. Please enter a valid whole number.") 
