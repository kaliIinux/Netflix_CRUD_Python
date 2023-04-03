import mysql.connector, inquirer, time


class Film():
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(user='ud5oh01997pbaodhbmps', password='pscale_pw_FW04EYmmsYOCoMFeiV0oD0VXm18vgXi1lDzdHTNc0mP', host='aws.connect.psdb.cloud', database='db-netflix')#(user='root', password='', host='127.0.0.1', database='db')
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
        print(self.__cursor.fetchall())
    
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
    film.add(nome=input("Digite o nome do filme: "), classificacao=input("Digite a classificação: "), desc=input("Insira a descrição do filme: "))

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
                            message="O que você deseja fazer?",
                            choices=['LISTAR TODOS OS FILMES', 'LISTAR FILME ESPECÍFICO', 'LISTAR FILMES POR CLASSIFICAÇÃO', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'LISTAR TODOS OS FILMES':
        
            print("FILMES CADASTRADOS:")
            print(film.get_all())
            time.sleep(3)
            print("\x1b[2J\x1b[1;1H", end="")
            
        elif choice == 'LISTAR FILME ESPECÍFICO':
            film.get_movie(name=input("DIGITE O NOME DO FILME: "))

        elif choice ==  'LISTAR FILMES POR CLASSIFICAÇÃO':
            film.get_movie_class(classificacao=input("DIGITE A CLASSIFICAÇÃO DO FILME: "))
            
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
                                message="O que você deseja fazer?",
                                choices=['ATUALIZAR ID', 'ATUALIZAR NOME', 'ATUALIZAR CLASSIFICAÇÃO', 'ATUALIZAR DESCRIÇÃO', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'ATUALIZAR ID':
            film.update_id(id= input("Digite o novo id: "), name= input("Qual o nome do filme? "))
            
        elif choice == 'ATUALIZAR NOME':
            film.update_name(name= input("Digite o novo nome: "), id= input("ID do filme: "))
            
        elif choice == 'ATUALIZAR CLASSIFICAÇÃO':
            film.update_class(classificacao= input("Digite a nova classificação: "), name= input("nome do filme: "))
            
        elif choice == 'ATUALIZAR DESCRIÇÃO':
            film.update_desc(desc= input("Digite a nova descrição: "), name= input("nome do filme: "))
    
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
                            message="O que você deseja fazer?",
                            choices=['REMOVER TODOS OS FILMES', 'REMOVER FILME ESPECÍFICO',
                                    'REMOVER FILME POR CLASSIFICAÇÃO', 'REMOVER FILME POR DESCRIÇÃO', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        film = Film()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'REMOVER TODOS OS FILMES':
            film.remove_all()
        
        elif choice == 'REMOVER FILME ESPECÍFICO':
            film.remove_movie(name=input("DIGITE O NOME DO FILME: "))
            
        elif choice == 'REMOVER FILME POR CLASSIFICAÇÃO':
            film.remove_movie_class(classificacao=input("DIGITE A CLASSIFICAÇÃO DO FILME: "))
        
        elif choice == 'REMOVER FILME POR DESCRIÇÃO':
            film.remove_movie_desc(desc=input("DIGITE A DESCRIÇÃO: "))
            
        else: 
            print("\x1b[2J\x1b[1;1H", end="") 
            break


def menu_films():
    
    print("\x1b[2J\x1b[1;1H", end="")
    while True:
        
        questions = [
            inquirer.List('option',
                            message="O que você deseja fazer?",
                            choices=['ADICIONAR FILMES', 'VER FILMES', 'ATUALIZAR FILMES', 'REMOVER FILMES', 'BACK'],
                        ),
            ]
        
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        if choice == 'ADICIONAR FILMES':
            print("\x1b[2J\x1b[1;1H", end="")
            Create()

        elif choice == 'VER FILMES':
            print("\x1b[2J\x1b[1;1H", end="")
            Read()
        
        elif choice == 'ATUALIZAR FILMES':
            print("\x1b[2J\x1b[1;1H", end="")
            Update()
                    
        elif choice == 'REMOVER FILMES':
            print("\x1b[2J\x1b[1;1H", end="")
            Remove()
            
        else:
            print("\x1b[2J\x1b[1;1H", end="")
            break
