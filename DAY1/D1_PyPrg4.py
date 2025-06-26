# Ask the user to input their favorite number
favorite_number_str = input("Please enter your favorite number: ")
try:
    # Try converting to an integer first
    converted_number = int(favorite_number_str)
    print(f"nSuccessfully converted input to an integer: {converted_number}")
    final_result_int = converted_number + 10
    print(f"Results after adding 10 (integer): {final_result_int}, Type: {type(final_result_int)}")

 except ValueError:
    # If integer conversion fails, try converting to a float
    try:
        converted_number = float(favorite_number_str)
        print(f"\nSuccessfully converted input to a float: {converted_number}")
        final_result_int = converted_number + 10
        print(f"Results after adding 10 (float): {final_result_int}, Type: {type(final_result_int)}")

    except ValueError:
        # If integer conversion fails, try converting to a float
        print(f"\nSuccessfully converted input to a float: {converted_number}")
        final_result_int = converted_number + 10
        print(f"Results after adding 10 (float): {final_result_int}, Type: {type(final_result_int)}")

