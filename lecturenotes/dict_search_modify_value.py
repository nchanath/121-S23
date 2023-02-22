# Define a dictionary
stock = {'apple': 5, 'banana': 10, 'orange': 7}
print(f"The current stock is {stock}")

old_value = 7
new_value = 10

for key, val in stock.items():

    # search for old_value
    if val == old_value:
        print(f"The key for the value {old_value} is {key}")

        # replace old_value with new_value
        stock[key] = new_value
        
        print(f"The new value for {key} is set to {stock[key]}")
        print(f"The stock is now {stock}")
