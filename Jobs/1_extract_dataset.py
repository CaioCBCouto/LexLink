import subprocess
import shutil
import os

# Verifica se a pasta 'Data' existe e, se não, a cria
if not os.path.exists('Data'):
    os.makedirs('Data')

# Executar processo_juridico.py
subprocess.run(['python', 'criadorCSV.py'])

# Executar processos_info.py
subprocess.run(['python', 'criadorCSVinfos.py'])

# Mover os arquivos gerados para a pasta 'Data'
shutil.move('processos_juridicos_completos.csv', 'Data/processos_juridicos_completos.csv')
shutil.move('processos_juridicos_info.csv', 'Data/processos_juridicos_info.csv')

print("Arquivos gerados e movidos para a pasta 'Data'.")