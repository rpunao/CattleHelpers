import random
import json
'''
{
    "ID" :0
    "date": "2018-08-04T17:00:00Z",
    "location":[40.7398,-121.26866]
    "DeviceID": 1234
    "FarmID":
    ]
}
'''
def randLatLong():
    CONST_LAT1 = 35.323659
    CONST_LON1 = -120.652973
    CONST_LAT2 = 35.3227741
    CONST_LON2 = -120.646899
    lat = round(random.uniform(CONST_LAT2, CONST_LAT1),6)
    lon = round(random.uniform(CONST_LON1, CONST_LON2),6)
    return {'lat' : lat, 'lon' : lon}

def generateData():
    CONST_DEVICEID = 1
    CONST_FARMID = 0
    data = {}
    for i in range(10):
        data[i] = []
        tempLoc = randLatLong()
        data[i].append({
            'ID' : i,
            'Date:' : '2018-10-10T0' + str(i) + ':00:00Z',
            'Location' : [tempLoc['lat'], tempLoc['lon']],
            'DeviceID' : 1234,
            "FarmID" : 0
        })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=3)

generateData()