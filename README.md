# TokaPruebaTecnica
Repositorio con analisis de pruebas tecnicas, desarrollador fullstack

# Actividad 1 Diseño y Arquitectura de Software

![ArquitecturaPruebaTecnica](https://github.com/user-attachments/assets/888bf3fe-b6eb-4d00-ad30-13c4d9248bea)

## Justificacion

Decidi utilizar una doble autenticacion, para tener un doble candado al momento de que el usuario quiera ingresar al sistema, esta doble autenticacion deberia de involucrar una contraseña con ciertas reglas que haga dificil de descifrar la contraseña, mas de 10 caracteres, numeros y caracteres especiales adicional utilizar la biometria del usuario ya sea el rostro, huella dactilar o voz.

El almacenamiento de Logs para tener un registro de quien ingreso y quien intento ingresar, apoyado de un monitoreo de trafico que permita anticipar algun ataque DDoS y bloquear las ips atacantes.

Siempre y cuando sea un administrador quien ingresa al sistema, utilizar una api para determinar los roles de cada usuario y los permisos que tendran.

Independientemente de quien se logeo, que pase por una red privada para no tener trafico con posible acceso al publico.

Esta red privada virtual debera pasar por un balancer para distriibuir la carga de trabajo y la alta volumetria del sistema, acompañada de un monitor de recursos para toda la infrastuctura de la base de datos y aplicativos web. Entre el balancer y el front estara una API REST para el control del CRUD.

# Actividad 2 API REST ( Con Python )
Para esta actividad subire el codigo a este repositorio, lenguaje utilizado Python con MySQL.

El ORM tengo tiempo que no lo utilizo y estoy un poco oxidado. 

# Actividad 3 Code Review

Para el analisis del codigo en Python noto lo siguiente: 
Codigo repetido, se viola una de las mejores practicas en el desarollo que es " reutilizar codigo y evitar escribir lineas de codigo repetido "

Si user_id viene de un input del usuario, se ejecuta directamente en el SQL Esto permite extraer datos no autorizados o incluso borrar tablas.
**Grave vulnerabilidad de seguridad**.
Solución: usar consultas parametrizadas.

Es importante tener en cuenta que cada conexion sea cerrada manualmente, es decir asegurar que cada conexion que sea abierta sea cerrada, es importante utilizar conn.close() al ternimo de utilizar cada conexion.

"User_id" no tiene el tipo de dato definido si es caracter, cadena, booleano, entero, flotante, operador logico, etc etc

Un codigo mas eficiente podria ser el siguiente:

import sqlite3

def ObtenerDatosUsuario(user_id: int):
    try:
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None






