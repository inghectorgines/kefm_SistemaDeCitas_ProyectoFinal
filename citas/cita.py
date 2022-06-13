import re
from sqlite3 import connect
import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor= connect[1]

class Cita:

    def __init__(self, doctores_id, nombre_paciente="", descripcion="", fecha_cita=""):
        self.doctores_id = doctores_id
        self.nombre_paciente = nombre_paciente
        self.descripcion = descripcion
        self.fecha_cita = fecha_cita

    def create(self):
        sql = "INSERT INTO citas VALUES (null, %s, %s, %s, %s, NOW())"
        cita = (self.doctores_id, self.nombre_paciente, self.descripcion, self.fecha_cita)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]

    def read(self):
        sql = f"SELECT* FROM citas WHERE doctores_id = {self.doctores_id}"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def update(self,nombre_paciente, descripcion, fecha_cita, id):
        sql = f"UPDATE citas SET nombre_paciente = '{nombre_paciente}',descripcion = '{descripcion}', fecha_cita = '{fecha_cita}' WHERE id = {id}"

        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    
    def delete(self, id_cita):
        sql =  f"DELETE FROM citas WHERE id = {id_cita}"

        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result



