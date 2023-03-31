import mysql.connector


conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='netflix')
cursor = conexao.cursor()

cursor.close()
conexao.close()

nome_produto = "chocolate"
valor = 5
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' # ESCREVE O COMANDO
cursor.execute(comando) # MANDA O COMANDO SER EXECUTADO
conexao.commit() # EDITA O BANCO DE DADOS(CRIAR, EDITAR OU DELETAR)
resultado = cursor.fetchall() #LER O BANCO DE DADOS
