from repo.repo_docente import *
from time import sleep


class Docente(DocenteRepo):
    def __init__(self, nombres, edad, dni):
        self.nombres = nombres
        self.edad = edad
        self.dni = dni


    def interfazDocente(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA DOCENTES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO DOCENTE
            2 -> LISTAR DOCENTES REGISTRADOS
            3 -> RETORNAR AL MENU PRINCIPAL
            4 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")
            if respuesta == "1":
                self.registar_docente()
            elif respuesta == "2":
                self.listDocente()
            elif respuesta == "3":
                self.deshabilitar_docente()
            elif respuesta == "4":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_docente(self):
        try:
            print('''REGISTRO DE DOCENTES
                POR FAVOR INGRESE LOS NOMBRES, APELLIDOS, FECHA DE NACIMIENTO, DNI, CORREO, TELEFONO DEL DOCENTE
            ''')
            nombre = input(">>Ingresar los nombres del Docente: >>> ")
            apellido_paterno = input(">>Ingresar el apellido paterno del Docente: >>> ")
            apellido_materno = input(">>Ingresar el apellido materno del Docente: >>> ")
            fecha_nacimiento = input(">>Ingresar fecha de nacimiento (dd/mm/aaaa) del Docente: >>> ")
            dni = int(input(">>Ingresar el DNI del Docente: >>> "))
            correo = input(">>Ingresar el correo del Docente (No indispensable): >>> ")
            telefono = input(">>Ingresar el numero de telefono del Docente: >>> ")

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

            self.insert_docente(registro)
            print("volviendo al menu Docentes")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazDocente()
        except Exception as ex:
            print(f'Error al registrar Docente. Error Code: {str(ex)}')

    def listDocente(self):
        self.all_docentes()

    def actualizar_docente(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR DOCENTES A MODIFICAR             ")
            print("*****************************************************")
            self.all_alumnos()
            id = input("Ingrese el ID del Docente: \n>")
            where = {
                'id_docente' : id
            }
            
            docente = self.one_docente(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Nombres: {docente[1]} >>> ')
            apellido_paterno = input(f'Apellido Paterno: {docente[2]} >>> ')
            apellido_materno = input(f'Apellido Materno: {docente[3]} >>> ')
            fecha_nacimiento = input(f'Fecha_Nacimiento: {docente[4]} >>> ')
            dni = input(f'DNI: {docente[5]} >>> ')
            correo = input(f'Correo: {docente[6]} >>> ')
            telefono = input(f'Telefono: {docente[7]} >>> ')
            estado = input(f'Estado: {docente[8]} >>> ')

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

            self.actualizar_docente(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Docente. Error code: {str(ex)}')


    def deshabilitar_docente(self):

        try:
            print("******************************************")
            print("            LISTA DE DOCENTES             ")
            self.docentes_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DEL DOCENTE A INHABILITAR
            ''')
            estado = 'false'
            data = {
                'id_docente' : id
            }
            self.inhabilitar_docente(estado, data)
        except Exception as ex:
            print(f'Error al deshabilitar Docente. Error Code: {str(ex)}')
