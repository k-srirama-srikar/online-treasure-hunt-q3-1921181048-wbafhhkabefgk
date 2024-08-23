from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("page.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c3 = False
    ans3 = ""

    if request.method == "POST":
        pwd = request.form['pwd']
        if pwd == "aurjaoobt":
            c3 = True
            ans3 = "first link"
        else:
            return render_template("page.html")
    return render_template("page.html", c1=c3, ans1=ans3)
