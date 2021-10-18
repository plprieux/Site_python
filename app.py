from flask import Flask, render_template, request
from http import HTTPStatus

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content="Testing")

@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1, num2):
    result = num1 * num2
    return render_template('multiplication.html', num1=num1, num2=num2, result=result)

@app.route('/hello/<name>')
def hello(name):
    #return 'Bonjour {} !'.format(name), HTTPStatus.OK
    return render_template('hello.html', nom=name)

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