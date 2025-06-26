import csv
import datetime

# Create a python dictionary representing product information.
# The 'last_updated' timestamp is generated dynamically for demostration

employee_data = [
        {"Name": "Alice Smith", "Departement": "HR", "Salary": 100},
        {"Name": "Bob Johnson", "Departement": "IT", "Salary": 50},
        {"Name": "Charlie Brown", "Departement": "MKT", "Salary": 75},
        {"Name": "Diana Prince", "Departement": "IT", "Salary": 60},
        {"Name": "Eve Devson", "Departement": "HR", "Salary": 80}
    ]


#Define the name of the CSV file
csv_file_name = "employees.csv"

fieldnames = ["Name", "Departement", "Salary"]

print(f"Attempting to write product data to '{csv_file_name}'...")

try:
    # Open the csv file in write mode ('w').
    # Using 'with' statement ensures the file is properly closed.
    with open(csv_file_name, mode='w', newline = '') as csv_file_name:

        writer = csv.DictWriter(csv_file_name, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()
        writer.writerows(employee_data)
        print("CSV headers written.")

        # Write all employee data rows
        writer.writerows(employee_data)
        print(f"Successfully wrote {len(employee_data)} employee records to ")

except IOError as e:
    print(f"Error: Could not wirte to file '{csv_file_name}'. {e}")
except Exception as e:
    print(f"An expected error occured: {e}")

print(f"\nPlease check the csv file ")