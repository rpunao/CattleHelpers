import psycopg2
import generatevalues as value

NUM_RECORDS = 30
CONST_LAT = 35.325467
CONST_LON = -120.653275
from datetime import datetime
from datetime import timedelta

def postgres_insert():
    try:
        conn = psycopg2.connect(
            "dbname='CattleDB' user='cattleroot' host='cattleinstance.coo92izzstxf.us-west-2.rds.amazonaws.com' password='05t*XQDxuuaM'")
        cur = conn.cursor()

        time_delta = 0
        for i in range(NUM_RECORDS):
            if (i % 7 == 0):
                CONST_LAT = value.setNewLat(CONST_LAT)
                CONST_LON = value.setNewLon(CONST_LON)
            time = str(value.getTime() + timedelta(minutes=time_delta))
            lon = str(value.newLon(CONST_LON))
            lat = str(value.newLat(CONST_LAT))
            device_id = '1'
            farm_id = '1'
            command = ('INSERT INTO location (date, longitude, latitude, device_id_id, farm_id_id) VALUES (\''
                       + time + '\', ' + lon + ', ' + lat + ', ' + device_id + ', ' + farm_id + ');')

            time_delta = time_delta + 15
        cur.execute(command)
        conn.commit()
        conn.close()
        return True
    except:
        print('Fail')
        return False


postgres_insert()
