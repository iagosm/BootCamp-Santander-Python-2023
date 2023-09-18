# Junções: Tipos
° INNER JOIN
° LEFT JOIN OU LEFT OUTER JOIN
° RIGHT JOIN OU RIGHT OUTER JOIN
° FULL JOIN OU FULL OUTER JOIN 

<!-- Inner Join -->

# Retorna apenas as linhas que tem correspondencia em ambas as tabelas
# envolvidas na junção. A junção é feita com base em uma condição de igualdade especificada na clausula ON.
 
SELECT * 
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna; 

<!-- Left Join -->

# Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita
# Se não houver correspondencia, os valores  da tabela à direita serão NULL

SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna


<!-- Right Join -->

# Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da tabela à esquerda
# Se não houver correspondencia, os valores  da tabela à esquerda serão NULL

SELECT *
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna



<!-- SubConsultas -->

# Elas permitem realizar consultas mais complexas permitindo que voce use o resultado de uma consulta como entrada para outra consulta.
° SELECT
° FROM
° WHERE
° HAVING
° JOIN