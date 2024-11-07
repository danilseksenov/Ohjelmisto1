import mysql.connector
from flask import Flask, request, json

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game2',
            user='danilseksenov',
            password='mammutti123',
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            autocommit=True
        )
        if conn.is_connected():
            return conn
        else:
            print("Yhteyttä ei voitu muodostaa.")
            return None
    except mysql.connector.Error as err:
        print(f"Tietokantavirhe: {err}")
        return None

app = Flask(__name__)

def get_from_sql(icao_code):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        sql = (f"SELECT ident, name, municipality FROM airport WHERE ident = %s")
        cursor.execute(sql, (icao_code,))
        result = cursor.fetchone()
        return {"ICAO": result[0], "Name": result[1], "Municipality": result[2]} if result else None

@app.route("/kenttä/<string:icao_code>")
def airport_info(icao_code):
    airport = get_from_sql(icao_code.upper())
    if airport:
        return json.dumps(airport)
    else:
        return json.dumps({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
