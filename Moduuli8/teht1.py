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

def fetch_airport_by_icao(icao):
    sql = f"select name, municipality from airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

user_input = input("Anna ICAO- koodi: ").upper()
result = fetch_airport_by_icao(user_input)

if result != None:
    print(f"Haettu kenttä: {result[0]}, {result[1]}")
else:
    print("Eipä löydy")