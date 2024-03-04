import csv
from geopy.geocoders import Nominatim

def geocode_area(area_id):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(area_id)
    if location:
        return location.address
    else:
        return None

with open('sample_data.csv', newline='') as csvfile:
    read = csv.DictReader(csvfile)
    for row in read:
        area_id = row['area_id']
        address = geocode_area(area_id)
        if address:
            print(f"Полный адрес ID {area_id}: {address}")
        else:
            print(f"Адрес для ID {area_id} не найден.")
