from flask import Flask
import requests
import yaml

app = Flask(__name__)

@app.route("/")
def index():
    data = yaml.safe_load("a: 1")
    r = requests.get("https://example.com")
    return f"Data: {data}, Status: {r.status_code}"

if __name__ == "__main__":
    app.run()
