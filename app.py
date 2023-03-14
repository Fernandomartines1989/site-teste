from flask import Flask

app = Flask(__name__)

menu = """ <a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> <br> """

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Esse é meu site. (Fernando Martines)"

@app.route("/sobre")
def sobre():
  return menu + "Meu nome é Fernando Martines, sou jornalista"

@app.route("/contato")
def contato():
  return menu + "fernandomartines0@gmail.com"
