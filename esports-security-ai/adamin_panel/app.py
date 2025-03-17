from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    logs = []
    if os.path.exists("logs/security.log"):
        with open("logs/security.log", "r") as file:
            logs = file.readlines()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
