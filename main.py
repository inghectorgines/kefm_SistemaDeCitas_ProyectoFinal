## Descargo y procedo a revisar y calificar.


"""
Proyecto python + MySQL:
1.- Abrir el asistente
2.- Login y registro
3.- Si elegimos registro, crear un usuario en la BD
4.- Si elegimos login, indetificar al usuario y nos preguntara
5.- Crear nota, mostrar notas, o borrarlas
"""
from doctores import acciones

print("**********************************************")
print("Mi nombre es Karla Elena Francisco Manuel\nCurso el 9no cuatrimestre Grupo A\nEl nombre de la materia es Desarrollo para Dispositivos Inteligentes (DDI)\nLa fecha de hoy es 11/06/2022\n")

print("***********************************************")
print("Proyecto final 1er parcial\n")

print("""
Acciones disponibles:
    1.- Registrar doctor
    2.- Iniciar sesión 
""")

hazEl = acciones.Acciones()

accion = input("Escriba el número de la acción a realizar: ")

if accion == "1":
    hazEl.registro()
elif accion == "2":
    hazEl.login()

