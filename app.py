import os
from flask_login import (LoginManager, current_user, login_required)
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
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
    if request.method == "POST":
        # checks if the user exists in the database
        existing_user = mongo.db.users.find_one({"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already exists, please sign in")
            return redirect(url_for("signin"))

        register = {
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "full_name": request.form.get("fullName"),
            "current_role": request.form.get("currentRole"),
            "interests": request.form.get("areasOfInterest"),
            "location": request.form.get("location"),
            "mentee": request.form.get("mentee"),
            "mentor": request.form.get("mentor"),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Thank you for signing up!")
        # once logged, redirect user to dashboard,
        # using session cookie
        return redirect(url_for("thankyou", email=session["user"]))

    return render_template("signup.html")


@app.route("/thankyou/<email>", methods=["GET", "POST"])
def thankyou(email):
    if session["user"]:
        # get the session user's username from the database
        email = mongo.db.users.find_one(
            {"email": session["user"]})["email"]
        full_name = mongo.db.users.find_one(
            {"email": session["user"]})["full_name"]
        return render_template(
            "thankyou.html", email=email, full_name=full_name)


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

