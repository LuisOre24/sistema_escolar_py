from connection.connection import Connection

class Seccion:

    def __init__(self, seccion):
        self.seccion = seccion

    def all_secciones(self):
        try:
            conn = Connection('seccion')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Seccion: {record[1]}')
                print('=====================')
        except Exception as e:
            print(e)


    def insert_seccion(self):
        seccion = self.seccion.upper()
        try:  
            conn = Connection('seccion')
            conn.insert({
                'seccion' : seccion
            })

            print(f'se registro correctamente la seccion: {seccion}')

        except Exception as ex:
            print(ex)

seccion = Seccion('a')
seccion.insert_seccion()
