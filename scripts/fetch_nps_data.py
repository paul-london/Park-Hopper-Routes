# Available fields for each park
"""
id
url
*fullName
*parkCode (only needed for amenities)
name
*description
*designation
*latitude
*longitude
latLong (combined "lat:..., long:...")
*activities (array of objects with id and name)
*amenities
topics
*states
contacts (e.g., phone, email)
entranceFees (array)
entrancePasses
fees
directionsInfo
directionsUrl
operatingHours
addresses
images (photos array)
weatherInfo
"""

# Import requests for JSON and pandas
import requests
import pandas as pd
import time
from tqdm import tqdm 

api_key = "API_KEY"
url = "https://developer.nps.gov/api/v1/parks"

def fetch_all_parks(api_key):
    """
    Gets information from NPS about National Parks.
    """
    all_parks = []
    start = 0
    limit = 50

    while True:
        params = {
            "limit": limit,
            "start": start,
            "api_key": api_key,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()  # raise error for bad response
        data = response.json().get("data", [])

        if not data:
            break  # no more data

        all_parks.extend(data)
        start += limit  # go to next page

    return all_parks

# Fetch data
parks_raw = fetch_all_parks(api_key)

# Convert to DataFrame
records = []
for park in parks_raw:
    # Activities
    activity_list = park.get('activities', [])
    activity_names = [a.get('name', '') for a in activity_list]
    # Topics
    topic_names = [t.get('name', '') for t in park.get('topics', [])]
    # First image
    images = park.get('images', [])
    image_url = images[0].get('url') if images else ''
    image_caption = images[0].get('caption') if images else ''
    # Contacts
    contacts = park.get('contacts', {})
    phone = contacts.get('phoneNumbers', [{}])[0].get('phoneNumber', '') if contacts.get('phoneNumbers') else ''
    email = contacts.get('emailAddresses', [{}])[0].get('emailAddress', '') if contacts.get('emailAddresses') else ''
    # Addresses
    addresses = park.get('addresses', [])
    physical = next((a for a in addresses if a.get('type') == 'Physical'), {})
    mailing = next((a for a in addresses if a.get('type') == 'Mailing'), {})
    # Operating hours
    operating_hours_list = park.get('operatingHours', [])
    hours = operating_hours_list[0] if operating_hours_list else {}
    op_desc = hours.get('description', '')
    standard_hours = hours.get('standardHours', {})
    hours_string = ', '.join(f"{k}: {v}" for k, v in standard_hours.items())
    # Entrance fees and passes
    entrance_fees = park.get('entranceFees', [])
    fee = entrance_fees[0] if entrance_fees else {}
    fee_cost = fee.get('cost', '')
    fee_desc = fee.get('description', '')
    fee_title = fee.get('title', '')
    # Passes
    entrance_passes = park.get('entrancePasses', [])
    pass_info = entrance_passes[0] if entrance_passes else {}
    pass_cost = pass_info.get('cost', '')
    pass_title = pass_info.get('title', '')
    pass_desc = pass_info.get('description', '')

    records.append({
        'id': park.get('id', ''),
        'parkCode': park.get('parkCode', ''),
        'name': park.get('fullName', ''),
        'latitude': park.get('latitude', ''),
        'longitude': park.get('longitude', ''),
        'designation': park.get('designation', ''),
        'states': park.get('states', ''),
        'description': park.get('description', ''),
        'directionsInfo': park.get('directionsInfo', ''),
        'directionsUrl': park.get('directionsUrl', ''),
        'weatherInfo': park.get('weatherInfo', ''),
        'url': park.get('url', ''),
        'activities': ', '.join(activity_names),
        'topics': ', '.join(topic_names),
        'image_url': image_url,
        'image_caption': image_caption,
        'contact_phone': phone,
        'contact_email': email,
        'physical_address': f"{physical.get('line1', '')}, {physical.get('city', '')}, {physical.get('stateCode', '')} {physical.get('postalCode', '')}",
        'mailing_address': f"{mailing.get('line1', '')}, {mailing.get('city', '')}, {mailing.get('stateCode', '')} {mailing.get('postalCode', '')}",
        'operating_hours_description': op_desc,
        'standard_hours': hours_string,
        'entrance_fee_cost': fee_cost,
        'entrance_fee_title': fee_title,
        'entrance_fee_description': fee_desc,
        'entrance_pass_cost': pass_cost,
        'entrance_pass_title': pass_title,
        'entrance_pass_description': pass_desc
    })

parks = pd.DataFrame(records)

# Get park amenities by park code
def get_amenities_by_park(park_code, api_key):
    """
    Gets list of amenity names for a specific park by its parkCode.
    """
    url = "https://developer.nps.gov/api/v1/amenities/parksplaces"
    params = {
        "parkCode": park_code,
        "api_key": api_key
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json().get("data", [])
        print(f"Raw data for {park_code}: {data}")  # Debug
        if data and isinstance(data[0], list):
            amenities_list = data[0]
        else:
            amenities_list = []
        print(f"Amenities list: {amenities_list}")  # Debug
        amenity_names = [amenity['name'] for amenity in amenities_list]
        return ', '.join(amenity_names)
    except Exception as e:
        print(f"Error for park {park_code}: {e}")
        return ""

# Add amenities to dataframe
amenities = []
for code in tqdm(parks['parkCode']):
    time.sleep(1)
    amenities.append(get_amenities_by_park(code, api_key))

parks['amenities'] = amenities

# Drop parkCode column - not needed
parks.drop(columns=['parkCode'], inplace=True)

# Save as CSV
parks.to_csv("../data/parks.csv", index=False)
