from connection.connection import Connection

class AlumnoRepo:

    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, dni, correo, telefono):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.correo = correo
        self.telefono = telefono

    def all_alumnos(self):
        try:
            conn = Connection('alumno')
            records = conn.select([])
            
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
    
    def one_alumno(self,id):
        try:    
            conn = Connection('alumno')
            records = conn.selectOne(id)

            print(f'ID: {records[0]}')
            print(f'Nombres: {records[1]}')
            print(f'Apellido_Paterno: {records[2]}')
            print(f'Apellido_Materno: {records[3]}')
            print(f'Fecha_Nacimiento: {records[4]}')
            print(f'DNI: {records[5]}')
            print(f'Correo: {records[6]}')
            print(f'Telefono: {records[7]}')
            print(f'Estado: {records[8]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_alumno(self, data):
        
        try:  
            conn = Connection('alumno')
            conn.insert(data)

            print(f'se registro correctamente al alumno')

        except Exception as ex:
            print(ex)


    def update_alumno(self, id_object, data):

        conn = Connection('alumno')

        list_where = []
        for field_name, field_value in id_object.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_where.append(f"{field_name}={field_value}")
        
        list_update = []
        for field_name, field_value in data.items():
            if isinstance(field_value, str):
                field_value = f"'{field_value}'"
            list_update.append(f"{field_name}={field_value}")
            
        query = f'''
            UPDATE {conn.table_name} SET {', '.join(list_update)}
            WHERE {' AND '.join(list_where)}
        '''
        conn.execute_query(query)
        return True

    def inhabilitar_alumno(self,parameter, id_object):
        conn = Connection('alumno')
        conn.disable(parameter, id_object)
        return True

    def alumnos_habilitados(self):
        conn = Connection('alumno')
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
