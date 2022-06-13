import datetime
import hashlib
from sqlite3 import connect
from unittest import result # Cifrar contraseña
import doctores.conexion as conexion

# Llamar la clase Conectar
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctores:
    
    def __init__(self, nombre, apellidos, especialidad, no_consultorio, dni, email, password):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Especialidad = especialidad
        self.No_Consultorio = no_consultorio
        self.Dni = dni
        self.Email = email
        self.Password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.Password.encode('utf8'))

        sql = "INSERT INTO doctores VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s)"
        doctor = (self.Nombre,self.Apellidos, self.Especialidad, self.No_Consultorio,self.Dni,self.Email,cifrado.hexdigest(),fecha)

        try:
            cursor.execute(sql,doctor)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]


        return result
        

    def identificar(self):
        # Login de usuarios
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.Password.encode('utf8'))

        # Datos para la consulta
        doctor = (self.Email, cifrado.hexdigest())

        cursor.execute(sql,doctor)
        result = cursor.fetchone()

        return result
