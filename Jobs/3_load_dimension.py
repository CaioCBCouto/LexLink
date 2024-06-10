import psycopg2
import os

# Database connection details
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'analise_juridica'
DB_PORT = 54320

# Function to connect to the PostgreSQL database
def get_connection():
    try:
        conn = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME, port=DB_PORT)
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Database connection failed: {e}")
        return None

# Function to create tables in the PostgreSQL database
def create_tables(conn):
    if conn is not None:
        cursor = conn.cursor()
        try:
            # Iterate over all files in the Tables directory
            for filename in os.listdir("Tables"):
                if filename.endswith(".sql"):
                    filepath = os.path.join("Tables", filename)
                    with open(filepath, "r") as file:
                        table_definition = file.read()
                        cursor.execute(table_definition)
            conn.commit()
            print("Tables created successfully.")
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to create tables: {e}")
        finally:
            cursor.close()

# Function to insert data into the dim_empresa table
def insert_empresa(conn, empresas):
    if conn is not None:
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO dim_empresa (nome_da_empresa) VALUES (%s) RETURNING empresa_id
            """
            empresa_ids = {}
            for empresa in empresas:
                cursor.execute(insert_query, (empresa,))
                empresa_id = cursor.fetchone()[0]
                empresa_ids[empresa] = empresa_id
            conn.commit()
            print(f"Inserted {len(empresas)} empresas successfully.")
            return empresa_ids
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert empresas: {e}")
            return {}
        finally:
            cursor.close()

# Function to insert data into the dim_processo table
def insert_processo(conn, processos):
    if conn is not None:
        cursor = conn.cursor()
        try:
            
            insert_query = """
                INSERT INTO dim_processo (tipo_de_processo, prioridade, palavras_chave, tempo_medio_resolucao_mes, 
                                          taxa_de_sucesso, custos_medios, numero_medio_testemunhas, complexidade_media)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING processo_id
            """
            processo_ids = {}
            for processo in processos:
                cursor.execute(insert_query, processo)
                processo_id = cursor.fetchone()[0]
                processo_ids[processo[0]] = processo_id
            conn.commit()
            print(f"Inserted {len(processos)} processos successfully.")
            return processo_ids
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert processos: {e}")
            return {}
        finally:
            cursor.close()

# Function to insert data into the dim_advogado table
def insert_advogado(conn, advogados):
    if conn is not None:
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO dim_advogado (nome_advogado) VALUES (%s) RETURNING advogado_id
            """
            advogado_ids = {}
            for advogado in advogados:
                cursor.execute(insert_query, (advogado,))
                advogado_id = cursor.fetchone()[0]
                advogado_ids[advogado] = advogado_id
            conn.commit()
            print(f"Inserted {len(advogados)} advogados successfully.")
            return advogado_ids
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert advogados: {e}")
            return {}
        finally:
            cursor.close()

# Function to insert data into the dim_tribunal table
def insert_tribunal(conn, tribunais):
    if conn is not None:
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO dim_tribunal (nome_tribunal, regiao) VALUES (%s, %s) RETURNING tribunal_id
            """
            tribunal_ids = {}
            for tribunal in tribunais:
                cursor.execute(insert_query, tribunal)
                tribunal_id = cursor.fetchone()[0]
                tribunal_ids[tribunal] = tribunal_id
            conn.commit()
            print(f"Inserted {len(tribunais)} tribunais successfully.")
            return tribunal_ids
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert tribunais: {e}")
            return {}
        finally:
            cursor.close()

# Function to insert data into the dim_departamento table
def insert_departamento(conn, departamentos):
    if conn is not None:
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO dim_departamento (nome_departamento) VALUES (%s) RETURNING departamento_id
            """
            departamento_ids = {}
            for departamento in departamentos:
                cursor.execute(insert_query, (departamento,))
                departamento_id = cursor.fetchone()[0]
                departamento_ids[departamento] = departamento_id
            conn.commit()
            print(f"Inserted {len(departamentos)} departamentos successfully.")
            return departamento_ids
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert departamentos: {e}")
            return {}
        finally:
            cursor.close()

def insert_data(conn, data, column_names, batch_size=100000):
    if conn is not None:
        cursor = conn.cursor()
        try:
            insert_fato_processo_query = """
                INSERT INTO fato_processo_juridico (empresa_id, processo_id, advogado_id, tribunal_id, departamento_id, 
                                                    data_inicio, data_conclusao, status, descricao_processo, 
                                                    valor_envolvido, resultado, custas_judiciais, data_registro, 
                                                    numero_processo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for index, row in enumerate(data):
                row_values = {column_names[i]: row[i] for i in range(len(column_names))}
                cursor.execute(insert_fato_processo_query, (
                    row_values['empresa_id'], row_values['processo_id'], row_values['advogado_id'], row_values['tribunal_id'],
                    row_values['departamento_id'], row_values['data_inicio'], row_values['data_conclusao'], 
                    row_values['status'], row_values['descricao_processo'], row_values['valor_envolvido'], 
                    row_values['resultado'], row_values['custas_judiciais'], row_values['data_registro'], 
                    row_values['numero_processo']
                ))

                if (index + 1) % batch_size == 0:
                    conn.commit()
                    print(f"Processed {index+1} rows")

            conn.commit()
            print(f"Final data insertion complete. Processed {len(data)} rows")
        except psycopg2.DatabaseError as e:
            conn.rollback()
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()

# Function to load data from PostgreSQL table
def load_data_from_postgres(table_name):
    print(f"Loading data from table {table_name}...")
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description] if cursor.description else []
            cursor.close()
            return data, column_names
        except psycopg2.Error as e:
            print(f"An error occurred while accessing the database: {e}")
            return [], []  # Return empty lists in case of error
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")
        return [], []  # Return empty lists if connection could not be established

# Main function to manage the database setup
def main():
    conn = get_connection()
    if conn:
        create_tables(conn)

        # Load data from processos_juridicos_info
        info_data, info_columns = load_data_from_postgres('processos_juridicos_info')
        processos = [(row[info_columns.index('Tipo de Processo')],
                      row[info_columns.index('Prioridade')],
                      row[info_columns.index('Palavras-Chave')],
                      row[info_columns.index('Tempo Médio de Resolução (meses)')],
                      row[info_columns.index('Taxa de Sucesso')],
                      row[info_columns.index('Custos Médios')],
                      row[info_columns.index('Número Médio de Testemunhas')],
                      row[info_columns.index('Complexidade Média')]) for row in info_data]
        # remove R$ from 'Custos Médios' column
        processos = [(row[0], row[1], row[2], row[3], row[4], row[5].replace('R$ ', '').replace('.', '').replace(',', '.'), row[6], row[7]) for row in processos]
        processo_ids = insert_processo(conn, processos)

        # Load data from processos_juridicos_completos
        completos_data, completos_columns = load_data_from_postgres('processos_juridicos_completos')
        empresas = set(row[completos_columns.index('Nome da Empresa')] for row in completos_data)
        empresa_ids = insert_empresa(conn, list(empresas))

        advogados = set(row[completos_columns.index('Advogado Responsável')] for row in completos_data)
        advogado_ids = insert_advogado(conn, list(advogados))

        tribunais = set((row[completos_columns.index('Tribunal')], row[completos_columns.index('Região')]) for row in completos_data)
        tribunal_ids = insert_tribunal(conn, list(tribunais))

        departamentos = set(row[completos_columns.index('Departamento Envolvido')] for row in completos_data)
        departamento_ids = insert_departamento(conn, list(departamentos))

        fato_data = []
        for row in completos_data:
            try:
                fato_data.append((
                    empresa_ids[row[completos_columns.index('Nome da Empresa')]],
                    processo_ids[row[completos_columns.index('Tipo de Processo')]],
                    advogado_ids[row[completos_columns.index('Advogado Responsável')]],
                    tribunal_ids[(row[completos_columns.index('Tribunal')], row[completos_columns.index('Região')])],
                    departamento_ids[row[completos_columns.index('Departamento Envolvido')]],
                    row[completos_columns.index('Data de Início')],
                    row[completos_columns.index('Data de Conclusão')],
                    row[completos_columns.index('Status')],
                    row[completos_columns.index('Descrição do Processo')],
                    row[completos_columns.index('Valor Envolvido')].replace('R$ ', '').replace('.', '').replace(',', '.'),
                    row[completos_columns.index('Resultado')],
                    row[completos_columns.index('Custas Judiciais')].replace('R$ ', '').replace('.', '').replace(',', '.'),
                    row[completos_columns.index('Data de Registro')],
                    row[completos_columns.index('Número do Processo')]
                ))
            except KeyError as e:
                print(f"Error inserting row: {e}")
                # Handle the error appropriately (e.g., log it, skip the row, etc.)
        # remove R$ from 'Valor Envolvido' and 'Custas Judiciais' column
        fato_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9].replace('R$ ', '').replace('.', '').replace(',', '.'), row[10], row[11].replace('R$ ', '').replace('.', '').replace(',', '.'), row[12], row[13]) for row in fato_data]
        
        insert_data(conn, fato_data, [
            'empresa_id', 'processo_id', 'advogado_id', 'tribunal_id', 'departamento_id',
            'data_inicio', 'data_conclusao', 'status', 'descricao_processo',
            'valor_envolvido', 'resultado', 'custas_judiciais', 'data_registro',
            'numero_processo'
        ])

        conn.close()

if __name__ == "__main__":
    main()
