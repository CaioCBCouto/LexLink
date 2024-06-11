import csv
import random

def random_keywords(keywords):
    random.shuffle(keywords)
    return ', '.join(keywords[:random.randint(1, len(keywords))])

dados_adicionais = {
    'Execução Fiscal': [['Baixa', 'Média', 'Alta'], ['Fazenda Pública', 'Dívida Fiscal', 'Irregularidades Financeiras', 'Impostos'], 12, 0.75, 'R$ 10.000,00', 2, 'Alta'],
    'Trabalhista': [['Baixa', 'Média', 'Alta'], ['Assédio Moral', 'Horas Extras', 'Rescisão Contratual', 'Salários'], 18, 0.65, 'R$ 15.000,00', 3, 'Média'],
    'Cível': [['Baixa', 'Média', 'Alta'], ['Contratos', 'Danos Materiais', 'Indenização', 'Propriedade'], 15, 0.70, 'R$ 20.000,00', 1, 'Média'],
    'Ambiental': [['Baixa', 'Média', 'Alta'], ['Contaminação', 'Desmatamento', 'Poluição', 'Resíduos'], 24, 0.60, 'R$ 50.000,00', 5, 'Alta'],
    'Administrativo': [['Baixa', 'Média', 'Alta'], ['Licitações', 'Irregularidades', 'Normas Setoriais', 'Contratos'], 10, 0.80, 'R$ 12.000,00', 1, 'Baixa'],
    'Roubo': [['Baixa', 'Média', 'Alta'], ['Propriedade Intelectual', 'Bens Valiosos', 'Suspeitos', 'Furtos'], 36, 0.50, 'R$ 100.000,00', 4, 'Alta'],
    'Fraude': [['Baixa', 'Média', 'Alta'], ['Manipulação de Balanços', 'Evasão Fiscal', 'Práticas Ilícitas', 'Fraude Contábil'], 30, 0.55, 'R$ 80.000,00', 2, 'Alta'],
    'Corrupção': [['Baixa', 'Média', 'Alta'], ['Suborno', 'Contratos Governamentais', 'Vantagens Ilícitas', 'Desvios'], 24, 0.60, 'R$ 75.000,00', 3, 'Alta'],
    'Lavagem de Dinheiro': [['Baixa', 'Média', 'Alta'], ['Operações Financeiras', 'Fundos Ilícitos', 'Ramificações Internacionais', 'Transações'], 48, 0.40, 'R$ 150.000,00', 6, 'Alta'],
    'Homicídio': [['Baixa', 'Média', 'Alta'], ['Funcionários', 'Implicações Legais', 'Reputacionais', 'Crimes'], 36, 0.45, 'R$ 120.000,00', 4, 'Alta'],
    'Difamação': [['Baixa', 'Média', 'Alta'], ['Reputação', 'Mídia', 'Falsas Alegações', 'Compensação'], 14, 0.65, 'R$ 8.000,00', 1, 'Média'],
    'Invasão de Privacidade': [['Baixa', 'Média', 'Alta'], ['Dados Pessoais', 'Consentimento', 'Exposição Pública', 'Direitos de Privacidade'], 20, 0.55, 'R$ 10.000,00', 2, 'Média'],
    'Quebra de Contrato': [['Baixa', 'Média', 'Alta'], ['Obrigações Contratuais', 'Indenização', 'Acordos Comerciais', 'Disputas Legais'], 22, 0.60, 'R$ 18.000,00', 2, 'Média'],
    'Propriedade Intelectual': [['Baixa', 'Média', 'Alta'], ['Patentes', 'Direitos Autorais', 'Marcas Registradas', 'Inovação'], 16, 0.75, 'R$ 22.000,00', 1, 'Alta'],
    'Disputa de Terras': [['Baixa', 'Média', 'Alta'], ['Posse', 'Demarcação', 'Direitos de Uso', 'Registro de Terras'], 28, 0.50, 'R$ 30.000,00', 3, 'Média'],
    'Falência': [['Baixa', 'Média', 'Alta'], ['Dívidas', 'Insolvência', 'Plano de Recuperação', 'Liquidação'], 34, 0.45, 'R$ 25.000,00', 5, 'Alta'],
    'Assédio Sexual': [['Baixa', 'Média', 'Alta'], ['Violência', 'Condição de Trabalho', 'Proteção de Vítimas', 'Indenização'], 12, 0.55, 'R$ 20.000,00', 3, 'Alta'],
    'Tráfico de Drogas': [['Baixa', 'Média', 'Alta'], ['Substâncias Ilícitas', 'Redes Criminosas', 'Operações Policiais', 'Legislação'], 40, 0.30, 'R$ 80.000,00', 7, 'Alta'],
    'Contrabando': [['Baixa', 'Média', 'Alta'], ['Mercadorias Ilícitas', 'Fronteiras', 'Apreensões', 'Investigação'], 25, 0.45, 'R$ 45.000,00', 3, 'Alta'],
    'Evasão de Divisas': [['Baixa', 'Média', 'Alta'], ['Remessas Ilegais', 'Legislação Cambial', 'Investigações', 'Fraudes'], 18, 0.50, 'R$ 70.000,00', 2, 'Alta'],
    'Falsificação de Documentos': [['Baixa', 'Média', 'Alta'], ['Identidade', 'Documentos Oficiais', 'Fraude', 'Legislação'], 10, 0.65, 'R$ 15.000,00', 1, 'Alta'],
    'Desvios de Fundos': [['Baixa', 'Média', 'Alta'], ['Fraude Financeira', 'Contas Bancárias', 'Legislação', 'Investigações'], 32, 0.50, 'R$ 90.000,00', 4, 'Alta'],
    'Exploração Sexual': [['Baixa', 'Média', 'Alta'], ['Tráfico Humano', 'Proteção de Vítimas', 'Legislação', 'Investigações'], 36, 0.35, 'R$ 60.000,00', 6, 'Alta'],
    'Crimes Cibernéticos': [['Baixa', 'Média', 'Alta'], ['Hackers', 'Dados Pessoais', 'Fraudes Online', 'Legislação'], 28, 0.40, 'R$ 55.000,00', 5, 'Alta'],
    'Estelionato': [['Baixa', 'Média', 'Alta'], ['Fraude', 'Engano', 'Vítimas', 'Compensação'], 14, 0.55, 'R$ 12.000,00', 3, 'Média'],
    'Despejo': [['Baixa', 'Média', 'Alta'], ['Propriedade', 'Contrato de Aluguel', 'Direitos de Inquilinos', 'Legislação'], 20, 0.60, 'R$ 8.000,00', 2, 'Média'],
    'Adoção': [['Baixa', 'Média', 'Alta'], ['Processos Legais', 'Direitos da Criança', 'Família', 'Legislação'], 12, 0.75, 'R$ 5.000,00', 1, 'Média'],
    'Sucessão': [['Baixa', 'Média', 'Alta'], ['Herança', 'Testamento', 'Partilha de Bens', 'Direitos'], 22, 0.70, 'R$ 18.000,00', 3, 'Média']
}

registros_info = []
for tipo_processo, detalhes in dados_adicionais.items():
    prioridades, palavras_chave, tempo_medio, taxa_sucesso, custos_medios, num_testemunhas, complexidade = detalhes
    prioridade_random = random.choice(prioridades)
    palavras_chave_random = random_keywords(palavras_chave)
    taxa_sucesso_random = round(random.uniform(0.4, 0.9), 2)
    custos_medios_random = f'R$ {random.randint(5000, 150000):,.2f}'.replace(',', '.')
    complexidade_random = random.choice(['Baixa', 'Média', 'Alta'])
    
    registros_info.append([
        tipo_processo,
        prioridade_random,
        palavras_chave_random,
        tempo_medio,
        taxa_sucesso_random,
        custos_medios_random,
        num_testemunhas,
        complexidade_random
    ])

with open('processos_juridicos_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Tipo de Processo', 'Prioridade', 'Palavras-Chave', 
        'Tempo Médio de Resolução (meses)', 'Taxa de Sucesso', 
        'Custos Médios', 'Número Médio de Testemunhas', 'Complexidade Média'
    ])
    writer.writerows(registros_info)