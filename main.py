from entities.curso import Curso
from entities.periodo import Periodo
from entities.categoria import Categoria
from entities.docente import Docente
from entities.alumno import Alumno

from time import sleep

class Start(Alumno, Docente, Curso, Periodo, Categoria):

    def __init__(self):
        try:
            print('''
            BIENVENIDO AL SISTEMA DE GESTION ESCOLAR
            ¿QUE ES LO QUE DESEA GESTIONAR?
            1 -> GESTION PARA DOCENTES
            2 -> GESTION PARA ESTUDIANTES
            3 -> GESTION DE CURSOS
            4 -> GESTION DE PERIODOS
            5 -> GESTION DE CATEGORIAS
            6 -> SALIR DEL SISTEMA
            ''')
            opcion = input(">>")
            if opcion == "1":
                self.interfazDocente()
            if opcion == "2":
                self.interfazEstudiante()
            if opcion == "3":
                self.interfazCurso()
            if opcion == "4":
                self.interfazPeriodo()
            if opcion == "5":
                self.interfazCategoria()
            if opcion == "6":
                print("Saliendo del Sistema ....")
                sleep(2)
                exit()
        except KeyboardInterrupt:
            print("\nForzando salida del sistema")
    
Start()