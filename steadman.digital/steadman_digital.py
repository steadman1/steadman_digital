from flask import Flask, request, render_template, redirect, url_for, flash
import steadman_firebase

app = Flask(__name__)

web_color = "#282828"

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")

@app.route("/code/class-transcript", methods=["GET"])
def class_trans():
    return render_template("class-transcript.html")

if __name__ == "__main__":
    app.run(host='steadman-digital.herokuapp.com')
