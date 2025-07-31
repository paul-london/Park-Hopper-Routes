# Import libraries
import pandas as pd
import googlemaps
import numpy as np

# Create necessary dataframes
parks_subset = pd.read_csv('../data/parks_subset.csv')

# Initialize Google Maps API client
api_key_g = 'API_KEY'
gmaps = googlemaps.Client(key=api_key_g)

def GenerateGoogleMapsArray(origins, destinations):
    # Create origin dictionary using parks_w
    keys = parks_subset['name']
    values = [(parks_subset.loc[parks_subset['name'] == name, 'latitude'].values[0],        # redundant/cleanup to get coordinates tuple directly
           parks_subset.loc[parks_subset['name'] == name, 'longitude'].values[0])
          for name in keys]

# To compute trips from A to B
origins = dict(zip(keys, values))

# To compute trips from B to A
destinations = origins

# Initialize distance matrix
travel_array = np.zeros((len(origins) * (len(destinations) - 1), 4), dtype = object)

# Loop through all dictionary items
i = 0
for origin_name, origin_coords in origins.items():
    for dest_name, dest_coords in destinations.items():
        # Skip pairs where origin = destination (distance 0)
        if origin_name == dest_name:
            continue
        
        # Travel data from origin to destination
        result = gmaps.distance_matrix(origins=[origin_coords], destinations=[dest_coords], mode='driving')
        element = result['rows'][0]['elements'][0]
        # Check for valid result
        if element['status'] == 'OK':
            distance_meters = element['distance']['value']
            duration_seconds = element['duration']['value']
            
        travel_array[i, 0] = origin_name
        travel_array[i, 1] = dest_name
        travel_array[i, 2] = np.round(distance_meters / 1609.344, 2)
        travel_array[i, 3] = np.round(duration_seconds / 3600, 2)

        i += 1

        print(f"{origin_name} → {dest_name} = {np.round((distance_meters/1609.344),2)} mi ({np.round((duration_seconds/3600),2)} hrs)") # convert to miles and hours

        time.sleep(0.5)  # Pause to avoid API rate limits



# Print array
print("\nTravel Matrix:")
print(travel_array)

# Save array
np.save('../data/arrays/travel_array_subset.npy', travel_array)
