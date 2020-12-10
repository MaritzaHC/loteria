from flask import Flask, render_template
from flask import request
import datetime
import numpy as np
from static.py.mysql_final import run_query
from static.py.predict import Predictor

global redes

app = Flask(__name__)

@app.route('/')



def home():
	redes = []
	for i in range(5):
		redes.append(Predictor(i + 1))
	print("Ya acabé uwu")
    #cantidad = 0
	return render_template('home.html', cantidad=cantidad)

@app.route('/nuevoSorteo', methods = ['POST'])
def nuevoSorteo():
	data = request.form
	a_parts = data['fecha'].split("-")
	b_parts = data['fechaI'].split("-")
	a = datetime.datetime(int(a_parts[0]), int(a_parts[1]), int(a_parts[2]))
	b = datetime.datetime(int(b_parts[0]), int(b_parts[1]), int(b_parts[2]))
	dias = (a - b).days;
	mes = int(a_parts[1])
	dia = int(a_parts[2])
	precio = int(data['precio'])
	index_red = int(data['sorteo']) - 1
    #(a - b).split(" ")[0]
    #dediez = Predictor(data['sorteo'])
    #modifigar las fecheas para que lo reciba la funcion
    #cantidad = dediez.predict(test_data)#aqui las fechas
	cantidad = redes[index_red].predict(np.array([dias, mes, dia, precio]))
	return render_template('home.html',cantidad = cantidad)

if __name__ == '__main__':
	app.run(debug=True)

#https://www.youtube.com/watch?v=JqUV25aFRV0