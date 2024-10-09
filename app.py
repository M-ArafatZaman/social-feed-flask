from flask import Flask, render_template, request, redirect, make_response
from db import create_table, insert_user, get_all_users

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template("home.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    create_table()
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    insert_user(name, email, password)
    return redirect("/dashboard")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    users = get_all_users()
    return render_template("dashboard.html", users=users)
