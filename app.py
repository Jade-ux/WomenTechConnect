import os

from flask import (Flask, render_template)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


@app.route("/inspiration")
def inspiration():
    return render_template("inspiration.html")


@app.route("/404")
def pagenotfound():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)