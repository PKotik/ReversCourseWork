from flask import Flask, request
import yaml
import os

app = Flask(__name__)

# УЯЗВИМОСТЬ 1 — RCE через небезопасный yaml.load()
@app.route("/yaml", methods=["POST"])
def yaml_injection():
    data = request.data.decode()
    result = yaml.load(data, Loader=yaml.Loader)  # BAD
    return {"parsed": str(result)}

# УЯЗВИМОСТЬ 2 — путь из запроса → Directory Traversal
@app.route("/read")
def read():
    path = request.args.get("file")
    return open(path, "r").read()

# УЯЗВИМОСТЬ 3 — команда из запроса → RCE
@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

# УЯЗВИМОСТЬ 4 — XSS
@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    return f"<h1>Hello {name}</h1>"

app.run()
