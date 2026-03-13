from flask import Flask, request, redirect, jsonify
import string
import random
import json
import os

app = Flask(__name__)
DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/")
def home():
    return """<h1>URL Shortener</h1>
    <p>POST to /shorten with JSON: {"url": "https://example.com"}</p>
    <p>Then visit the returned short URL</p>"""

@app.route("/shorten", methods=["POST"])
def shorten():
    data = load_db()
    url = request.json.get("url")
    code = generate_code()
    data[code] = url
    save_db(data)
    return jsonify({"short_url": f"http://localhost:5000/{code}"})

@app.route("/<code>")
def redirect_url(code):
    data = load_db()
    if code in data:
        return redirect(data[code])
    return "URL not found"

if __name__ == "__main__":
    app.run(debug=True)
