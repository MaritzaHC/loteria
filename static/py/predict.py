from mysql_final import run_query
#from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

class Predictor:
	model = None

	def __init__(self, id):
		self.train(id)

	def train(self, id):
		#-------Datos de Entrenamiento --------
		training_query = "select datediff(fecha_sorteo,fecha_ingreso) as dias, Month(fecha_sorteo), Day(fecha_sorteo), precio from sorteoespecifico where fecha_ingreso > '2015-02-25 00:00:00' and fecha_ingreso < '2019-01-01 00:00:00' and ID_Sorteo = " + str(id) + ";" 
		training_result = run_query(training_query)

		npArray = np.array(training_result) 
		training_data = npArray

		#-------Salida de Entrenamiento --------

		target_query = "select (ingresados - regresados) as vendidos from sorteoespecifico where fecha_ingreso > '2015-02-25 00:00:00' and fecha_ingreso < '2019-01-01 00:00:00' and ID_Sorteo = " + str(id) + ";" 
		target_result = run_query(target_query)

		npArray = np.array(target_result) 
		target_data = npArray

		self.model = Sequential()
		self.model.add(Dense(16, input_dim = 4, kernel_initializer = 'uniform', activation = 'relu'))
		self.model.add(Dense(8, kernel_initializer = 'uniform', activation = 'relu'))
		self.model.add(Dense(4, kernel_initializer = 'uniform', activation = 'relu'))
		self.model.add(Dense(1, kernel_initializer = 'uniform', activation = 'relu'))

		self.model.compile(loss = 'poisson', optimizer = 'adam', metrics = ['accuracy'])
		self.model.fit(training_data, target_data, epochs = 3000, batch_size = 5, verbose = 0)

	def predict(self, array):
		return self.model.predict(array)


	def show_comparison(self, expected, predicted):
		return np.concatenate((expected,predicted),axis=1)
