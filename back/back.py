from flask import Flask, request, jsonify
import pymysql
import random

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'data'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydatabase'

def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
    )

@app.route("/api/v1/get-quote", methods=["GET"])
def get_quote():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quotes")
    quotes = cursor.fetchall()
    conn.close()
    if quotes:
        return jsonify({"random_quote": random.choice(quotes)[1]})
    return jsonify({"error": "No quotes found"})

@app.route("/api/v1/set-quote", methods=["POST"])
def set_quote():
    new_quote = request.json.get("quote")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (new_quote,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Quote added!"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

