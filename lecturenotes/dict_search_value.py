# Define a dictionary
my_dict = {'apple': 5, 'banana': 10, 'orange': 7}

# Search for a value in the dictionary
value = 7
for key, val in my_dict.items():
    if val == value:
        print(f"The key for the value {value} is {key}")
