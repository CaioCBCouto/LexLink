CREATE TABLE fato_processo_juridico (
    fato_id SERIAL PRIMARY KEY,
    empresa_id INT REFERENCES dim_empresa(empresa_id),
    processo_id INT REFERENCES dim_processo(processo_id),
    advogado_id INT REFERENCES dim_advogado(advogado_id),
    tribunal_id INT REFERENCES dim_tribunal(tribunal_id),
    departamento_id INT REFERENCES dim_departamento(departamento_id),
    data_inicio DATE,
    data_conclusao DATE,
    status VARCHAR(255),
    descricao_processo TEXT,
    valor_envolvido FLOAT,
    resultado VARCHAR(255),
    custas_judiciais FLOAT,
    data_registro DATE,
    numero_processo VARCHAR(255)
);
