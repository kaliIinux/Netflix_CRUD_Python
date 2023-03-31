import inquirer

def menu():
    
    while True:
        questions = [
        inquirer.List('option',
                        message="O que você deseja fazer?",
                        choices=['CADASTRAR USUÁRIO', 'LOGIN', 'SAIR'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        return answers['option']

if menu() == 'SAIR':
    exit()

elif menu() == 'CADASTRAR USUÁRIO':
    

    
    
menu()
