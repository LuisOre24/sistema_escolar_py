from connection.connection import Connection

class CursoRepo:

    def __init__(self,nombre_curso,id_categoria):
        self.nombre_curso = nombre_curso
        self.id_categoria = id_categoria
    
    def all_cursos(self):
        try:
            conn = Connection('curso')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Curso: {record[1]}')
                print(f'Categoria: {record[2]}')
                print(f'Estado: {record[3]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_curso(self,id):
        try:    
            conn = Connection('curso')
            records = conn.selectOne(id)

            print(f'ID: {records[0]}')
            print(f'Curso: {records[1]}')
            print(f'Categoria: {records[2]}')
            print(f'Estado: {records[3]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_curso(self, data):
        
        try:  
            conn = Connection('curso')
            conn.insert(data)

            print(f'se registro correctamente el curso')

        except Exception as ex:
            print(ex)


    def update_curso(self, id_object, data):

        conn = Connection('curso')

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
    

    def inhabilitar_curso(self,parameter, id_object):
        conn = Connection('curso')
        conn.disable(parameter, id_object)
        return True

    def cursos_habilitados(self):
        conn = Connection('curso')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'ID: {record[0]}')
                print(f'Curso: {record[1]}')
                print(f'Categoria: {record[2]}')
                print(f'Estado: {record[3]}')
                print('=====================')