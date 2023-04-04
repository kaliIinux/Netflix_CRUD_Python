import mysql.connector
import inquirer

class User:
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db')
        self.__cursor = self.__conexao.cursor()
    
    def add(self, name: str, plan: str, type: str, age: int):
        
        """
        Função para adicionar
        um usuário na tabela
        """
        
        self.__cursor.execute(f'INSERT INTO usuarios (name, plan, type, age) VALUES ("{name}", "{plan}", "{type}", {age});')
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
        
        """
        Função para atualizar
        o id de algum usuário da
        tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET id = {id} WHERE name = "{name}"')
        self.__conexao.commit()
    
    def update_name(self, id: int, name: str):
        
        """
        Função para atualizar
        o nome de algum usuário
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET name = "{name}" WHERE id = {id}')
        self.__conexao.commit()
        
    def update_plan(self, name: str, plan: str):
        
        """
        Função para atualizar
        o plano de algum usuário
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET plan = "{plan}" WHERE name = "{name}"')
        self.__conexao.commit()
        
        
    def update_type(self, name: str, type: str):
        
        """
        Função para atualizar
        o tipo de algum usuário
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET type = "{type}" WHERE name = "{name}"')
        self.__conexao.commit()
        
    def update_age(self, name: str, age: int):
        
        """
        Função para atualizar
        a idade de algum usuário
        da tabela
        """
        
        self.__cursor.execute(f'UPDATE usuarios SET age = "{age}" WHERE name = "{name}"')
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
    user.add(name=input("Enter username: "), plan=input("Enter user plan:  "), type=input("Enter user type: "), age=input("Enter user age: "))
    
def Read():
    
    """
    Função que lê usuários
    da tabela
    """
    
    questions = [
        inquirer.List('option',
                        message="What do you want to do?",
                        choices=['READ USERS', 'READ USER', 'READ USER FROM AGE', 'BACK'],
                    ),
        ]
    
    answers = inquirer.prompt(questions)
    user = User()
    
    print("\x1b[2J\x1b[1;1H", end="")
    if answers['option'] == "READ USERS":
        print("All users: ",user.get_all())
        
    elif answers['option'] == "READ USER":
        print(f"User informations: ",user.get_user(id=input("Input user ID: ")))

    else:
        exit()
        
def Update():
    
    while True:
        questions = [
                inquirer.List('option',
                                message="What do you want to do?",
                                choices=['UPDATE ID', 'UPDATE NAME', 'UPDATE PLAN', 'UPDATE TYPE', 'UPDATE AGE', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        user = User()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'UPDATE ID':
            user.update_id(id=input("Enter new ID: "), name=input("Enter the username: "))
            
        elif choice == 'UPDATE NAME':
            user.update_name(name=input("Enter new username "), id= input("User ID: "))
            
        elif choice == 'UPDATE PLAN':
            user.update_plan(plan=input("Enter new user plan: "), name= input("username: "))
            
        elif choice == 'UPDATE TYPE':
            user.update_type(type=input("Enter new usesr type "), name= input("username: "))
            
        elif choice == 'UPDATE AGE':
            user.update_age(age=input("Enter new age: "), name=input("username: "))
            
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
                                choices=['DELETE ALL USERS', 'DELETER USER', 'BACK'],
                            ),
                ]
            
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        user = User()
        
        print("\x1b[2J\x1b[1;1H", end="")
        if choice == 'DELETE ALL USERS':
            user.remove_all()
            
        elif choice == 'DELETE USER':
            user.remove_user(name= input("Enter username: "))
            
        else:
            break

def menu_users():
    
    questions = [
        inquirer.List('option',
                        message="What do you want to do?",
                        choices=['REGISTER USERS', 'UPDATE USER', 'REMOVE USER', 'BACK'],
                    ),
        ]
    
    answers = inquirer.prompt(questions)
    choice = answers ['option']
    
    if choice == 'REGISTER USERS':
        print("\x1b[2J\x1b[1;1H", end="")
        Create()
    
    elif choice == 'UPDATE USER':
        print("\x1b[2J\x1b[1;1H", end="")
        Update()
        
    elif choice == 'REMOVE USER':
        print("\x1b[2J\x1b[1;1H", end="")
        Delete()
    
    else:
        pass
    
    
def Login():
    
    
    while True:
        list_user = []
        users = User()
        id_user = int(input("Enter your ID: "))
            
        user = users.get_user(id=id_user)
        list_user.append(id_user)
        str = (user)
        
        user = input("Name: ")
        list_user.append(user)
        plan = input("Plan: ")
        list_user.append(plan)
        type = input("Type: ")
        list_user.append(type)
        age = int(input("Age: "))
        list_user.append(age)
        
        print(str)
        print(list_user)
        list_user = tuple(list_user)  

        print("\x1b[2J\x1b[1;1H", end="")
        if list_user == str:
            return True
        
        else:
            print("User not found, try again")
            print()
            continue
