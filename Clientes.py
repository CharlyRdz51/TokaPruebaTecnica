#Se importa todo desde Conexion
from Conexion import *

class ccclientes:
    
    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mosstrar de datos{}".format(error))
    
    def ingresarClientes(nombres,apellidos,sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s);"
            #La variable valores tiene que ser una tupla, Como minina expresion es (valor,)
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Ingresado")
            cone.close()
            

        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))
            
    def modificarClientes(idUsuario,nombres,apellidos,sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %s Where usuarios.id =%s;"
            valores = (nombres,apellidos,sexo,idUsuario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()
            

        except mysql.connector.Error as error:
            print("Error de Actualizado{}".format(error))
            
    def eliminarClientes(idUsuario):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE from usuarios WHERE usuarios.id = %s;"
            valores = (idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Elminado")
            cone.close()
            

        except mysql.connector.Error as error:
            print("Error de Eliminacion{}".format(error))

