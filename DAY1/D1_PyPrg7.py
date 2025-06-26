# Ranking your grades for input marks
try:
    number = int(input("Please enter your marks: "))

    # Check if the number is positive, negative or zero
    if number < 0 or number > 100:
        print(f"Your marks is {number} and it is invalid.")
    elif number < 35:
        print(f"Your marks is {number} and grade is D.")
    elif number < 50:
        print(f"Your marks is {number} and grade is C.")
    elif number < 70:
        print(f"Your marks is {number} and grade is B.")
    elif number < 90:
        print(f"Your marks is {number} and grade is A.")
    else: # Thiscondition will be true if number is 0
        print(f"Your marks is {number} and grade is A+.")

except ValueError:
    print(f"Input is invalid. Please enter a valid mark.")