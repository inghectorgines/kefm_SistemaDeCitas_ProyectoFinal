from ast import alias
import doctores.doctor as modelo
import citas.acciones

class Acciones:

    def registro(self):
        print("Registrar a un doctor...")

        nombre = input("¿Cuál es su nombre?: ")
        apellidos = input("¿Cuales son los apellido?: ")
        especialidad = input("¿Cuál es la especialidad?: ")
        no_consultorio = input("No. del consultorio: ")
        dni = input("No. de empleado: ")
        email = input("Introduce su email: ")
        password = input("Introduce su contraseña: ")

        doctor = modelo.Doctores(nombre, apellidos, especialidad, no_consultorio, dni, email, password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto dr. {registro[1].Nombre} te ha registrado con el email {registro[1].Email}")
        else:
            print("\nNo te has registrado correctamente!!!")

    def login(self):
        print("\nIdentificate en el sistema...")

        try:
            email = input("Introduce su email: ")
            password = input("Introduce su contraseña: ")

            doctores = modelo.Doctores('','','','','',email,password)
            login = doctores.identificar()

            if email == login[6]:
                print(f"\nBienvenido dr(a). {login[1]}, se ha registrado en el sistema con el no. de empleado: {login[5]}.")

                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("\nLogin Incorrecto!!! Intentalo más tarde.")

    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles para el doctor:
            1.- Crear una cita 
            2.- Mostrar citas 
            3.- Modificar citas 
            4.- Eliminar cita 
            5.- Salir
        """)

        accion = input("Escriba el número de la accion a realizar: ")
        hazEl = citas.acciones.Acciones()

        if accion == "1":
            # print("Vamos a crear nota")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "2":
            #print("Vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "3":
            #print("Vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "4":
            #print("Vamos a eliminar")
            hazEl.modificar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "5":
            exit()
