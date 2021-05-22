from time import sleep
from repo.repo_categoria import CategoriaRepo

class Categoria (CategoriaRepo):
    
    #CONSTRUCTOR
    def __init__(self, descripcion):
        self.descripcion = descripcion

    #INTERFAZ CON EL USUARIO
    def interfazCategoria(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA CATEGORIAS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UNA NUEVA CATEGORIA
            2 -> LISTAR CATEGORIAS REGISTRADAS
            3 -> DESHABILITAR CATEGORIA
            4 -> ACTUALIZAR CATEGORIA
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_categoria()
            elif respuesta == "2":
                self.listCategoria()
            elif respuesta == "3":
                self.deshabilitar_categoria()
            elif respuesta == "4":
                self.actualizar_categoria()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_categoria(self):

        try:
            print('''REGISTRO DE CATEGORIA
                POR FAVOR INGRESE UNA DESCRIPCION
            ''')
            descripcion = input(">>Ingresar DESCRIPCION DE LA CATEGORIA: >>> ")
            
            

            registro = {
                'descripcion' : descripcion,
                'estado' : True
            }

            self.insert_categoria(registro)
            print("Categoria registrada correctamente!")
            sleep(2)
            print("volviendo al menu Categorias")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazCategoria()

        except Exception as ex:
            print(f'Error al registrar la Categoria. Error code: {str(ex)}')

    def listCategoria(self):
        self.all_categorias()

    def actualizar_categoria(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR CATEGORIAS A MODIFICAR              ")
            print("*****************************************************")
            self.all_categorias()
            id = input("Ingrese el ID de la Categoria a modificar: \n>>> ")
            where = {
                'id_categoria' : id
            }
            
            Categoria = self.one_categoria(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            descipcion = input(f'Descripcion: {Categoria[1]} >>> ')
            estado = input(f'Estado: {Categoria[2]} >>> ')

            registro = {
                'descripcion' : descipcion,
                'estado' : estado
            }

            self.update_categoria(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos de la Categoria. Error code: {str(ex)}')

    def deshabilitar_categoria(self):
        try:
            print("******************************************")
            print("       LISTA DE CATEGORIAS REGISTRADOS       ")
            self.categorias_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DE LA CATEGORIA A INHABILITAR
            ''')

            estado = 'false'
            data = {
                'id_categoria' : id
            }
            self.inhabilitar_categoria(estado, data)

            print(f'Categoria indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar la Categoria, error code: {str(ex)}')


