
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
#revenue = []
    
def calculate_revenue(prices, quantities_sold):
    revenue_local=[]
    for rl in range(len(prices)):
        revenue_local.append(prices[rl] * quantities_sold[rl])
    return revenue_local
revenue=calculate_revenue(prices,quantities_sold)

def formatted_output(revenue_per_product): 
    for prod, rev in sorted(revenue_per_product):
        print(f"{prod.lower()} has total revenue of ${rev}")
        
#prod=formatted_output(revenue_per_product) 
revenue_per_product=list(zip(products, revenue))
sorted_revenue=sorted(revenue_per_product)
formatted_output(revenue_per_product)
#formatted_output(name, revenue) 


# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${rev enue[1]}")