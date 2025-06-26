import csv
#
stock_data = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keybpard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15} # External
]

print("---Initial Inventory---")
for product in stock_data:
    print(f"ID : {product['id']}, Name: {product['name']}. Price: {product['price']}, Stock: {product['stock']}")
print("\n")

###FIRST###


#Define the name of the CSV file
csv_file_name = "stock.csv"

fieldnames = ["id","name", "price", "stock"]

print(f"Attempting to write stock data to '{csv_file_name}'...")

try:
    # Open the csv file in write mode ('w').
    # Using 'with' statement ensures the file is properly closed.
    with open(csv_file_name, mode='w', newline = '') as csv_file_name:

        writer = csv.DictWriter(csv_file_name, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()
        writer.writerows(stock_data)
        print("CSV headers written.")

        # Write all employee data rows
        writer.writerows(stock_data)
        print(f"Successfully wrote {len(stock_data)} employee records to ")

except IOError as e:
    print(f"Error: Could not wirte to file '{csv_file_name}'. {e}")
except Exception as e:
    print(f"An expected error occured: {e}")

print(f"\nPlease check the csv file ")

##############

###SECOND


def update_stock(product_id, quantity):
    """
    Updates the stock for a given product to update
    Args:
        product_id( str): The ID of the product
        quantity (int): The amount to add to the stock. Can be negative
    """
    found = False
    for product in stock_data:
        if product['id'] == product_id:
            #Ensure stock does not go below zero
            if product['stock'] >= 0:
                product['stock'] = product['stock'] + quantity
                print(f"Updated stock for {product['name']} (ID: {product['id']})")
            else:
                print(f"Error: Not enough stock for {product['name']} (ID: {product['id']})")
            found = True
            break
    if not found:
        print(f"Error: Product with ID '{product_id}' not found in inventory)")

# update_stock(input("Enter the product ID: "),input("Enter the quantity: "));

def get_low_stock_products(threshold):
        """
                        adgada        
        """
        low_stock_products = []
        for product in stock_data:
            if product['stock'] < threshold:
                low_stock_products.append(product['name'])
        print(low_stock_products)
        return low_stock_products

#########

print("---Demostrate the functions---")
# --- Demostrate the functions---
update_stock("P001", -10) # Sell 10 Laptops
update_stock("P003", 5) # Restock 5 Keyboards 
update_stock("P005", -20) # Try to sell more Webcams than available

get_low_stock_products(30)
      

