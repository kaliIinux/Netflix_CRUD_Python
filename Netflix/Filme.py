import inquirer
import mysql.connector

conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='crud_python')
cursor = conexao.cursor()

cursor.close()
conexao.close()
    
nome_filme = "camelo"
comando = f'INSERT INTO netflix (filmes) VALUES ("{nome_filme}")' # ESCREVE O COMANDO
cursor.execute(comando) # MANDA O COMANDO SER EXECUTADO
conexao.commit() # EDITA O BANCO DE DADOS(CRIAR, EDITAR OU DELETAR)
resultado = cursor.fetchall() #LER O BANCO DE DADOS
    



