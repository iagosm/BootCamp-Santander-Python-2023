# Análise do Plano de Execução

Ela nos permite examinar as operações realizadas, as tabelas acessadas, os índices utilizados
e outras informações importantes para identificar possiveis melhorias de desempenho.

{
  EXPLAIN SELECT * {{tabela}}
}

# Análise do Plano de Execução 
° select_type:"SIMPLE","SUBQUERY", "JOIN" table
° type: "ALL", "INDEX" entre outros
° possible_keys: Os índices possíveis que podem ser utilizados na operação
° key: o índice utilizado na operação, se aplicavel
° key_len: o comprimento do índice utilizado
° ref: as colunas ou constantes usadas para acessar o índice rows

# Índices de Busca
{
  CREATE INDEX {{nome_index}}
  ON {{tabela}} ({{coluna1, coluna2}}); 
}