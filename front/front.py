from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    try:
        res = requests.get("http://back:3000/api/v1/get-quote")
        quote = res.json().get("random_quote", "No quote found.")
    except:
        quote = "Could not fetch quote."
    return render_template("index.html", name=name, quote=quote)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)

