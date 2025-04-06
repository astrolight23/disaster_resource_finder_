import json

# Load the data
with open("offline_data.json", "r") as file:
    data = json.load(file)

# Print all available resources
print("=== Emergency Resource List ===\n")
for resource in data["resources"]:
    print(f"Type: {resource['type'].title()}")
    print(f"Name: {resource['name']}")
    print(f"Address: {resource['address']}")
    print(f"Contact: {resource['contact']}")
    print(f"Status: {resource['status']}")
    print("-" * 40)
