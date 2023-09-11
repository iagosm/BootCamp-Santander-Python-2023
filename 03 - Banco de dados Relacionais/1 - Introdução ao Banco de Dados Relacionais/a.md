# MER e DER

O Modelo de Entidade-Relacionamento (MER) é representado através de diagramas chamados Diagramas Entidade-Relacionamento (DER), modelo conceitual usado para representar estrutura geral de um banco de dados.

# Entidades
 As entidades são nomeadas com substantivos concretos ou abstratos que representem de forma clara sua função dentro do domínio
 
 ° Usuários
 ° Destinos 
 ° Reservas

 # Atributos 
Os atributos são as caracteristicas ou propriedades das entidades. Eles descrevem informações especificas sobre uma entidade.

Usuários {
° Nome
° Email
° Senha
}

# Relacionamentos
Os relacionamentos representam as associações entre entidades 

# Cardinalidade
° Relacionamento 1..1 ou (um para um )
° Relacionamento 1..n ou 1..* ( um para muitos)
° Relacionamento n..n ou *..* (Muitos para muitos)

# Tabelas
Utilizadas para armazenar dados de forma organizada. Cada tabela em um banco de dados relacional tem um nome único e é dividida em colunas e linhas.

# Colunas
Uma coluna é uma estrutura dentro de uma tabela que representa um atributo especifico dos dados armazenados.

# Registros
Um registro também é conhecido como linha ou tupla, é uma instância individual de dados em uma tabela

CREATE TABLE {{nome}}
({{coluna}}{{tipo}}{{opções}}) COMMENT
{{`Comentario`}}

# Opções
Restrições de valor {
  °NOT NULL
  °UNIQUE
  °DEFAULT
}
Chaves primarias e estrangeiras
Auto Incremento

# Tipos de Dados
Os dados podem variar muito entre diversos SGBD, os mais comuns são:
°Inteiro (Integer)
°Decimal/Numerico(Decimal/Numeric)
°Caractere/Varchar(Character/Varchar)
°Data/Hora (Date/Time)
°Booleano (Boolean)
°Texto Longo (Text)

# Operadores

° = (igualdade)
° <> ou != (desigualdade)
° > (maior que)
° < (menor que)
° >= (maior ou igual que)
° <= (menor ou igual que)
° LIKE (comparação de padrões)
° IN (pertence a uma lista de valores)
° BETWEEN ( dentro de um intervalo)
° AND (e lógico)
° OR (ou lógico)

# Normalização de Dados
A normalização de dados é um processo no qual se organiza e estrutura um banco de dados relacional de forma a eliminar redundâncias e anomalias, garantindo a consistencia e integridade dos dados.

# Formas Normais
1FN : Atomicidade de Dados
A 1FN estabelece que cada valor em uma tabela deve ser atômico, ou seja, indivisivel. Nenhum campo deve conter múltiplos valores ou listas. No seu caso, o campo "endereço" contem multiplos vaores, como rua, numero, estado e cidade. Para atingir a 1FN, precisamos dividir o campo "endereços" em colunas separadas.