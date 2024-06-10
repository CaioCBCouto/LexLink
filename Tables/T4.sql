CREATE TABLE dim_tribunal (
    tribunal_id SERIAL PRIMARY KEY,
    nome_tribunal VARCHAR(255) NOT NULL,
    regiao VARCHAR(255)
);
