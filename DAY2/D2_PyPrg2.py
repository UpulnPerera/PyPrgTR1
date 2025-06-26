# This script demostrates how to handle ValueError
try:
    numerator_input = input("Please enter the numerator: ")
    numerator = float(numerator_input) # Use float to allow for decide

    denominator_input =  input("Please enter the enominator: ")
    denominator = float(denominator_input) # Use float to allow for decide

    result = numerator / denominator

    print("You entered: Numerator {numerator}, Denominator = {denominator}")
    print(f"The result of the division is: {result}")

except ValueError:
    print("Invalid input. Pleae enter valid numbers for both numerator and denominator")
except ZeroDivisionError:
    print("Cannot divid by zero")
except Exception as e:
    # Cartch any other unexpected errors
    print(f"an unexpected error occured {e}")
