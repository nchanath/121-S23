# Create
capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Italy": "Rome",
    "Japan": "Tokyo",
}

# Update the value for Italy
capitals["Italy"] = "Milan"
print("The new capital of Italy is", capitals["Italy"])

# Remove Canada from the dictionary
del capitals["Canada"]
print("Canada has been removed from the dictionary.")

# Add a new country and its capital to the dictionary
capitals["Australia"] = "Canberra"
print("The capital of Australia is", capitals["Australia"])

# Iterate over the key-value pairs in the dictionary
print("List of capitals:")
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
