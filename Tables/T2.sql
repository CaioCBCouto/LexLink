CREATE TABLE dim_processo (
    processo_id SERIAL PRIMARY KEY,
    tipo_de_processo VARCHAR(255) NOT NULL,
    prioridade VARCHAR(255),
    palavras_chave TEXT,
    tempo_medio_resolucao_mes FLOAT,
    taxa_de_sucesso FLOAT,
    custos_medios FLOAT,
    numero_medio_testemunhas INT,
    complexidade_media VARCHAR(255)
);
