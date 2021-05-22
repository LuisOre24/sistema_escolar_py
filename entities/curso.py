from time import sleep
from repo.repo_curso import CursoRepo

class Curso (CursoRepo):
    
    #CONSTRUCTOR
    def __init__(self, nombre):
        self.nombre = nombre

    #INTERFAZ CON EL USUARIO
    def interfazCurso(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA CURSOS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UN NUEVO CURSO
            2 -> LISTAR CURSOS REGISTRADOS
            3 -> DESHABILITAR CURSO
            4 -> ACTUALIZAR CURSO
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_curso()
            elif respuesta == "2":
                self.listCurso()
            elif respuesta == "3":
                self.deshabilitar_curso()
            elif respuesta == "4":
                self.actualizar_curso()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_curso(self):

        try:
            print('''REGISTRO DE CURSOS
                POR FAVOR INGRESE EL NOMBRE DEL CURSO
            ''')
            nombre = input(">>Ingresar el nombre del Curso: >>> ")
            id_categoria = input(">>Ingresar la categoria del Curso: >>> ")
            

            registro = {
                'curso' : nombre,
                'id_categoria' : id_categoria,
                'estado' : True
            }

            self.insert_curso(registro)
            print("Curso registrado correctamente!")
            sleep(2)
            print("volviendo al menu Cursos")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazCurso()

        except Exception as ex:
            print(f'Error al registrar al Curso. Error code: {str(ex)}')

    def listCurso(self):
        self.all_cursos()

    def actualizar_curso(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR CURSOS A MODIFICAR              ")
            print("*****************************************************")
            self.all_cursos()
            id = input("Ingrese el ID del Curso a modificar: \n>>> ")
            where = {
                'id_curso' : id
            }
            
            curso = self.one_curso(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Curso: {curso[1]} >>> ')
            categoria = input(f'Categoria: {curso[2]} >>> ')
            estado = input(f'Estado: {curso[3]} >>> ')

            registro = {
                'curso' : nombres,
                'id_categoria' : categoria,
                'estado' : estado
            }

            self.update_curso(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Curso. Error code: {str(ex)}')

    def deshabilitar_curso(self):
        try:
            print("******************************************")
            print("       LISTA DE CURSOS REGISTRADOS       ")
            self.cursos_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DEL CURSO A INHABILITAR
            ''')

            estado = 'false'
            data = {
                'id_curso' : id
            }
            self.inhabilitar_curso(estado, data)

            print(f'Curso indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar al curso, error code: {str(ex)}')


