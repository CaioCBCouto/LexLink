import csv
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Dados de exemplo
empresas = [
    'Tech Solutions Ltda', 'Green Energy Corp', 'Food & Beverages Inc', 
    'HealthCare Plus', 'EduFuture', 'TransLogistics', 'AquaPure', 
    'BuildRight', 'CosmoRetail', 'AgriGoods', 'MediCare Ltd', 'CleanTech Co', 
    'FutureCom', 'BioLife Sciences', 'Urban Innovations', 'EcoTech Systems', 
    'NanoTech Labs', 'SolarWave Energy', 'QuantumLeap Technologies', 'GreenLeaf Enterprises', 
    'SmartHome Solutions', 'GlobalTrade Ltd', 'NextGen AI', 'AgroGrow', 
    'SecureNet', 'RoboMotive', 'DigitalWorld', 'UrbanSpaces', 'RenewPower', 'BlueOcean Inc',
    'Soluciona TI', 'Energia Verde', 'Alimentos & Bebidas Ltda', 'Saúde e Bem-Estar', 'EduFuturo', 
    'TransLogística', 'Água Pura', 'ConstróiCerto', 'VarejoCosmos', 'AgroProdutos', 'MediCuidar', 
    'Tecnologia Limpa', 'FuturoCom', 'CiênciasBioVida', 'Inovações Urbanas', 'SistemasEcoTech', 
    'LabsNanoTec', 'EnergiaSolar', 'TecnologiasQuantum', 'EmpreendimentosFolhaVerde', 
    'SoluçõesCasaInteligente', 'ComércioGlobal', 'PróximaGeração AI', 'CrescimentoAgro', 
    'RedeSegura', 'RoboMotiva', 'MundoDigital', 'EspaçosUrbanos', 'EnergiaRenovada', 'OceanoAzul Ltda'
]

tipos_processos = [
    'Execução Fiscal', 'Trabalhista', 'Cível', 'Ambiental', 
    'Administrativo', 'Roubo', 'Fraude', 'Corrupção', 
    'Lavagem de Dinheiro', 'Homicídio', 'Difamação', 'Invasão de Privacidade',
    'Quebra de Contrato', 'Propriedade Intelectual', 'Disputa de Terras',
    'Falência', 'Assédio Sexual', 'Tráfico de Drogas', 'Contrabando',
    'Evasão de Divisas', 'Falsificação de Documentos', 'Desvios de Fundos',
    'Exploração Sexual', 'Crimes Cibernéticos', 'Estelionato', 'Despejo',
    'Adoção', 'Sucessão'
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
    'Homicídio': 'Investigação criminal relacionada a homicídio ocorrido nas dependências da empresa, envolvendo funcionários e resultando em graves implicações legais e reputacionais.',
    'Difamação': 'Caso de difamação envolvendo falsas alegações que prejudicaram a reputação de indivíduos ou empresas, resultando em pedidos de compensação.',
    'Invasão de Privacidade': 'Ação judicial movida por violação de privacidade, onde dados pessoais foram expostos sem consentimento, causando danos morais e materiais.',
    'Quebra de Contrato': 'Litígio resultante da quebra de obrigações contratuais, com pedidos de indenização por perdas e danos.',
    'Propriedade Intelectual': 'Disputa envolvendo patentes, direitos autorais e marcas registradas, com foco na proteção de inovações e criações intelectuais.',
    'Disputa de Terras': 'Caso judicial envolvendo disputas sobre posse e demarcação de terras, incluindo questões de direitos de uso e registro de propriedades.',
    'Falência': 'Processo de falência onde empresas insolventes buscam recuperação ou liquidação de ativos para pagamento de dívidas.',
    'Assédio Sexual': 'Ação judicial relacionada a assédio sexual no local de trabalho, com foco na proteção das vítimas e na busca por indenização.',
    'Tráfico de Drogas': 'Investigação e litígio envolvendo redes de tráfico de drogas, operações policiais e apreensões de substâncias ilícitas.',
    'Contrabando': 'Caso de contrabando de mercadorias através de fronteiras, com apreensões e investigações de redes criminosas.',
    'Evasão de Divisas': 'Investigação sobre remessas ilegais de dinheiro para o exterior, violando legislação cambial e resultando em fraudes financeiras.',
    'Falsificação de Documentos': 'Ação judicial envolvendo falsificação de documentos oficiais, identidade e fraudes associadas.',
    'Desvios de Fundos': 'Caso de desvio de fundos envolvendo fraudes financeiras, contas bancárias e investigações legais.',
    'Exploração Sexual': 'Investigação sobre exploração sexual e tráfico humano, com foco na proteção das vítimas e na punição dos culpados.',
    'Crimes Cibernéticos': 'Litígio envolvendo crimes cibernéticos como hacking, fraudes online e roubo de dados pessoais.',
    'Estelionato': 'Caso de estelionato onde vítimas foram enganadas para obter vantagens financeiras, resultando em litígios complexos.',
    'Despejo': 'Ação de despejo por violação de contratos de aluguel, incluindo questões de direitos de inquilinos e proprietários.',
    'Adoção': 'Processo legal de adoção, envolvendo direitos da criança, requisitos legais e disputas familiares.',
    'Sucessão': 'Caso de sucessão envolvendo partilha de heranças, testamentos e direitos dos herdeiros.'
}

status_processos = ['Em andamento', 'Concluído']
valores_envolvidos = [5000, 15000, 30000, 50000, 75000, 100000, 250000, 500000, 1000000]
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
departamentos = [
    'Financeiro', 'Recursos Humanos', 'Operacional', 'Marketing', 'Vendas', 'Jurídico',
    'Segurança', 'Compliance', 'TI', 'Auditoria', 'Produção', 'Qualidade',
    'Logística', 'Atendimento ao Cliente', 'Relações Públicas', 'Pesquisa e Desenvolvimento',
    'Manutenção', 'Expedição', 'Sustentabilidade', 'Planejamento Estratégico',
    'Controle de Riscos', 'Engenharia', 'Serviços Gerais', 'Administração'
    ]
resultados = ['Multa', 'Acordo', 'Absolvição', 'Condenação', 'Arquivamento']
sobrenomes_advogados = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima",
    "Ferreira", "Costa", "Almeida", "Ribeiro", "Carvalho", "Gomes",
    "Martins", "Rocha", "Barbosa", "Medeiros", "Nascimento", "Castro",
    "Araújo", "Cunha", "Cardoso", "Teixeira", "Vieira", "Freitas",
    "Dias", "Fernandes", "Rodrigues", "Morais", "Moura", "Duarte",
    "Mendonça", "Guimarães", "Fonseca", "Andrade", "Nunes", "Campos",
    "Reis", "Siqueira", "Monteiro", "Batista", "Farias", "Borges",
    "Barros", "Sousa", "Figueiredo", "Moraes", "Melo", "Xavier",
    "Rezende", "Bittencourt", "Queiroz", "Peixoto", "Neves", "Machado",
    "Pinto", "Torres", "Ramos", "Coelho", "Cardoso", "Sampaio"
]
tipos_tribunais = ["de Justiça", "Regional", "Superior", "do Trabalho", "Federal"]

registros = []
for empresa in empresas:
    for _ in range(random.randint(10, 70)): 
        tipo_processo = random.choice(tipos_processos)
        descricao_processo = descricoes_processos[tipo_processo]
        status_processo = random.choice(status_processos)
        data_inicio = random_date(datetime(2015, 1, 1), datetime(2023, 12, 31))
        data_conclusao = (random_date(data_inicio, datetime(2024, 12, 31)) 
                          if status_processo == 'Concluído' else '')
        valor_envolvido = f'R$ {random.choice(valores_envolvidos):,.2f}'.replace(',', '.')
        advogado_responsavel = f'Dr. {random.choice(sobrenomes_advogados)}'
        tribunal = f'Tribunal {random.choice(tipos_tribunais)}'
        regiao = random.choice(regioes)
        departamento = random.choice(departamentos)
        resultado = random.choice(resultados) if status_processo == 'Concluído' else ''
        custas_judiciais = f'R$ {random.uniform(500, 10000):,.2f}'.replace(',', '.')
        data_registro = data_inicio.strftime('%Y-%m-%d') 
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