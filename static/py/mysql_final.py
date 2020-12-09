import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'loteria' 

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data



#para intalar descargra en https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient y poner poner: 
#pip install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl