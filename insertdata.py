import psycopg2
import generatevalues as value

NUM_RECORDS = 10

def postgres_insert():
    try:
        conn = psycopg2.connect(
            "dbname='CattleDB' user='cattleroot' host='cattleinstance.coo92izzstxf.us-west-2.rds.amazonaws.com' password='05t*XQDxuuaM'")
        cur = conn.cursor()

        for i in range(NUM_RECORDS):
            time = value.getTime()
            lon = value.randLon()
            lat = value.randLat()
            device_id = '1'
            farm_id = '1'
            command = ('INSERT INTO location (date, longitude, latitude, device_id_id, farm_id_id) VALUES (\''
                       + time + '\', ' + lon + ', ' + lat + ', ' + device_id + ', ' + farm_id + ');')
            cur.execute(command)
            conn.commit()

        conn.close()
        return True
    except:
        print('Fail')
        return False


postgres_insert()
