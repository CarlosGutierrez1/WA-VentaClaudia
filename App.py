from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CJ322100'
app.config['MYSQL_DB'] = 'wa-ventaspe'

mysql = MySQL(app)

app.secret_key = "UnaContras3nas3cr3ta"

@app.route('/')
def Rindex():
    return render_template('index.html')

@app.route('/Ingresardatos')
def Ringresardatos():
    return render_template('Ingresardatos.html')
@app.route('/Mostrardatos')
def RMostrardatos():
    return render_template('Mostrardatos.html')
