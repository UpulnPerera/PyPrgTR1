try:
    user_input = input("Enter a list of numbers separated by commas (,)")
    numbers_str = user_input.split(',')
    numbers = []

    if not numbers_str or (len(numbers_str) == 1 and not numbers_str[0]):
        raise IndexError("The list is empty.")
    
    for num_str in numbers_str:
        numbers.append(int(num_str.strip()))
    
except ValueError:
    print("Error: Non-numeric input encountered. Please enter only numbers.")
except IndexError as e:
    print(f"Error: {e}")
else:
    total_sum = sum(numbers)
    print(f"The sum of the numbers is: {total_sum}")
finally:
    print("Program completed")