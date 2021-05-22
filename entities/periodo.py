from time import sleep
from repo.repo_periodo import PeriodoRepo

class Periodo (PeriodoRepo):
    
    #CONSTRUCTOR
    def __init__(self, mes):
        self.mes = mes

    #INTERFAZ CON EL USUARIO
    def interfazPeriodo(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA PERIODOS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UN NUEVO PERIODO
            2 -> LISTAR PERIODOS REGISTRADOS
            3 -> DESHABILITAR PERIODO
            4 -> ACTUALIZAR PERIODO
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_periodo()
            elif respuesta == "2":
                self.listPeriodo()
            elif respuesta == "3":
                self.deshabilitar_periodo()
            elif respuesta == "4":
                self.actualizar_periodo()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_periodo(self):

        try:
            print('''REGISTRO DE PERIODOS
                POR FAVOR INGRESE EL MES Y AÑO
            ''')
            mes = input(">>Ingresar el mes del Periodo: >>> ")
            año = input(">>Ingresar año del Periodo: >>> ")
            

            registro = {
                'mes' : mes,
                'año' : año,
                'estado' : True
            }

            self.insert_periodo(registro)
            print("Periodo registrado correctamente!")
            sleep(2)
            print("volviendo al menu Periodos")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazPeriodo()

        except Exception as ex:
            print(f'Error al registrar al Curso. Error code: {str(ex)}')

    def listPeriodo(self):
        self.all_periodos()

    def actualizar_periodo(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR PERIODOS A MODIFICAR              ")
            print("*****************************************************")
            self.all_periodos()
            id = input("Ingrese el ID del Periodo a modificar: \n>>> ")
            where = {
                'id_periodo' : id
            }
            
            periodo = self.one_periodo(where)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            mes = input(f'Mes: {periodo[1]} >>> ')
            año = input(f'Año: {periodo[2]} >>> ')
            estado = input(f'Estado: {periodo[3]} >>> ')

            registro = {
                'mes' : mes,
                'año' : año,
                'estado' : estado
            }

            self.update_periodo(where, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Periodo. Error code: {str(ex)}')

    def deshabilitar_periodo(self):
        try:
            print("******************************************")
            print("       LISTA DE PERIODOS REGISTRADOS       ")
            self.periodos_habilitados()
            print("******************************************")
            id = input(f'''
                POR FAVOR INGRESE EL ID DEL PERIODO A INHABILITAR
            ''')

            estado = 'false'
            data = {
                'id_periodo' : id
            }
            self.inhabilitar_periodo(estado, data)

            print(f'Periodo indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar al periodo, error code: {str(ex)}')


