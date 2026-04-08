# Initialize the inventory dictionary with stock details
# "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
inventory =  {"Bread": [30, 50, 10, False],"Eggs": [120, 200, 40, False],"Milk": [60, 100, 20, False],"Apples": [15, 50, 15, False]}
discount_threshold = 100
print("Processing started")
for item in inventory:
    current_stock, minimum_stock, restock_amount, on_sale = inventory[item]
    print(f"Processing {item}")
    while current_stock < minimum_stock:
        current_stock += restock_amount
print("Processing completed")
        

    