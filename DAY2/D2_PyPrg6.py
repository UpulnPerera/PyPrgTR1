# Create the kist baned temperatures
temperaures = [25.5, 28.1, 22.9, 30.2, 27.8, 24.3, 29.5]

# Add 31.0 to the end of the temperatures list
temp1 = temperaures.append(31.0)
print(temperaures)

# remove the third element (Index 2) from the list
temp2 = temperaures.pop(2)
print(temp2)

# Find the maximum and minimum temperature in the list
max_temp = max(temperaures)
print(f"Maximum Temperature is {max_temp}")

min_temp = min(temperaures)
print(f"Minimum Temperature is {min_temp}")

# Calculate the average temperature
avg_temp = sum(temperaures) / len(temperaures)

# Print the modified list, the maximum and minimum, and average temperature
print(f"Modified temperatures list: {temperaures}")
print(f"Maximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")
print(f"Average temperature: {avg_temp}")