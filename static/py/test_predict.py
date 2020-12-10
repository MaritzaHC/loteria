from mysql_final import run_query
import numpy as np
from predict_mejorado import Predictor


#-------Datos de Prueba --------

test_query = "select datediff(fecha_sorteo,fecha_ingreso) as dias, Month(fecha_sorteo), Day(fecha_sorteo), precio from sorteoespecifico where fecha_ingreso > '2018-12-31 00:00:00' and fecha_ingreso < '2020-01-01 00:00:00' and ID_Sorteo = 1;" 
test_result = run_query(test_query)

npArray = np.array(test_result)
test_data = npArray

#-------Salida de prueba --------

test_target_query = "select (ingresados - regresados) as vendidos from sorteoespecifico where fecha_ingreso > '2018-12-31 00:00:00' and fecha_ingreso < '2020-01-01 00:00:00' and ID_Sorteo = 1;" 
test_target_result = run_query(test_target_query)

npArray = np.array(test_target_result) 
test_target_data = npArray

dediez = Predictor(1)

prediccion = dediez.predict(test_data)
print(dediez.show_comparison(test_target_data, prediccion))
