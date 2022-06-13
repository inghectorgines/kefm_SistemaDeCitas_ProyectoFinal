from pydoc import describe


import citas.cita as modelo

class Acciones:

    def crear(self, doctor):
        print("\n*************************")
        print(f"Hola dr(a). {doctor[1]}!! Cree una cita...")

        nombre_paciente = input("Introduce el nombre del paciente: ")
        descripcion = input("Escribe el diagnóstico del paciente: ")
        fecha_cita  = input("Escribe la fecha de la cita (yyyy-mm-dd): ")

        cita = modelo.Cita(doctor[0], nombre_paciente, descripcion, fecha_cita)
        guardar = cita.create()

        if guardar[0] >= 1:
            print("\n***********************")
            print(f"¡Perfecto! Has guardado la cita: {cita.nombre_paciente}, para la fecha: {cita.fecha_cita}")
        else:
            print(f"\nNo se guardo su cita dr. {doctor[1]}, inténtelo más tarde.")

    def mostrar(self, doctor):
        print("\n***********************")
        print(f"\nHola dr(a). {doctor[1]}!!\nEstas son sus citas: \n ")
        print("***********************\n")

        cita = modelo.Cita(doctor[0])
        citas = cita.read()
        
        for cita in citas:
            if cita[0] >= 1:
                print(f"No. de cita: {cita[0]}")
                print(f"Nombre del paciente: {cita[2]}")
                print(f"Diagnóstico del paciente: {cita[3]}")
                print(f"Fecha de la cita: {cita[4]}\n")
                print("*************************")
            else:
                print("No hay notas, ingrese una.")

    def borrar(self, doctor):
        print("\n*************************")
        print(f"\nHola dr(a). {doctor[1]}!!\nAquí puede borrar sus citas")

        no_cita = input("Introduzca el no. de cita que desee borrar: ")

        cita = modelo.Cita(doctor[0])
        eliminar = cita.delete(no_cita)

        if eliminar[0] >= 1:
            print(f"Se borró la cita con número: {no_cita}")
        else:
            print("No se borró la cita, inténtelo más tarde...")
    
    def modificar(self,usuario,doctor):
        print("\n*********************")
        id = input(f"\nHola dr(a). {doctor[1]}!! el mo. de la cita a modificar: ")

        print("\nIngresa los datos a modificar: \n")

        nombre_paciente = input("Introduce nombre del paciente: ")
        descripcion = input("Escriba el diagnostico: ")
        fecha_cita = input("Fecha de la cita: ")

        cita = modelo.Cita(usuario[0])
        modificar = cita.update(nombre_paciente,descripcion,fecha_cita,id)

        if modificar[0] >= 1:
            print(f"\nLa Cita se actualizo correctamente!!!")
        else:
            print("No se pudo actualizar, prueba más tarde...")