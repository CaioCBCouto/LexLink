import csv
import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória entre duas datas
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Dados de exemplo
empresas = [
    'Tech Solutions Ltda', 'Green Energy Corp', 'Food & Beverages Inc', 
    'HealthCare Plus', 'EduFuture', 'TransLogistics', 'AquaPure', 
    'BuildRight', 'CosmoRetail', 'AgriGoods'
]
tipos_processos = [
    'Execução Fiscal', 'Trabalhista', 'Cível', 'Ambiental', 
    'Administrativo', 'Roubo', 'Fraude', 'Corrupção', 
    'Lavagem de Dinheiro', 'Homicídio'
]
descricoes_processos = {
    'Execução Fiscal': 'Processo movido pela Fazenda Pública para cobrar dívidas fiscais acumuladas ao longo dos anos, envolvendo diversas irregularidades financeiras e inadimplências tributárias significativas.',
    'Trabalhista': 'Ação judicial movida por ex-funcionário alegando assédio moral, horas extras não pagas, e rescisão contratual indevida, resultando em um litígio complexo e prolongado.',
    'Cível': 'Disputa judicial entre partes privadas sobre direitos e obrigações civis, incluindo contratos não cumpridos, danos materiais e pedidos de indenização substanciais.',
    'Ambiental': 'Processo envolvendo infrações às leis ambientais, tais como contaminação de solo e água, desmatamento ilegal e emissão excessiva de poluentes, com implicações regulatórias severas.',
    'Administrativo': 'Ações movidas contra a empresa por órgãos reguladores devido a irregularidades administrativas, incluindo licitações fraudulentas e descumprimento de normas setoriais.',
    'Roubo': 'Investigação criminal sobre roubo de propriedade intelectual e bens valiosos da empresa, envolvendo suspeitos internos e externos, e causando impacto financeiro considerável.',
    'Fraude': 'Processo por fraude financeira e contábil, onde se apuram manipulações de balanços, evasão fiscal e outras práticas ilícitas com graves consequências legais e econômicas.',
    'Corrupção': 'Investigação de práticas corruptas envolvendo suborno de funcionários públicos, com objetivo de obter vantagens ilícitas em contratos governamentais, gerando ampla repercussão negativa.',
    'Lavagem de Dinheiro': 'Caso de lavagem de dinheiro através de operações comerciais e financeiras complexas, visando ocultar a origem ilícita de fundos, com extensas ramificações internacionais.',
    'Homicídio': 'Investigação criminal relacionada a homicídio ocorrido nas dependências da empresa, envolvendo funcionários e resultando em graves implicações legais e reputacionais.'
}
status_processos = ['Em andamento', 'Concluído']
valores_envolvidos = [5000, 15000, 30000, 50000, 75000, 100000, 250000, 500000, 1000000]
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
departamentos = ['Financeiro', 'Recursos Humanos', 'Operacional', 'Marketing', 'Vendas', 'Jurídico']
resultados = ['Multa', 'Acordo', 'Absolvição', 'Condenação', 'Arquivamento']

# Gerar registros para o CSV
registros = []
for empresa in empresas:
    for _ in range(30):  # 30 registros por empresa
        tipo_processo = random.choice(tipos_processos)
        descricao_processo = descricoes_processos[tipo_processo]
        status_processo = random.choice(status_processos)
        data_inicio = random_date(datetime(2015, 1, 1), datetime(2023, 12, 31))
        data_conclusao = (random_date(data_inicio, datetime(2024, 12, 31)) 
                          if status_processo == 'Concluído' else '')
        valor_envolvido = f'R$ {random.choice(valores_envolvidos):,.2f}'.replace(',', '.')
        advogado_responsavel = f'Dr. {random.choice(["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima"])}'
        tribunal = f'Tribunal {random.choice(["de Justiça", "Regional", "Superior", "do Trabalho", "Federal"])}'
        regiao = random.choice(regioes)
        departamento = random.choice(departamentos)
        resultado = random.choice(resultados) if status_processo == 'Concluído' else ''
        custas_judiciais = f'R$ {random.choice(valores_envolvidos) * 0.1:,.2f}'.replace(',', '.')
        data_registro = random_date(datetime(2015, 1, 1), datetime(2023, 12, 31)).strftime('%Y-%m-%d')
        numero_processo = f'{random.randint(10000, 99999)}-{random.randint(2015, 2023)}'

        registros.append([
            empresa,
            tipo_processo,
            descricao_processo,
            status_processo,
            data_inicio.strftime('%Y-%m-%d'),
            data_conclusao.strftime('%Y-%m-%d') if data_conclusao else '',
            valor_envolvido,
            advogado_responsavel,
            tribunal,
            regiao,
            departamento,
            resultado,
            custas_judiciais,
            data_registro,
            numero_processo
        ])

# Escrever o CSV
with open('processos_juridicos_completos.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Nome da Empresa', 'Tipo de Processo', 'Descrição do Processo', 'Status', 
        'Data de Início', 'Data de Conclusão', 'Valor Envolvido', 'Advogado Responsável', 
        'Tribunal', 'Região', 'Departamento Envolvido', 'Resultado', 'Custas Judiciais', 
        'Data de Registro', 'Número do Processo'
    ])
    writer.writerows(registros)