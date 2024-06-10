import csv

# Dados adicionais por tipo de processo
dados_adicionais = {
    'Execução Fiscal': ['Média', 'Fazenda Pública, Dívida Fiscal, Irregularidades Financeiras', 12, 0.75, 'R$ 10.000,00', 2, 'Alta'],
    'Trabalhista': ['Alta', 'Assédio Moral, Horas Extras, Rescisão Contratual', 18, 0.65, 'R$ 15.000,00', 3, 'Média'],
    'Cível': ['Média', 'Contratos, Danos Materiais, Indenização', 15, 0.70, 'R$ 20.000,00', 1, 'Média'],
    'Ambiental': ['Alta', 'Contaminação, Desmatamento, Poluição', 24, 0.60, 'R$ 50.000,00', 5, 'Alta'],
    'Administrativo': ['Média', 'Licitações, Irregularidades, Normas Setoriais', 10, 0.80, 'R$ 12.000,00', 1, 'Baixa'],
    'Roubo': ['Alta', 'Propriedade Intelectual, Bens Valiosos, Suspeitos', 36, 0.50, 'R$ 100.000,00', 4, 'Alta'],
    'Fraude': ['Alta', 'Manipulação de Balanços, Evasão Fiscal, Práticas Ilícitas', 30, 0.55, 'R$ 80.000,00', 2, 'Alta'],
    'Corrupção': ['Alta', 'Suborno, Contratos Governamentais, Vantagens Ilícitas', 24, 0.60, 'R$ 75.000,00', 3, 'Alta'],
    'Lavagem de Dinheiro': ['Alta', 'Operações Financeiras, Fundos Ilícitos, Ramificações Internacionais', 48, 0.40, 'R$ 150.000,00', 6, 'Alta'],
    'Homicídio': ['Alta', 'Funcionários, Implicações Legais, Reputacionais', 36, 0.45, 'R$ 120.000,00', 4, 'Alta']
}

# Gerar registros para o CSV
registros_info = []
for tipo_processo, detalhes in dados_adicionais.items():
    prioridade, palavras_chave, tempo_medio, taxa_sucesso, custos_medios, num_testemunhas, complexidade = detalhes
    registros_info.append([
        tipo_processo,
        prioridade,
        palavras_chave,
        tempo_medio,
        taxa_sucesso,
        custos_medios,
        num_testemunhas,
        complexidade
    ])

# Escrever o CSV
with open('processos_juridicos_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Tipo de Processo', 'Prioridade', 'Palavras-Chave', 
        'Tempo Médio de Resolução (meses)', 'Taxa de Sucesso', 
        'Custos Médios', 'Número Médio de Testemunhas', 'Complexidade Média'
    ])
    writer.writerows(registros_info)