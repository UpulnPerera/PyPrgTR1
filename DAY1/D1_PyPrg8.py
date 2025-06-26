total_sum = 0

for number in range(1, 101):
    # Add the current number to the total_sum
    total_sum += number # This is equivalent to total_sum = total_sum + number

# print the final sum after the loop has completyed
print(f"The sum of numbers from 1 to 100 is {total_sum}")