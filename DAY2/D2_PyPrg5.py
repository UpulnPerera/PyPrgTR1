class NegativeNumberError(ValueError):
    """Custom exception raised when a negative number is entered"""
    def returnerror(ValueError):
        print(ValueError)

def get_positive_number():
    """
    Asks the user for a number and raises a NegativeNumberError if
    """
    while True:
        try:
            num_str = input("Pleae enter a positive number: ")
            number = float(num_str) # Use float to allow decimal number

            if number < 0:
                raise NegativeNumberError("Number must be positive.")
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except NegativeNumberError as e:
            print(f"Error: {e}")

if __name__ == "__main__": # With this part, it is unbale to remotely execute this part
    try:
        positive_num = get_positive_number()
        print(f"You entered a positive number: {positive_num}")
    except NegativeNumberError as a:
        print(f"Caught an error in the main script: {a}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")