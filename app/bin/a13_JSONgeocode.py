import json, urllib.request, urllib.parse, urllib.error, ssl

import requests

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

baseaddr = "http://py4e-data.dr-chuck.net/json?"

# address = input('Enter location: ')
# if len(address) < 1: break
address = 'UNISA'
parms = dict()
parms['address'] = address

parms = {'address': address, 'key': api_key}
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)

r = requests.get(url)

js = r.json()

# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters')

# try:

# js = json.loads(data)
# except:
#     js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(js)
    # continue

print(json.dumps(js, indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
