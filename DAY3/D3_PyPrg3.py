import json
import datetime

# Create a python dictionary representing product information.
# The 'last_updated' timestamp is generated dynamically for demostration

product_data = {
    "products": [
        {"id": "A1", "name": "Keybpard", "price": 75.00, "stock": "available"},
        {"id": "A2", "name": "Mouse", "price": 25.50, "stock": "available"},
        {"id": "A3", "name": "Monitor", "price": 300.00, "stock": "available"},
        {"id": "A4", "name": "Webcam", "price": 50.00, "stock": "available"},
        {"id": "A5", "name": "Headphone", "price": 120.00, "stock": "available"}
    ],
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
}

#Define the name of the JSON file
json_file_name = "products.json"

print(f"Attempting to write product data to '{json_file_name}'...")
try:
    # Open the JSON file in write mode ('w').
    # Using 'with' statement ensures the file is properly closed.
    with open(json_file_name, mode='w', encoding='utf-8') as json_file_name:

        json.dump(product_data, json_file_name, indent=4)
        print(f"Sucessfully wrote product data to '{json_file_name}'.")

except IOError as e:
    print(f"Error: Could not wirte to file '{json_file_name}'. {e}")
except Exception as e:
    print(f"An expected error occured: {e}")
            #(variable_ json_file_name: Literal['products.json'])

print(f"\nPlease check the jason file ")