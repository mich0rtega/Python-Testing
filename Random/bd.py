import mysql.connector

try:

    conexion = mysql.connector.connect(
          host = 'localhost',
          user = 'root',
          password =''
     )
    micursor = conexion.cursor()
    sql = "CREATE DATABASE prueba"
    micursor.execute(sql)
except:
    print("ocurrio un error")
else:
    print("bd creada correctamente")