print("🌪️ Welcome to the Disaster Resource Finder App 🌍")

# Dummy function to simulate locating nearby resources
def get_nearby_resources(location):
    # Placeholder logic
    resources = [
        {"name": "Relief Center A", "distance": "1.2 km"},
        {"name": "Medical Camp B", "distance": "2.5 km"}
    ]
    return resources

# Simulate a user location
user_location = "Bangalore"
resources = get_nearby_resources(user_location)

print(f"Nearby resources for {user_location}:")
for r in resources:
    print(f"- {r['name']} ({r['distance']})")
