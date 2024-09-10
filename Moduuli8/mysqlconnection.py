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

cursor = connection.cursor()
cursor.execute("SELECT name, iso_country FROM country WHERE name = 'asdas'")
#result = cursor.fetchone()
#print(result[0])
#result = cursor.fetchmany(3)
#print(result)
result = cursor.fetchall()
print(result)