import random
from datetime import datetime

CONST_LAT = 35.325467
CONST_LON = -120.653275
CONST_DELTA = 0.002500
CONST_TIME = datetime.now()

def setNewLat(old):
    return old + round(random.uniform(-CONST_DELTA*2, CONST_DELTA*2), 6)

def setNewLon(old):
    return old + round(random.uniform(-CONST_DELTA*2, CONST_DELTA*2), 6)

def newLat(currLat):
    delt = round(random.uniform(-CONST_DELTA, CONST_DELTA), 6)
    return CONST_LAT + delt

def newLon(currLon):
    delt = round(random.uniform(-CONST_DELTA, CONST_DELTA), 6)
    return CONST_LON + delt

def randLat():
    CONST_LAT1 = 35.323659
    CONST_LAT2 = 35.3227741
    lat = round(random.uniform(CONST_LAT2, CONST_LAT1), 6)
    return str(lat)

def randLon():
    CONST_LON1 = -120.652973
    CONST_LON2 = -120.646899
    lon = round(random.uniform(CONST_LON1, CONST_LON2),6)
    return str(lon)

def getTime():
    dt = datetime.now()
    dt.isoformat("T")
    return dt

print(newLat(0))