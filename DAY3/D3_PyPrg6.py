import csv

# Define the name of the CSV file to read from
csv_file_name = "employees.csv"

# Defime the departement to filter by
target_departement = "IT"

print(f"Attempting to read employee data from '{csv_file_name} and filter by")

filtered_employees = []

try:
    # Open the CSV file in read mode ('r').
    with open(csv_file_name, mode = 'r', newline = '') as csv_file:
        # Create a csv.DictReader object.
        # This reader will treat each row as a dictionary using the header row
        reader = csv.DictReader(csv_file)

        # Iterte through each row in csv file
        for row in reader:
            # Check if the Departement value of the current row matches the 
            if row.get('Departement') == target_departement:
                filtered_employees.append(row)
    print(f"\nFiltered employee list: {filtered_employees}")

except FileNotFoundError:
    print(f"Error: The file '{csv_file_name}' was not fount. Please")
except Exception as e:
    print(f"An expected error occurred: {e}")
