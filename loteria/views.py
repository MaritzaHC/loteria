"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request,redirect,url_for,flash 
from loteria import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='h4mildad'
app.config['MYSQL_DB'] ='loteria'
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Loteria',
        year=datetime.now().year,
    )

@app.route('/sorteos')
def sorteos():
    """Renders the contact page."""
    return render_template(
        'sorteos.html',
        title='Ventas',
        year=datetime.now().year,
       
    )

@app.route('/ventas',methods=['POST'])
def ventas():
    """Renders the about page."""
    return render_template(
        'ventas.html',
        title='Tipos de sorteo',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/junto',methods=['POST'])
def junto():
     if request.method == 'POST':
            sorteos = request.form['sorteos']
            fecha = request.form['fecha']
            print(sorteos)
            print(venta)
            return "recivido"