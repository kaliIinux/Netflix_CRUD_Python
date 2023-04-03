import mysql.connector
import inquirer

class User:
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(user='pwpb2tbqe0be9vouc8bz', password='pscale_pw_X8PeFwzAyVOWgNAthIlT7KK9v2dGDKlqJfmjQBiylWx', host='aws.connect.psdb.cloud', database='db-netflix')#(user='root', password='', host='127.0.0.1', database='db')
        self.__cursor = self.__conexao.cursor()
    
    def add(self, name: str, plan: str, type: str):
        
        """
        Função para adicionar
        um usuário na tabela
        """
        
        self.__cursor.execute(f'INSERT INTO usuarios (name, plan, type) VALUES ("{name}", "{plan}", "{type}");')
        self.__conexao.commit()
        
    def get_all(self):
        
        """
        Função para selecionar
        todos os usuários da tabela
        """
        
        self.__cursor.execute(f'SELECT * FROM usuarios;')
        return self.__cursor.fetchall()
    
    def get_user(self, id: int):
        
        """
        Função para selecionar
        um usuário específico da tabela
        """
    
        self.__cursor.execute(f'SELECT * FROM usuarios where id = {id};')
        return self.__cursor.fetchone()
    
    def update_id(self, id: int, name: int):
        
        self.__cursor.execute(f'UPDATE usuarios SET id = {id} WHERE name = "{name}"')
        self.__conexao.commit()
    
    def update_name(self, id: int, name: str):
        
        """
        Função para atualizar
        o nome de algum filme
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET name = "{name}" WHERE id = {id}')
        self.__conexao.commit()
        
    def update_plan(self, name: str, plan: str):
        
        """
        Função para atualizar
        a classificação indicativa de 
        algum filme da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET plan = "{plan}" WHERE name = "{name}"')
        self.__conexao.commit()
        
        
    def update_type(self, name: str, type: str):
        
        """
        Função para atualizar
        a descrição de algum
        filme da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET type = "{type}" WHERE name = "{name}"')
        self.__conexao.commit()
    
    def remove_all(self):
        
        """
        Função para remover todos
        os usuários da tabela
        """
        
        self.__cursor.execute(f'DELETE FROM usuarios')
        self.__conexao.commit()

    
    def remove_user(self, name: str):
        
        """
        Função para remover um usuário
        específico
        """
        
        self.__cursor.execute(f'DELETE FROM usuarios where nome = "{name}";')
        self.__conexao.commit()
        
    def remove_user_plan(self, plan: str):
        
        """
        Função para remover um 
        usuário com base no seu plano
        """
        
        self.__cursor.execute(f'DELETE FROM usuarios where plan = "{plan}";')
        self.__conexao.commit()
        
    def remove_user_type(self, type: str):
        
        """
        Função para remover um usuário
        com base no seu tipo
        """
        
        self.__cursor.execute(f'DELETE FROM usuarios where type = "{type}";')
        self.__conexao.commit()


def Create():
    
    """
    Função que cria um usuário e 
    adiciona na tabela
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    user = User()
    user.add(name=input("Digite o nome do usuário: "), plan=input("Digite o plano: "), type=input("Digite o tipo do usuário: "))
    
def Read():
    
    """
    Função que lê usuários
    da tabela
    """
    
    questions = [
        inquirer.List('option',
                        message="What do you want to do?",
                        choices=['LER USUÁRIOS', 'LER USUÁRIO DO ÍNDICE', 'SAIR'],
                    ),
        ]
    
    answers = inquirer.prompt(questions)
    user = User()
    
    print("\x1b[2J\x1b[1;1H", end="")
    if answers['option'] == "LER USUÁRIOS":
        print("Todos os usuários: ",user.get_all())
        
    elif answers['option'] == "LER USUÁRIO DO ÍNDICE":
        id = int(input("Digite o índice do usuário desejado: "))
        print(f"Usuário no índice {id}: ",user.get_user(id))

    else:
        exit()
        
def Update():
    
    while True:
        questions = [
                inquirer.List('option',
                                message="What do you want to do?",
                                choices=['ATUALIZAR ID', 'ATUALIZAR NOME', 'ATUALIZAR PLANO', 'ATUALIZAR TIPO', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        user = User()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'ATUALIZAR ID':
            user.update_id(id=input("Digite o novo ID: "), name=input("Digite o nome de usuário: "))
            
        elif choice == 'ATUALIZAR NOME':
            user.update_name(name=input("Digite o novo nome de usuário: "), id= input("ID do usuário: "))
            
        elif choice == 'ATUALIZAR PLANO':
            user.update_plan(plan=input("Digite o novo plano do usuário: "), name= input("nome do usuário: "))
            
        elif choice == 'ATUALIZAR TIPO':
            user.update_type(type=input("Digite o novo tipo do usuário: "), name= input("nome do usuário: "))
            
        else:
            break
            

def Delete():
    
    """
    Funçao menu com todas 
    as opções de remoções que
    são possíveis realizar na
    tabela usuários
    """
    
    while True:
        questions = [
                inquirer.List('option',
                                message="What do you want to do?",
                                choices=['DELETAR TODOS OS USUÁRIOS', 'DELETAR USUÁRIO', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        user = User()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'DELETAR TODOS OS USUÁRIOS':
            user.remove_all()
            
        elif choice == 'DELETAR USUÁRIO':
            user.remove_user(name= input("Digite o nome do usuário: "))
            
        else:
            break

def menu_users():
    
    questions = [
        inquirer.List('option',
                        message="What do you want to do?",
                        choices=['CADASTRAR USUÁRIOS', 'UPDATE USER', 'REMOVE USER', 'SAIR'],
                    ),
        ]
    
    answers = inquirer.prompt(questions)
    choice = answers ['option']
    
    print("\x1b[2J\x1b[1;1H", end="")
    if choice == 'CADASTRAR USUÁRIOS':
        Create()
    
    elif choice == 'UPDATE USER':
        Update()
        
    elif choice == 'REMOVE USER':
        Delete()
    
    else:
        pass
    
    
def Login():
    
    
    while True:
        list_user = []
        users = User()
        id_user = int(input("Input your id: "))
            
        user = users.get_user(id=id_user)
        list_user.append(id_user)
        str = (user)
        
        user = input("Name: ")
        list_user.append(user)
        plan = input("Plan: ")
        list_user.append(plan)
        type = input("Type: ")
        list_user.append(type)
        
        list_user = tuple(list_user)  

        print("\x1b[2J\x1b[1;1H", end="")
        if list_user == str:
            return True
        
        else:
            print("User not found, try again")
            print()
            continue
