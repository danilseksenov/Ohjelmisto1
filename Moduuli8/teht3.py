from geopy import distance

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='mammutti123',
         autocommit=True,
         collation = 'utf8mb4_general_ci',
         )
def distance_between_airports(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

user_input1 = input("Syötä ICAO- koodi: ").upper()
user_input2 = input("Syötä ICAO- koodi: ").upper()

result1 = distance_between_airports(user_input1)
result2 = distance_between_airports(user_input2)
result_distance = distance.distance(result1, result2).km
print(f"Kahden lentokentän välinen etäisyys on {result_distance:.2f} km")


