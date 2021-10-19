from flask import Flask, render_template, request
from http import HTTPStatus

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html", content="Testing")

@app.route('/multiplication')
def multiplier():
    return render_template("multiplication.html")

@app.route('/hello')
def hello():
    return render_template("index.html", content="Testing")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  a = result['age']
  return render_template("resultat.html", nom=n, prenom=p, age=a)

@app.route('/add')
def calcul():
    return render_template("add.html")

@app.route('/addresult',methods = ['POST'])
def addresult():
  result = request.form
  n1 = result['nbr1']
  n1 = int(n1)
  n2 = result['nbr2']
  n2 = int(n2)
  resultat = n1+n2
  return render_template("addresult.html", nbr1=n1, nbr2=n2, result=resultat)

@app.route('/resultmul',methods = ['POST'])
def resultmul():
  result = request.form
  n1 = result['nbr1']
  n1 = int(n1)
  n2 = result['nbr2']
  n2 = int(n2)
  resultat = n1*n2
  return render_template("resultmul.html", nbr1=n1, nbr2=n2, result=resultat)