import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium
from opencage.geocoder import OpenCageGeocode
import webbrowser

# taking input the phonenumber along with the country code
number = input("Enter the PhoneNumber with the country code: ")
# Parsing the phonenumber string to convert it into phonenumber format
phoneNumber = phonenumbers.parse(number)

# Storing the API Key in the Key variable
Key = "e262d8a9fc864d4c85f5e7639c58c227"  # generate your api https://opencagedata.com/api

# Using the geocoder module of phonenumbers to print the Location in console
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("location : " + yourLocation)

# Using the carrier module of phonenumbers to print the service provider name in console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("service provider : " + yourServiceProvider)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Getting the map for the given latitude and longitude
myMap = folium.Map(location=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# Save map to html file
html_file_path = "Location.html"
myMap.save(html_file_path)

# Open the HTML file in the default web browser
webbrowser.open(html_file_path)
