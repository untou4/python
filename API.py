import urllib.request, urllib.parse, urllib.error
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address' : address}) # encodes text in the right way: address=Ann+Arbor%2C+Mi

    print('Retrieving',url)
    uh = urllib.request.urlopen(url) #get a handle
    data = uh.read().decode() #read whole doc and decode from utf8
    print('Retrieved',len(data),'characters')

    try:
        js = json.load(data) # string to dict/list
    except:
        js = None

    if not js or 'status' not in js or js['status'] !='OK': #standart checks
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js,indent=4)) #opposite to Read

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',  lng)
    location = js['results'][0]['formatted address']
    print(location)
