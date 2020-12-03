"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from loteria import app

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

@app.route('/ventas')
def ventas():
    """Renders the about page."""
    return render_template(
        'ventas.html',
        title='Tipos de sorteo',
        year=datetime.now().year,
        message='Your application description page.'
    )
