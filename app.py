import os
from flask_login import (LoginManager, current_user, login_required)
from flask import (Flask, render_template)
from flask_pymongo import PyMongo
import pymongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Database environment variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def get_home():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


@app.route("/inspiration")
def inspiration():
    return render_template("inspiration.html")

@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/404")
def pagenotfound():
    return render_template("404.html")


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/team")
def team():
    return render_template("team.html")
    

@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

