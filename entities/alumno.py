from time import sleep
from repo.repo_alumno import *

class Alumno (AlumnoRepo):
    
    #CONSTRUCTOR
    def __init__(self, nombres):
        self.nombres = nombres

    #INTERFAZ CON EL USUARIO
    def interfazEstudiante(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA ESTUDIANTES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO ESTUDIANTE
            2 -> LISTAR ESTUDIANTES REGISTRADOS
            3 -> DESHABILITAR ESTUDIANTE
            4 -> ACTUALIZAR ESTUDIANTE
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_alumno()
            elif respuesta == "2":
                self.listEstudiante()
            elif respuesta == "3":
                self.deshabilitar_alumno()
            elif respuesta == "4":
                self.actualizar_alumno()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_alumno(self):

        try:
            print('''REGISTRO DE ALUMNOS
                POR FAVOR INGRESE LOS NOMBRES, APELLIDOS, FECHA DE NACIMIENTO, DNI, CORREO, TELEFONO DEL ALUMNO
            ''')
            nombre = input(">>Ingresar los nombres del Alumno: >>> ")
            apellido_paterno = input(">>Ingresar el apellido paterno del Alumno: >>> ")
            apellido_materno = input(">>Ingresar el apellido materno del Alumno: >>> ")
            fecha_nacimiento = input(">>Ingresar fecha de nacimiento (dd/mm/aaaa) del Alumno: >>> ")
            dni = int(input(">>Ingresar el DNI del Alumno: >>> "))
            correo = input(">>Ingresar el correo del Alumno (No indispensable): >>> ")
            telefono = input(">>Ingresar el numero de telefono del Alumno: >>> ")

            registro = {
                'nombres' : nombre,
                'apellido_paterno' : apellido_paterno,
                'apellido_materno' : apellido_materno,
                'fecha_nacimiento' : fecha_nacimiento,
                'dni' : dni,
                'correo' : correo,
                'telefono' : telefono,
                'estado' : True
            }

            self.insert_alumno(registro)
            print("Alumno registrado correctamente!")
            sleep(2)
            print("volviendo al menu Estudiantes")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazEstudiante()

        except Exception as ex:
            print(f'Error al registrar al Alumno. Error code: {str(ex)}')

    def listEstudiante(self):
        self.all_alumnos()

    def actualizar_alumno(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR ALUMNOS A MODIFICAR              ")
            print("*****************************************************")
            self.all_alumnos()
            id = input("Ingrese el ID del Alumno a modificar: \n>>> ")
            where = {
                'id_alumno' : id
            }
            
            alumno = self.one_alumno(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Nombres: {alumno[1]} >>> ')
            apellido_paterno = input(f'Apellido Paterno: {alumno[2]} >>> ')
            apellido_materno = input(f'Apellido Materno: {alumno[3]} >>> ')
            fecha_nacimiento = input(f'Fecha_Nacimiento: {alumno[4]} >>> ')
            dni = input(f'DNI: {alumno[5]} >>> ')
            correo = input(f'Correo: {alumno[6]} >>> ')
            telefono = input(f'Telefono: {alumno[7]} >>> ')
            estado = input(f'Estado: {alumno[8]} >>> ')

            registro = {
                'nombres' : nombres,
                'apellido_paterno' : apellido_paterno,
                'apellido_materno' : apellido_materno,
                'fecha_nacimiento' : fecha_nacimiento,
                'dni' : dni,
                'correo' : correo,
                'telefono' : telefono,
                'estado' : estado
            }

            self.update_alumno(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Alumno. Error code: {str(ex)}')

    def deshabilitar_alumno(self):
        try:
            print("******************************************")
            print("       LISTA DE ALUMNOS REGISTRADOS       ")
            self.alumnos_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DEL ALUMNO A INHABILITAR
            ''')

            estado = 'false'
            data = {
                'id_alumno' : id
            }
            self.inhabilitar_alumno(estado, data)

            print(f'Alumno indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar al alumno, error code: {str(ex)}')


