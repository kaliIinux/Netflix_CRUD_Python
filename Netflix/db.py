import mysql.connector

try:
    conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='netflix')
    cursor = conexao.cursor()
    
except Exception as e:
    print('Conection failed, try again')
    
else:
    conexao.is_connected()
    
finally:
    cursor.close()
    conexao.close()

    """
    CREATE TABLES:
    
CREATE TABLE `filmes` (
 `id_filmes` int NOT NULL AUTO_INCREMENT,
 `nome` varchar(50),
 `classificacao` int,
 `descricao` varchar(50),
 PRIMARY KEY (`id_filmes`)
 ) ENGINE InnoDB,
 CHARSET utf8mb4,
 COLLATE utf8mb4_0900_ai_ci;
 
 CREATE TABLE `usuarios` (
 `id` int NOT NULL AUTO_INCREMENT,
 `name` varchar(50),
 `plan` varchar(50),
 `type` varchar(50),
 PRIMARY KEY (`id`)
 ) ENGINE InnoDB,
 CHARSET utf8mb4,
 COLLATE utf8mb4_0900_ai_ci;
    
    """

