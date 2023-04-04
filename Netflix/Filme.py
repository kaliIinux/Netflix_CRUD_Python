import mysql.connector, inquirer, time
from prettytable import PrettyTable


class Film():
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db')
        self.__cursor = self.__conexao.cursor()
    
        
    def add(self, nome: str, classificacao: int, desc:str):
        
        """
        Função para adicionar
        um filme na tabela
        """
        
        self.__cursor.execute(f'INSERT INTO filmes (nome, classificacao, descricao) VALUES ("{nome}", "{classificacao}", "{desc}");')
        self.__conexao.commit()

    def get_all(self):
        
        """
        Função para selecionar
        todos os filmes da tabela
        """
        
        self.__cursor.execute(f'SELECT * FROM filmes;')
        lines = self.__cursor.fetchall()
        tabel = PrettyTable()
        tabel.field_names = ["ID", "NAME", "CLASS", "DESC"]
        
        for line in lines:
            tabel.add_row(line)
            
        print(tabel)
        
    def get_movie(self, name: str):
        
        """
        Função para selecionar
        um filme específico da tabela
        """
    
        self.__cursor.execute(f'SELECT * FROM filmes where nome = "{name}";')
        
        print(self.__cursor.fetchone())
        print()
    
    def get_movie_class(self, classificacao: int):
        
        """
        Função para selecionar
        um filme específico da tabela
        """
    
        self.__cursor.execute(f'SELECT * FROM filmes where classificacao = {classificacao};')
        print(self.__cursor.fetchall())
        
    def update_id(self, id: int, name: int):
        
        self.__cursor.execute(f'UPDATE filmes SET id_filmes = {id} WHERE nome = "{name}"')
        self.__conexao.commit()
    
    def update_name(self, id: int, name: str):
        
        """
        Função para atualizar
        o nome de algum filme
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE filmes SET nome = "{name}" WHERE id_filmes = {id}')
        self.__conexao.commit()
        
    def update_class(self, name: str, classificacao: int):
        
        """
        Função para atualizar
        a classificação indicativa de 
        algum filme da tabela
        """
        
        self.__cursor.execute(f'UPDATE filmes SET classificacao = "{classificacao}" WHERE nome = "{name}"')
        self.__conexao.commit()
        
        
    def update_desc(self, name: str, desc: str):
        
        """
        Função para atualizar
        a descrição de algum
        filme da tabela
        """
        
        self.__cursor.execute(f'UPDATE filmes SET descricao = "{desc}" WHERE nome = "{name}"')
        self.__conexao.commit()
        
        
    def remove_all(self):
        
        """
        Função para remover todos
        os filmes da lista
        """
        
        self.__cursor.execute(f'DELETE FROM filmes')
        self.__conexao.commit()

    
    def remove_movie(self, name):
        
        """
        Função para remover um filme
        cadastrado
        """
        
        self.__cursor.execute(f'DELETE FROM filmes where nome = "{name}";')
        self.__conexao.commit()
        
    def remove_movie_class(self, classificacao: int):
        
        """
        Função para remover um filme
        com base na sua classificação 
        indicativa
        """ 
        
        self.__cursor.execute(f'DELETE FROM filmes where classificacao = {classificacao};')
        self.__conexao.commit()
        
    def remove_movie_desc(self, desc: str):
        
        """
        Função para remover um filme
        com base na sua descrição
        """
        
        self.__cursor.execute(f'DELETE FROM filmes where descricao = "{desc}";')
        self.__conexao.commit()
        
def Create():
    
    """
    Cria um filme e adiciona
    na tabela
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    film = Film()
    film.add(nome=input("Imput movie name: "), classificacao=input("Imput the classification: "), desc=input("Imput the description of movie: "))

def Read():
    
    """
    Função menu com todas
    as opções de leitura que são
    possíveis realizar na
    tabela filmes
    """
    
    while True:
        questions = [
            inquirer.List('option',
                            message="What do you want to do?",
                            choices=['READ ALL MOVIES', 'READ SPECIFIC MOVIE', 'READ MOVIES BY CLASSIFICATION', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'READ ALL MOVIES':
        
            print("ALL MOVIES:")
            print(film.get_all())
            time.sleep(3)
            print("\x1b[2J\x1b[1;1H", end="")
            
        elif choice == 'READ SPECIFIC MOVIE':
            film.get_movie(name=input("Input the name of movie: "))

        elif choice ==  'READ MOVIES BY CLASSIFICATION':
            film.get_movie_class(classificacao=input("Input movie classification: "))
            
        else:
            break

def Update():
    
    """
    Funçao menu com todas 
    as opções de atualizações que
    são possíveis realizar na
    tabela filmes
    """

    while True:
        questions = [
                inquirer.List('option',
                                message="What do you want to do?",
                                choices=['UPDATE ID', 'UPDATE NAME', 'UPDATE CLASSIFICATION', 'UPDATE DESCRIPTION', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'UPDATE ID':
            film.update_id(id= input("Input new ID: "), name= input("What is the name of movie? "))
            
        elif choice == 'UPDATE NAME':
            film.update_name(name= input("Input the new name: "), id= input("movie ID: "))
            
        elif choice == 'UPDATE CLASSIFICATION':
            film.update_class(classificacao= input("Input the new classification: "), name= input("movie name: "))
            
        elif choice == 'UPDATE DESCRIPTION':
            film.update_desc(desc= input("Input the new description: "), name= input("movie name: "))
    
        else:
            break

def Remove():
    
    """
    Funçao menu com todas 
    as opções de remoções que
    são possíveis realizar na
    tabela filmes
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    while True:
        questions = [
            inquirer.List('option',
                            message="What do you want to do?",
                            choices=['REMOVE ALL MOVIES', 'REMOVE SPECIFY MOVIE',
                                    'REMOVE MOVIE BY CLASSIFICATION', 'REMOVE MOVIE BY DESCRIPTION', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'REMOVE ALL MOVIES':
            film.remove_all()
        
        elif choice == 'REMOVE SPECIFY MOVIE':
            film.remove_movie(name=input("Input movie name: "))
            
        elif choice == 'REMOVE MOVIE BY CLASSIFICATION':
            film.remove_movie_class(classificacao=input("Input movie classification: "))
        
        elif choice == 'REMOVE MOVIE BY DESCRIPTION':
            film.remove_movie_desc(desc=input("Input the description: "))
            
        else: 
            print("\x1b[2J\x1b[1;1H", end="") 
            break


def menu_films():
    
    print("\x1b[2J\x1b[1;1H", end="")
    while True:
        
        questions = [
            inquirer.List('option',
                            message="What do you want to do",
                            choices=['ADD MOVIES', 'READ MOVIES', 'UPDATE MOVIES', 'REMOVE MOVIES', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        if choice == 'ADD MOVIES':
            print("\x1b[2J\x1b[1;1H", end="")
            Create()

        elif choice == 'READ MOVIES':
            print("\x1b[2J\x1b[1;1H", end="")
            Read()
        
        elif choice == 'UPDATE MOVIES':
            print("\x1b[2J\x1b[1;1H", end="")
            Update()
                    
        elif choice == 'REMOVE MOVIES':
            print("\x1b[2J\x1b[1;1H", end="")
            Remove()
            
        else:
            print("\x1b[2J\x1b[1;1H", end="")
            break