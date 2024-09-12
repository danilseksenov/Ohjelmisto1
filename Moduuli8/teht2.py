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

def fetch_type_by_iso_country(iso_country):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{iso_country}' GROUP BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

user_input = input("Syötä maakoodi: ").upper()
result = fetch_type_by_iso_country(user_input)
print(f"Lentokenttien lukumäärät tyypeittäin: \n{result}")