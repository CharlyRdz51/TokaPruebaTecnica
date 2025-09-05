#Se realiza la imporatcion de las librerias mysql... pip install mysql-connector-python
import mysql.connector 

class CConexion:

   def ConexionBaseDeDatos():
    try:
        conexion = mysql.connector.connect(user='root',password='1951',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
        print("Conexion Correcta")
        
        return conexion
    
    except mysql.connector.Error as error:
        
        print("Error al conectar con la base de datos {}".format(error))
        
             
   ConexionBaseDeDatos()
            