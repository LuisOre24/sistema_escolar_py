from connection.connection import Connection

class PeriodoRepo:

    def __init__(self,mes,año):
        self.mes = mes
        self.año = año
    
    def all_periodos(self):
        try:
            conn = Connection('periodo')
            records = conn.select([])
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Mes: {record[1]}')
                print(f'Año: {record[2]}')
                print(f'Estado: {record[3]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_periodo(self,id):
        try:    
            conn = Connection('periodo')
            records = conn.selectOne(id)

            print(f'ID: {records[0]}')
            print(f'Mes: {records[1]}')
            print(f'Año: {records[2]}')
            print(f'Estado: {records[3]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_periodo(self, data):
        
        try:  
            conn = Connection('periodo')
            conn.insert(data)

            print(f'se registro correctamente el periodo')

        except Exception as ex:
            print(ex)


    def update_periodo(self, id_object, data):

        conn = Connection('periodo')

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
    

    def inhabilitar_periodo(self,parameter, id_object):
        conn = Connection('periodo')
        conn.disable(parameter, id_object)
        return True

    def periodos_habilitados(self):
        conn = Connection('periodo')
        query = f'''
            SELECT * FROM {conn.table_name} WHERE estado = 'true'
        '''
        conn.cursor.execute(query)
        records = conn.cursor.fetchall()

        for record in records:
                print(f'ID: {record[0]}')
                print(f'Mes: {record[1]}')
                print(f'Año: {record[2]}')
                print(f'Estado: {record[3]}')
                print('=====================')