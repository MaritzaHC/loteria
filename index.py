from flask import Flask, render_template
from flask import request
import numpy as np
from static.py.predict import Predictor
app = Flask(__name__)

@app.route('/')
def home():
    cantidad = 0
    return render_template('home.html', cantidad=cantidad)

@app.route('/nuevoSorteo', methods = ['POST'])
def nuevoSorteo():
    data = request.form
    dediez = Predictor(data['sorteo'])
    #modifigar las fecheas para que lo reciba la funcion
    cantidad = dediez.predict(test_data)#aqui las fechas

    return render_template('home.html',cantidad = cantidad)

if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=JqUV25aFRV0