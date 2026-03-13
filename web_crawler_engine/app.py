from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load crawled data
with open("data.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        query = request.form["query"].lower()

        for page in pages:
            if query in page["title"].lower() or query in page["content"].lower():
                results.append(page)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)