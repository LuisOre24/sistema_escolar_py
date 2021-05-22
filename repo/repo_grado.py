from connection.connection import Connection

class Grado:

    def __init__(self, grado, id_nivel):
        self.grado = grado
        self.id_nivel = id_nivel

    def all_grados(self):
        try:
            conn = Connection('grado')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Grado: {record[1]}')
                print(f'Nivel: {record[2]}')
                print('=====================')
        except Exception as e:
            print(e)


    def insert_grado(self):
        
        try:  
            conn = Connection('grado')
            conn.insert({
                'grado' : self.grado,
                'id_nivel' : self.id_nivel
            })

            print(f'se registro correctamente el grado: {self.grado}')

        except Exception as ex:
            print(ex)

grado = Grado('1er Grado', 1)
grado.insert_grado()

