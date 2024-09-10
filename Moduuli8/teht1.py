import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='mammutti123',
         autocommit=True,
         collation = 'utf8mb4_general_ci',
         )

def search_airport(nimi, kunta):
    cursor = connection.cursor()
    sql = (f"SELECT name, iso_region FROM airport WHERE ident = {icao_code} ")
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

icao_code = input("Syötä ICAO- koodi: ").upper()
search_airport(icao_code, icao_code)
