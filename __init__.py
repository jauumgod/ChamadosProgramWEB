#app flask
from flask import Flask, url_for, render_template, redirect

app = Flask (__name__)

@app.route("/")
def inicio():
  return render_template("inicio.html")


@app.route("/chamados")
def chamados():
  return render_template("chamados.html")

if __name__ =="__main__":
  app.run(debug=True)
