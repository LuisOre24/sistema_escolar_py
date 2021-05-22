from connection.connection import Connection

class Nivel:

    def __init__(self, nivel):
        self.nivel = nivel

    def all_niveles(self):
        try:
            conn = Connection('nivel')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nivel: {record[1]}')
                print('=====================')
        except Exception as e:
            print(e)


    def insert_nivel(self):
        
        try:  
            conn = Connection('nivel')
            conn.insert({
                'nivel' : self.nivel
            })

            print(f'se registro correctamente el nivel: {self.nivel}')

        except Exception as ex:
            print(ex)

nivel = Nivel('primaria')
nivel.insert_nivel()

