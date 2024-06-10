import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine

# Defina as suas variáveis de conexão com o banco de dados
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'analise_juridica'
DB_PORT = 54320

# Localização dos arquivos
current_dir = os.path.dirname(os.path.realpath(__file__))
pipeline_dir = os.path.join(current_dir, "..")
data_dir = os.path.join(pipeline_dir, "Data")

conn = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME, port=DB_PORT)

# Leitura do CSV
df_completos = pd.read_csv(f'{data_dir}/processos_juridicos_completos.csv')
df_info = pd.read_csv(f'{data_dir}/processos_juridicos_info.csv')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

df_completos.to_sql('processos_juridicos_completos', engine, if_exists='replace', index=False)
df_info.to_sql('processos_juridicos_info', engine, if_exists='replace', index=False)

conn.close()
