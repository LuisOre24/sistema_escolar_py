from connection.connection import Connection

class DocenteRepo:

    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, dni, correo, telefono, estado):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.correo = correo
        self.telefono = telefono
        self.estado = estado

    def all_docentes(self):
        
        try:
            conn = Connection('docente')
            records = conn.select([])
            #items = records

            """ for item in items:
                print(item) """
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombres: {record[1]}')
                print(f'Apellido_Paterno: {record[2]}')
                print(f'Apellido_Materno: {record[3]}')
                print(f'Fecha_Nacimiento: {record[4]}')
                print(f'DNI: {record[5]}')
                print(f'Correo: {record[6]}')
                print(f'Telefono: {record[7]}')
                print(f'Estado: {record[8]}')
                print('=====================')
        except Exception as e:
            print(e)


    def one_docente(self,id):
        conn = Connection('docente')
        conn.selectOne(id)

    def insert_docente(self, data):
        
        try:  
            conn = Connection('docente')
            conn.insert(data)

            print(f'se registro correctamente al docente')

        except Exception as ex:
            print(ex)


    def update_docente(self, id_object, data):
        
        conn = Connection('docente')
        conn.update(id_object, data)
        return True

    def inhabilitar_docente(self,parameter, id_object):
        conn = Connection('docente')
        conn.disable(parameter, id_object)
        return True

    def docentes_habilitados(self):

        conn = Connection('docente')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombres: {record[1]}')
                print(f'Apellido_Paterno: {record[2]}')
                print(f'Apellido_Materno: {record[3]}')
                print(f'Fecha_Nacimiento: {record[4]}')
                print(f'DNI: {record[5]}')
                print(f'Correo: {record[6]}')
                print(f'Telefono: {record[7]}')
                print(f'Estado: {record[8]}')
                print('=====================')
    