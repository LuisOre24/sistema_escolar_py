from connection.connection import Connection

class CategoriaRepo:

    def __init__(self,descripcion):
        self.descripcion = descripcion
           
    def all_categorias(self):
        try:
            conn = Connection('categoria')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Descipcion: {record[1]}')
                print(f'Estado: {record[2]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_categoria(self,id):
        try:    
            conn = Connection('categoria')
            records = conn.selectOne(id)

            print(f'ID: {records[0]}')
            print(f'Descripcion: {records[1]}')
            print(f'Estado: {records[2]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_categoria(self, data):
        
        try:  
            conn = Connection('categoria')
            conn.insert(data)

            print(f'se registro correctamente la categoria')

        except Exception as ex:
            print(ex)


    def update_categoria(self, id_object, data):

        conn = Connection('categoria')

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
    

    def inhabilitar_categoria(self,parameter, id_object):
        conn = Connection('categoria')
        conn.disable(parameter, id_object)
        return True

    def categorias_habilitados(self):
        conn = Connection('categoria')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'ID: {record[0]}')
                print(f'Descripcion: {record[1]}')
                print(f'Estado: {record[2]}')
                print('=====================')