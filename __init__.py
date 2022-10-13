#app flask
from flask import Flask, url_for, render_template, redirect
import data_base as db

app = Flask (__name__)
app.config['SECRET_KEY]= 'UZUMYMW_15032325'

           
@app.route("/")
def inicio():
  return render_template("inicio.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/chamados")
def chamados():
  return render_template("chamados.html")
           
@app.route("/settings")
def settings():
  return render_template("settings.html")

if __name__ =="__main__":
  app.run(debug=True)
