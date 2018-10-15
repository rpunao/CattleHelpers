import random
from datetime import datetime

def randLat():
    CONST_LAT1 = 35.323659
    CONST_LAT2 = 35.3227741
    lat = round(random.uniform(CONST_LAT2, CONST_LAT1),6)
    return str(lat)

def randLon():
    CONST_LON1 = -120.652973
    CONST_LON2 = -120.646899
    lon = round(random.uniform(CONST_LON1, CONST_LON2),6)
    return str(lon)

def getTime():
    dt = datetime.now()
    dt.isoformat("T")
    return str(dt)