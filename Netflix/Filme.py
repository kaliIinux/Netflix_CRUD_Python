import inquirer
import mysql.connector



class Filme():
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db')
        self.__cursor = self.__conexao.cursor()
        
    def add(self,nome: str, classificacao: int, desc:str):
        
        """
        Função para adicionar
        um filme na tabela
        """
        
        self.__cursor.execute(f'INSERT INTO netflix (nome, classificacao, descricao) VALUES ("{nome}", "{classificacao}", "{desc}");')
        self.__conexao.commit()

    def get_all(self):
        
        """
        Função para selecionar
        todos os filmes da tabela
        """
        
        comando = f'SELECT * FROM netflix;'
        self.__cursor.execute(comando)
        return self.__cursor.fetchall()
    
    def get_movie(self,id: int):
        
        """
        Função para selecionar
        um filme específico da tabela
        """
    
        comando = f'SELECT * FROM netflix where id_filmes = {id};'
        self.__cursor.execute(comando)
        return self.__cursor.fetchone()
    
    def remove_all(self):
        
        """
        Função para remover todos os filmes
        cadastrados
        """
        
        self.__cursor.execute(f'DELETE ;')
        self.__conexao.commit()
        return self.__cursor.fetchall()
        
def create():
    filme = Filme()
    
    filme.add(nome=input("Digite o nome do filme: "), classificacao=input("Digite a classificação: "), desc=input("Insira a descrição do filme: "))
        
    print('A TABELA FICOU ASSIM: ',filme.remove_all())
    
create()





